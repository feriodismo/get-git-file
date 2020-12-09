import urllib.request as req
import sys

path = sys.argv[1].replace('https://github.com/', 'https://raw.githubusercontent.com/')
path = path.replace('/blob/master/', '/master/')
name = path.split('/')[-1]

url = req.urlopen(path).read().decode('utf-8')
file = open(name, 'w')
file.write(url)
file.close()
print('Your file have download from github, thank you for using me!')