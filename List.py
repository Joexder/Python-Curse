demo_lis = [1,"casa", 2.5,[1.5,"bye"]]

# print(demo_lis)

num_list = list((2.5,"chao",45))

r = list(range(-5,100))

#print(r)

colors = ['red', 'yellow', 'blue']

#colors.append(('green','purple'))
colors.extend(['green','purple'])
colors.extend(("brown", "orange"))

colors.insert(2,'black')
print(colors)

#colors.pop(0)
#colors.remove("blue")

colors.sort(reverse=True)
print(colors)
