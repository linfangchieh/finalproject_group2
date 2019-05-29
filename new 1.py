import ssl
import urllib.request
context = ssl._create_unverified_context()
urllib.request.urlopen("https://www.google.com/", context=context).read()