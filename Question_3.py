def dispmsg(name):
    print("Hello",name," Have a good day.")


name = str(input("Enter your name: "))

if name == "":
    raise Exception("INVALID !!! ENTER A VALID NAME")
else:
    dispmsg(name)
