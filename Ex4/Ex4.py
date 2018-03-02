import requests
from bs4 import BeautifulSoup

def write_file(input_data):

	r = requests.get(input_data) #lay du lieu tu link
	data = r.text 
	soup = BeautifulSoup(data, "html.parser") # chuyen text nhan duoc sang dinh dang html
	file = open("conten.txt","w")
	for node in soup.find_all('p'):
		file.write(node.find_all(text = True)[0])
	file.close()
	return
if __name__ == '__main__':
	input_data = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
	write_file(input_data)

