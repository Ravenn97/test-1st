import requests
from bs4 import BeautifulSoup

def get_string():
	r = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	input_data = soup.get_text()
	return input_data

def write_file():
	file = open("conten.txt","w")
	file.write(get_string())
	file.close()
	return

if __name__ == '__main__':
	write_file()

