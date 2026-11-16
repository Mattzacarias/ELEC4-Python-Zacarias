"""
Full Name: [Your Full Name]
Section: [IV-BSIT A/B/C]
Activity Code: P6 - Recursion Toolkit
Date: December 2026
"""

# 1. Factorial
# Base case: kapag n == 0 o n == 1, ibabalik ang 1.
# Recursive call: n * factorial(n - 1)
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 2. Fibonacci
# Base case: kapag n == 0 ibabalik ang 0; kapag n == 1 ibabalik ang 1.
# Recursive call: fibonacci(n - 1) + fibonacci(n - 2)
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Helper recursive function para ipakita ang unang n terms nang walang loop
def print_fib_sequence(n, current=0):
    if current >= n:
        return
    print(fibonacci(current), end=" ")
    print_fib_sequence(n, current + 1)

# 3. Sum of Numbers (1 hanggang n)
# Base case: kapag n <= 1, ibabalik ang n.
# Recursive call: n + sum_numbers(n - 1)
def sum_numbers(n):
    if n <= 1:
        return n
    return n + sum_numbers(n - 1)

# 4. Recursive Search sa List
# Base case: kapag walang laman ang list (False) o kapag items[0] == target (True).
# Recursive call: search(items[1:], target)
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)

def main():
    while True:
        print("\n--- RECURSION TOOLKIT ---")
        print("1. Factorial (n!)")
        print("2. Fibonacci Sequence")
        print("3. Sum of Numbers (1 to n)")
        print("4. Recursive List Search")
        print("5. Exit")
        choice = input("Pumili (1-5): ").strip()

        if choice == "1":
            n = int(input("Ilagay ang non-negative integer n: "))
            print(f"{n}! = {factorial(n)}")
        elif choice == "2":
            n = int(input("Ilang terms ng Fibonacci ang ipapakita? "))
            print(f"Unang {n} terms: ", end="")
            print_fib_sequence(n)
            print(f"\nNth Fibonacci number (index {n}): {fibonacci(n)}")
        elif choice == "3":
            n = int(input("Ilagay ang positive integer n: "))
            print(f"Sum mula 1 hanggang {n} = {sum_numbers(n)}")
        elif choice == "4":
            sample_list = ["apple", "banana", "mango", "orange"]
            print(f"Listahan: {sample_list}")
            target = input("Ilagay ang hahanaping item: ").strip()
            found = search(sample_list, target)
            print(f"Nahanap ba ang '{target}'? {found}")
        elif choice == "5":
            print("Salamat! Paalam.")
            break
        else:
            print("Maling pili. Subukan ulit.")

if __name__ == "__main__":
    main()
