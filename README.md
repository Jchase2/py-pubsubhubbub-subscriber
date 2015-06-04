# py-pubsubhubbub-subscriber

# About
Very basic unfinished python subscriber with a python http.server
implementation. This is unfinished because the YouTube Data API is 
broken and so what I was going to use it for won't work until they
fix their service. 

See: 

https://code.google.com/p/gdata-issues/issues/detail?id=7138 and

https://code.google.com/p/gdata-issues/issues/detail?id=5602


Maybe someone else can get some use out of it... It's a very rough draft. 

# How-TO

Create a directory where server.py will be stored, and inside of that
another directory where the web-facing fffp.py script will be stored. 
Edit server.py such that the cgi_directories line points to the directory
with fffp.py.

Change the variables at the top of fffp.py to reflect your needs.
Also check the shebang line (the first line in the file) to make 
sure it reflects the actual location of your python installation. 
Also, make sure you have requests installed in python. Easily done with 

    pip install requests
    

Run server.py, then navigate to your "callback" url, which is just the url of the fffp.py script.

Check output in terminal and on the page...  

This was written with python 3, wasn't tested with 2. It's not a finished
product at all. 
