def main(key, value ):
	new_dic = dict(zip(key,value))
	return new_dic


# OR .

def main(key, value ):
	res ={}
	if (len(key) <= len(value)):
		length = len(key)
	elif (len(key) >= len(value)):
		length = len(value)
	for i in range(0,length):
		res[key[i]] = value[i]
	return res
