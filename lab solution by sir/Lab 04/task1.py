import random

def init_random(my_list):
	for i in range(20):
		my_list.append(random.randint(1,9))

def copy(old_list, new_list):
	for i in range(20):
		new_list.append(old_list[i])

def count_and_print_each_element(a):
	for i in range(len(a)):
		if a[i] != 0:
			count =1
			for j in range(i+1, len(a)):
				if a[i] == a[j]:
					count += 1
					a[j] = 0
			print (f'{a[i]},  exists {count} times in the list')

def count_and_copy_elements_and_counts(new_list, old_list, fresh_list, counts):
	for i in range(len(new_list)):
		if new_list[i] != 0:
			count = 0
			for j in range(len(old_list)):
				if new_list[i] == old_list[j]:
					count += 1
			fresh_list.append(old_list[i])
			counts.append(count)

def print_elements_count_times(mylist, counts):
	s = ""
	for i in range(len(mylist)):
		for j in range(counts[i]):
			s = s + str(mylist[i]) + " "
	print(s)

def main():
	x = []
	init_random(x)
	print(x)
	y = []
	copy(x, y)
	count_and_print_each_element(y)
	elements = []
	counts = []
	count_and_copy_elements_and_counts(y, x, elements, counts)
	print (elements)
	print(counts)
	print_elements_count_times(elements, counts)

main()
