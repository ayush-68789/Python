def main(st):
	maxn = 0 
	for i in st.split() :
		if maxn < len(i) :
			maxn = len(i) 
	return maxn
