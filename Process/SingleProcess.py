#! /usr/bin/python
from threading import Thread
import time
def my_counter():
	i = 0
	for _ in range(100000000):
		i = i + 1
	return True
def main():
	thread_array = {}
	start_time = time.time()
	for tid in range(1):
		t = Thread(target=my_counter)
		t.start()
		thread_array[0] = t
	for tid in range(1):
		t = Thread(target=my_counter)
		t.start()
		thread_array[1] = t
	for i in range(2):
		thread_array[i].join()
	end_time = time.time()
	print("Total time: {}".format(end_time - start_time))
if __name__ == '__main__':
	main()
