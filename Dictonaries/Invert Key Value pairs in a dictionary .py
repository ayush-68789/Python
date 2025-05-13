def main(dict1):
	new_dict = {}
	for key,value in dict1.items() : 
		new_dict[value] = key
	return new_dict
