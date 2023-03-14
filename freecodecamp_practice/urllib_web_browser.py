import urllib.request, urllib.parse, urllib.error

my_handler = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') # Handles the connection, the call, the encoding and everything around for you.
for line in my_handler: # You can just go through every line 
    print(line.decode().strip()) # Just make sure you decode the data and strip it to get rid of the extra \n

print("\nRead web-pages:")
# We readed a document, but we could read a web-page

my_handler = urllib.request.urlopen('http://data.pr4e.org/page1.htm')
for line in my_handler: 
    print(line.decode().strip()) 
