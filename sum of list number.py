num = input("List of Number: ")
# NO SPACE AFTER A FUCKING COMMA
str_num = len(num.split(","))
list_num = list(map(int, num.split(",")))
total = 0

print(list_num)

for i in range(0,str_num):
    total += list_num[i]
    
print(total)