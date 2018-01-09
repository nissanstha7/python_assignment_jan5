def square(num):
    print( num**2)
def cube(num):
    print(num**3)

print("Select (1) for Squaring \n (2) for Cubing")
user=input("Enter your choice: ")

choice = {
    "1": square,
    "2":cube
}
num =int(input("Enter the number:"))

try:
    choice[user](num)

except ValueError:
    print("Enter Valid Integer.")

else:
    print("Valid Operation.")
