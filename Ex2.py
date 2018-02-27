'''read and write file'''

def read_file():
	count = {} #tao 1 dict rong
	file = open("input.txt", "r") #mo file input voi mode read file
	data = file.read()
	for word in data.split(): #tach chuoi string thanh list cac tu cach nhau boi dau cach
		count.setdefault(word, 0) # set value mac dinh cua cac key la word trong dict count = 0 
		count[word] += 1 #voi moi lan xuat hien cua word trong count thi value cua key word tu dong cong them 1
	file.close()
	return count

def write_file():
	file = open("output.txt","w")
	file.write(str(read_file())) #ep kieu count tu dict() sang string() sau do ghi vao file output.txt
	file.close() 

if __name__ == '__main__':
	write_file()
