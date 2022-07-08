
heights = input("Enter a list of heights\n").split()
for n in range (0,len(heights)):
    heights[n] = int(heights[n])

# to calculate the sum of heights
total_height = 0
for height in heights:
    total_height += height
# print(total_height)

# to calculate no. of items
total = 0
for height in heights:
    total += 1
# print(total)

average = total_height/total
navg=round(average)
print(f"Average of all the heights is {navg}")