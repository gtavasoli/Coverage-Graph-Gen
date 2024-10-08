# Wget

This example visualize the execution path for different kind of input to CURL. We are using following command to get the wget.

```
wget https://ftp.gnu.org/gnu/wget/wget-<version>.tar.gz
tar xvf wget-<version>.tar.gz
cd wget-<version>

./configure CC=afl-clang-fast CXX=afl-clang-fast++
```

## Generate execution path
```
afl-showmap -o ./coverage_data/cd_1.txt -m none -- ./src/wget2 "https://www.google.com"
afl-showmap -o ./coverage_data/cd_2.txt -m none -- ./src/wget2 "https://w"
afl-showmap -o ./coverage_data/cd_3.txt -m none -- ./src/wget2 "https://cdnjs.cloudflare.com/ajax/libs/jquery/3.7.1/jquery.min.js"
afl-showmap -o ./coverage_data/cd_4.txt -m none -- ./src/wget2 "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAAA3NCSVQICAjb4U/gAAAABlBMVEXMzMz////TjRV2AAAACXBIWXMAAArrAAAK6wGCiw1aAAAAHHRFWHRTb2Z0d2FyZQBBZG9iZSBGaXJld29ya3MgQ1M26LyyjAAAABFJREFUCJlj+M/AgBVhF/0PAH6/D/HkDxOGAAAAAElFTkSuQmCC"
```
