import threading

counter = 0

def worker(start,end):
    global counter
    for i in range(start, end):
        counter += i

if __name__ == "__main__":
    start = 1
    input_data = int(input("nhap vao 1 so "))
    number = int(input_data / 2)
    threads = [threading.Thread(target = worker,args = (1, number)), threading.Thread(target = worker,args = (number, input_data))]
    for thread in threads:
        thread.setDaemon(True)
        thread.start()
    for thread in threads:
        thread.join()

    print (counter)
