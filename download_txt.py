import urllib.request


url = 'https://learnpythonthehardway.org/python3/languages.txt'
filename = 'languages.txt'

urllib.request.urlretrieve(url, filename)
