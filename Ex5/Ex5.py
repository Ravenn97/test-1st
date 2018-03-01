import threading
x = 0
def foo():
	global x
	input_data = int(input("nhap vao 1 so bat ki "))
	for i in range(input_data):
		x += i
	print(x)
	return
if __name__ == '__main__':
	threads = []
	t = threading.Thread(target = foo)
	threads.append(t)
	t.start()