# r - read only
# w - write only
# a - append
# x - create 


# file = open(r"E:\Projects\python_aug26\date_time.py", mode="r")
# print(file.read(5))
# print(file.readlines()[2])
# file.close()


# with open(r"E:\Projects\python_aug26\date_time.py") as file:
#     print(file.read(5))
    
    
# with open("file.txt", mode="w") as file:
#     file.write("Hello student\nHello Uncle")


file = open(r"president_height.csv")
data = file.readlines()
data.pop(0)

names = []
heights = []
for each in data:
   names.append(each.split(',')[1])
   height = each.split(',')[2]
   height = height.strip("\n")
   heights.append(int(height))
   
# print(names)
# print(heights)

maxi = max(heights)
mini = min(heights)

# print(heights.index(maxi))

# x=0
# for each in heights:
#     if each == mini:
#         print(names[x])
    
#     x+=1

# print(sum(heights)/len(heights))

import statistics as st

# print(st.mean(heights))
print(st.mode(heights))