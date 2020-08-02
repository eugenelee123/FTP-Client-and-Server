Contributors: \
Eugene Lee eugene097@csu.fullerton.edu
Bradley Keizer brad14@csu.fullerton.edu

Language:
Python

How to execute program: \
Start server \
`python serv.py <PORT NUMBER>` \
Start Client \
`python cli <server machine> <server port>` 

After client is started, you should see an "ftp" prompt. \
This prompt accepts 4 commands. `get`, `put`, `ls`, and `quit`

Usage:

ftp> `get` <file name> (downloads file <file name> from the server) \
ftp> `put` <filename> (uploads file <file name> to the server) \
ftp> `ls` (lists files on the server) \
ftp> `quit` (disconnects from the server and exits) 

Example: \
python serv.py 1234 \
python cli 127.0.0.1 1234 