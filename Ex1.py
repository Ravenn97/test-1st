'''in ra day fibonacci nho hon so nguoi dung nhap vao'''
def print_fibonacci(input_number):
	a, b = 0, 1
	while b <= input_number: #loop chay trong range cua input_number
		print (b)
		a, b = b, a + b #moi so trong day fibo thi bang tong 2 so ke truoc
	return 

if __name__ == '__main__':
	input_number = int(input("nhap vao 1 so bat ki: ")) #nhap tu ban phim 1 so bat ki
	print_fibonacci(input_number)
