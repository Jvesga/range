# caso 1
for i in range(10):
    print(i)

# caso 2 
for i in range(1, 11):
    print(i)

# caso 3
for i in range(1, 11):
    print("Ing. sistemas, la mejor")

# caso 4
for i in range(10):
    print(" i = " + str(i))

# caso 5
for i in range(10):
    print(f"i = {i}")

# caso 6
for i in range(-8, -13, -1):
    print(f"i = {i}")

# caso 7
nombre = input("Digite su nombre: ")
c_a = 0
c_e = 0
c_i = 0
c_o = 0
c_u = 0

for letra in nombre:
    if letra == "a":
        c_a += 1
    elif letra == "e":
        c_e += 1
    elif letra == "i":
        c_i += 1
    elif letra == "o":
        c_o += 1
    elif letra == "u":
        c_u += 1
    
print(f"El nombre tiene {c_a} vocales a ")
print(f"El nombre tiene {c_e} vocales e ")
print(f"El nombre tiene {c_i} vocales i ")
print(f"El nombre tiene {c_o} vocales o ")
print(f"El nombre tiene {c_u} vocales u ")
