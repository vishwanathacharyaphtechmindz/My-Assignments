a = 0 
b = 1
data = 0
print("Fibonocci series are :-")
while data < 10:
    print(a)
    c = a + b
    a = b
    b = c
    data += 1