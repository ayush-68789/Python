st = input()
caps = []
for i in st.split() :
    caps.append(i.capitalize())
res = ' '.join(caps)
print(res)
