import random

def is_exist(my_list, element, index):
	for i in range(0, index + 1):
		if my_list[i] == element:
			return True
	return False

def init_unique_random(my_list):
	for i in range(20):
		while True:
			value = random.randint(10,99)
			if is_exist(my_list, value, i-1) == False:
				break	# Terminate the loop, if element already exist in the list
		my_list.append(value)

def copy_and_shuffle_list(old_list, new_list):
	for i in range(len(old_list)):
		new_list.append(old_list[i])
	for i in range(100):
		index1 = random.randint(0, len(old_list)-1)
		index2 = random.randint(0, len(old_list)-1)
		temp = new_list[index1]
		new_list[index1] = new_list[index2]
		new_list[index2] = temp

def match_and_print(old_list, new_list):
	for i in range(len(old_list)):
		for j in range(len(old_list)):
			if old_list[i] == new_list[j]:
				print (f'{old_list[i]} exists at index {j} in second list')

def largest_distant_element(old_list, new_list):
	max_distance = 0
	for i in range(len(old_list)):
		for j in range(len(old_list)):
			if old_list[i] == new_list[j]:
				distance = abs(j-i)
				if distance > max_distance:
					max_distance = distance
	print (f'Maximum distance between two elements is: {max_distance}')

def main():
	x = []
	init_unique_random(x)
	print(x)
	y = []
	copy_and_shuffle_list(x, y)
	print(y)
	match_and_print(x, y)
	largest_distant_element(x, y)
main()
