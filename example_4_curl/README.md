# CURL

This example visualize the execution path for different kind of input to CURL. We are using the following commit of CURL.

https://github.com/curl/curl/commit/a610bb8d92c73b07b599f90b9f22361047c39a84

## Generate execution path
```
afl-showmap -o ./coverage_data/cd_1.txt -m none -t 10000 -- ./src/curl "https://www.google.com"
afl-showmap -o ./coverage_data/cd_2.txt -m none -t 10000 -- ./src/curl "https://w"
afl-showmap -o ./coverage_data/cd_3.txt -m none -t 10000 -- ./src/curl "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"
afl-showmap -o ./coverage_data/cd_4.txt -m none -t 10000 -- ./src/curl "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAAA3NCSVQICAjb4U/gAAAABlBMVEXMzMz////TjRV2AAAACXBIWXMAAArrAAAK6wGCiw1aAAAAHHRFWHRTb2Z0d2FyZQBBZG9iZSBGaXJld29ya3MgQ1M26LyyjAAAABFJREFUCJlj+M/AgBVhF/0PAH6/D/HkDxOGAAAAAElFTkSuQmCC"
```