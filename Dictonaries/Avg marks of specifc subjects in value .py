def main(dict1):
	n = len(dict1)
	sub1 = 0 
	sub2 = 0 
	sub3 = 0
	for marks in dict1.values() :
		sub1 += marks[0]
		sub2 += marks[1]
		sub3 += marks[2]

	avg1 = round(sub1/n , 2)
	avg2 = round(sub2/n , 2)
	avg3 = round(sub3/n, 2)

	return [avg1,avg2,avg3]
