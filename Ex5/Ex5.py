import threading
x = 0
input_data = int(input("nhap vao 1 so bat ki "))

def foo():
	global x
	for i in range(input_data-1):
		x += i
	return

def foo2():
	for i in range(input_data - 1, input_data +1):
		x += i
	return
if __name__ == '__main__':
	threads = []
	threads = [threading.Thread(target=foo), threading.Thread(target=foo2)]
	for t in threads:
		t.daemon = True
		t.start()
	for t in threads:
		t.join()
	print (x)