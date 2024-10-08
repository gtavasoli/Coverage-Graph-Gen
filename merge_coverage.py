import glob
import json
import os
import pandas as pd
import networkx as nx
from jinja2 import Environment, FileSystemLoader

def load_coverage_data(file) -> pd.DataFrame:
    """
    Load coverage data from a file. Coverage data should be generated by afl-showmap (AFL++ fuzzer).

    Format: <edge_id>:<hit_count>
    - edge_id: The unique identifier for the edge (a transition between two points in the program).
    - hit_count: The number of times that edge was executed during the fuzz run.

    Example format:
    000007:1
    000009:1
    000011:4
    000012:4
    000013:1
    000014:5

    args:
    - file: The path to the coverage file. 

    returns:
    - A pandas DataFrame with two columns: "node" and "count".
    """
    return pd.read_csv(file, sep=":", header=None, names=["node", "count"])

def add_edges_from_file_to_graph(df, G) -> None:
    """
    Add edges from a DataFrame to a graph. Sequential edges based on execution.
    
    args:
    - df: The DataFrame with the coverage data.
    - G: The networkx graph to add edges

    returns:
    - None
    """
    nodes = list(df["node"])
    for i in range(1, len(nodes)):
        G.add_edge(nodes[i-1], nodes[i])

def generate_interactive_graph_html(G, coverage_df, graph_title, output_file) -> None:
    """
    Generate an HTML file with an interactive graph using a Jinja2 template.

    args:
    - G: The networkx graph to visualize.
    - coverage_df: The coverage data used to color the nodes.
    - graph_title: The title of the graph.
    - output_file: The output HTML file.

    returns:
    - None
    """

    # Add nodes with different colors based on multiple inputs or outputs
    nodes = []
    start_node = int(coverage_df["node"].min())  # Convert to Python int
    end_node = int(coverage_df["node"].max())  # Convert to Python int

    for node in G.nodes:
        node_color = 'skyblue'
        if G.in_degree(node) > 1 or G.out_degree(node) > 1:
            node_color = 'orange'  # Highlight nodes with multiple inputs or outputs
        elif node == start_node:
            node_color = 'red'
        elif node == end_node:
            node_color = 'green'
        nodes.append({"id": node, "label": str(node), "color": node_color})

    # Create edges
    edges = [{"from": int(u), "to": int(v)} for u, v in G.edges()]

    # Setup Jinja2 environment and render template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    rendered_html = template.render(
        nodes=json.dumps(nodes),
        edges=json.dumps(edges),
        start_node=start_node,
        end_node=end_node,
        graph_title=graph_title
    )

    with open(output_file, 'w') as f:
        f.write(rendered_html)

def process_each_file(file_pattern) -> None:
    """
    Generate HTML files for each individual file and a merged file.

    args:
    - file_pattern: The pattern to match the coverage files.

    returns:
    - None
    """
    files = glob.glob(file_pattern)
    
    # Create a new graph for the merged version
    merged_graph = nx.DiGraph()

    # Generate a graph for each individual coverage file
    for file in files:
        df = load_coverage_data(file)
        file_name = os.path.basename(file).replace('.txt', '')  # Get a clean file name
        output_file = f"{file_name}_graph.html"  # Create an output HTML filename
        print(f"Generating graph for {file_name}")
        
        # Create a separate graph for this file
        G = nx.DiGraph()
        add_edges_from_file_to_graph(df, G)
        
        # Generate HTML for the individual graph
        generate_interactive_graph_html(G, df, graph_title=f"Graph for {file_name}", output_file=output_file)
        
        # Add the edges to the merged graph
        add_edges_from_file_to_graph(df, merged_graph)
    
    # Generate the merged graph
    print("Generating merged graph")
    merged_df = pd.concat([load_coverage_data(file) for file in files]).drop_duplicates()
    generate_interactive_graph_html(merged_graph, merged_df, graph_title="Merged Coverage Graph", output_file="merged_graph.html")

if __name__ == "__main__":
    file_pattern = 'cd_*.txt'  # Default pattern for input files
    process_each_file(file_pattern)
