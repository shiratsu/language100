# coding: utf-8
str1 = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
str2 = str1.replace(","," ")
arystr = str1.split(" ")

list = []

for word in arystr:
	list.append(len(word))

print(list)
