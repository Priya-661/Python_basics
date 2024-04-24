def c_to_f(c):
    f = (c * 9/5) + 32
    return f

def main():
    c = float(input("Enter the temperature in C: "))
    f = c_to_f(c)
    print("The equivalent temperature in F is:", f)

if __name__ == "__main__":
    main()
