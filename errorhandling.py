# 1. runtime error 
# items = ['banana', 'pepper']
# print(items[5])

# amount = float(input("Amount: "))
# print(amount)



# 2. compile time error 
# print(name)


# try, except , else, and finally

try:
    items = ['banana', 'pepper']
    # print(items[0])
    
    # print(name)
    
# except IndexError as i:
#     print("Error: ", i)
    
# except NameError as n:
#     print("Error: ", n)

except Exception as e:
    print("Error: ", e)
    
    
    
try:
    val1 = float(input("value 1: "))
    val2 = float(input("value 2: "))

    ans = val1/val2
except Exception as e:
    print("Error:", e)    
    
else: # works if no error occurs
    print("ans:", ans)
    
finally: # works if an error occurs or not
    print("Thank you for banking with us")
    