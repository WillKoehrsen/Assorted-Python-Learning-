import urllib.request
import urllib.parse
import re

url = 'https://pythonprogramming.net/search/'
values = {'q':'basics'}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()


paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))

for each in paragraphs:
	print(each)