def main(dict1,keys):
	new_dict = {}
	for i in keys :
		if i in dict1 :
			new_dict[i] = dict1[i]
	return new_dict
