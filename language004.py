# coding: utf-8
str1 = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

str1 = str1.replace(".","")
arystr = str1.split(" ")

list = []

i = 0
dict = {}
for word in arystr:
    if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
        dict[word[:1]] = i
    else:
        dict[word[:2]] = i
    i+=1
print(dict.items())

for k, v in sorted(dict.items(), key=lambda x:x[1]):
    print k, v

# str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# str = str.split()
#
# dict = {}
# single = [1, 5, 6, 7, 8, 9, 15, 16, 19]
#
# for element in str:
#     if str.index(element) + 1 in single:
#         dict[element[:1]] = str.index(element) + 1
#     else:
#         dict[element[:2]] = str.index(element) + 1
#
# # 原子番号順にソートして print（蛇足）
# for k, v in sorted(dict.items(), key=lambda x:x[1]):
#     print k, v
