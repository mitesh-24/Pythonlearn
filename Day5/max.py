number_list = input("Enter the numbers : ").split()
for n in range(0,len(number_list)):
    number_list[n] = int(number_list[n])
print(number_list)

highest_num = 0
for num in number_list:
    if num > highest_num:
        highest_num = num

print(highest_num)