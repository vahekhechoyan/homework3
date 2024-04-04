# harc 1


test_str = "GeeksforGeeks"

all_freq = {}

for i in test_str:
	if i in all_freq:
		all_freq[i] += 1
	else:
		all_freq[i] = 1


print("Count of all characters in GeeksforGeeks is :\n "
	+ str(all_freq))




# harc 2



def uniqueCharacters(str):
	
	
	for i in range(len(str)):
		for j in range(i + 1,len(str)): 
			if(str[i] == str[j]):
				return False;

	
	return True;



str = "GeeksforGeeks";

if(uniqueCharacters(str)):
	print("The String ", str," has all unique characters");
else:
	print("The String ", str, " has duplicate characters");




# harc 3


test_dict = {"Arush": 22, "May": 21, "Hilary": 21}


print("The dictionary before performing remove is : ", test_dict)

del test_dict['May']

print("The dictionary after remove is : ", test_dict)





# harc 4



A = {10, 20, 30, 40, 80}
B = {100, 30, 80, 40, 60}
print (A.difference(B))
print (B.difference(A))



# haec 5

from functools import reduce


test_str = "GeeksforGeeks"
char_to_count = 'e'


count = reduce(lambda acc, c: acc + 1 if c ==
			char_to_count else acc, test_str, 0)


print(f"Count of {char_to_count} in {test_str} is: {count}")



# harc 6





# harc 7

test_dict = {'gfg': 1, 'is': 2, 'best': 3}

if 21 in test_dict.values():
	print(f"Yes, It exists in dictionary")
else:
	print(f"No, It doesn't exist in dictionary")




	
# harc 8
	
A = {3,5,9,8}
B = [4,5,2,1]

result = A.symmetric_difference(B)

print(result)


# harc 9


Dictionary1 = {'A': 'Geeks', 'B': 'For', }
Dictionary2 = {'B': 'Geeks'}


print("Original Dictionary:")
print(Dictionary1)

Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)




# harc 10






# harc 11

mydict = {1: 'Geeks', 2: 'for', 3: 'geeks'}
keysList = list(mydict.keys())
print(keysList)



# harc 12

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7, 8}


size_a = len(set_a)
size_b = len(set_b)


if size_a > size_b:
    print("Set A is larger")
elif size_b > size_a:
    print("Set B is larger")
else:
    print("Both sets are equal in size")
	


# harc 13

    # create a dictionary
data = {'1': 'java', 'tripura': 'python',
		'1': 'statistics', '1': 'cpp'}

# get list of values
list(data.values())

print(data.values())  

# harc 14

dict = {'key1':'geeks', 'key2':'for'} 
print("Current Dict is: ", dict) 


dict1 = {'key3':'geeks', 'key4':'is', 'key5':'fabulous'} 
dict.update(dict1) 


dict.update(newkey1 ='portal') 
print(dict) 

