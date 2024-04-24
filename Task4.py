def c_to_f(c):
    f = (c * 9/5) + 32
    return f

c = float(input("Enter temperature in C: "))
f = c_to_f(c)
print("Equivalent temperature in F:", f)
