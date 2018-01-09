def divide(num):
    print(100/num)

num2 = int(input("Enter the number to divide 100 with:"))

try:
    divide(num2)

except:
    print("Zero Division is not allowed.")
else:
    print("Divison Successful")

finally:
    divide(100)

