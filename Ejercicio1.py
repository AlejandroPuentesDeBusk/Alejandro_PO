time = input("What time is it? ")

a,b= time.split(":")

a = float(a)
b = float(b)/100

c= a+b

print(c)