import bs4 as bs 
import random, requests, string
from multiprocessing import Pool 

letters = list(string.ascii_lowercase)
random.shuffle(letters)
def random_starting_url():
	# three random lowercase characters
	starting = ''.join((random.choice(letters) for i in range(3)))
	url = ''.join(['http://', starting, '.com'])
	return url


def handle_local_links(url, link):
	if link.startswith('/'):
		return ''.join([url, link])
	else:
		return link


def get_links(url):
	try:
		resp = requests.get(url)
		soup = bs.BeautifulSoup(resp.text, 'lxml')
		body = soup.body
		links = [link.get('href') for link in body.find_all('a')]
		links = [handle_local_links(url, link) for link in links]
		links = [str(link.encode("ascii")) for link in links]
		return links

	except TypeError as e:
		print(e)
		print('Received a TypeError, most likely a None that we then tried to iterate over.')
	except IndexError as e:
		print(e)
		print('Probably we did not find any useful links, returning empty list.')
		return []
	except AttributeError as e:
		print(e)
		print('Likely received None for links, so need to throw this.')
	except Exception as e:
		print(str(e))
		return []


url = random_starting_url()
print(url)

def main():
	how_many = 50
	p = Pool(processes=how_many)
	parse_us = [random_starting_url() for _ in range(how_many)]	
	data = p.map(get_links, [link for link in parse_us])
	data = [url for url_list in data for url in url_list] # taking a list of lists, and making a single list with all of the elements
	p.close()

	with open('urls.txt', 'w') as f:
		f.write(str(data))

if __name__ == "__main__":
	main()
