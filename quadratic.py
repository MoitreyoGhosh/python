import cmath

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    
    return root1, root2, discriminant

def describe_roots(root1, root2, discriminant):
    if discriminant > 0:
        print(f"Discriminant: {discriminant} (Two distinct real roots)")
    elif discriminant == 0:
        print(f"Discriminant: {discriminant} (equal real root)")
    else:
        print(f"Discriminant: {discriminant} (Two complex roots)")
    
    print(f"Root 1: {root1}")
    print(f"Root 2: {root2}")

def main():
    print("Quadratic Equation Solver")
    print("Enter coefficients for the quadratic equation ax^2 + bx + c = 0")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    
    if a == 0:
        print("Coefficient a cannot be zero in a quadratic equation.")
        return
    
    root1, root2, discriminant = solve_quadratic(a, b, c)
    
    describe_roots(root1, root2, discriminant)

if __name__ == "__main__":
    main()
