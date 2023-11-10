import random as r

def init_random_list(x):
    for i in range(20):
        x.append(r.randint(10,99))

#find length of ordered elements starting from given position
def get_length_of_ordered_sub_array_starting_from_position (x, position):
    length = 1          #If an array has one element it is always ordered, called trivial
    for i in range(position, len(x)-1):
        if x[i] <= x[i+1]:
           length += 1
        else:
            break
    return length

#This is a very simple but time taking algorithm, it can be made better in terms of time
#We have considered that array is in descending order, therefore the longest length is 1 that is all pairs are unordered
#Therefore, we have taken longest length 1 and considered first elements as sub-array
#Next, we are calling above function to get length of ordered sub array starting from ith position of array
#We compare it with existing longest length and update our longest length and sub-array start and end
def print_longest_ordered_sub_array(x):
    longest_length = 1
    longest_array_start = 0
    longest_array_end = 1
    for i in range(len(x)):           #minimum possible size is 1, if array is sorted in descending order, than first element will be printed by default
        length = get_length_of_ordered_sub_array_starting_from_position(x, i)
        if length > longest_length:
            longest_length = length
            longest_array_start = i
            longest_array_end = i + length
    print(x[longest_array_start:longest_array_end])
    print(f'Longest ordered sub array is starting from {longest_array_start} and ending on {longest_array_end-1}')

def main():
    x=[]
    init_random_list(x)
    print(x)
    print_longest_ordered_sub_array(x)

main()