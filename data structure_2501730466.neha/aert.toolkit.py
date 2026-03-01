# =========================================================
# AERT TOOLKIT - DATA STRUCTURES ASSIGNMENT (UNIT-1)
# Name: Neha 
# Roll No: 2501730466
# =========================================================

# ---------------- STACK ADT ----------------
class StackADT:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            return "Stack Empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack Empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# ---------------- FACTORIAL ----------------
def factorial(n):
    if n < 0:
        return "Invalid Input"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# ---------------- FIBONACCI ----------------
naive_calls = 0
memo_calls = 0

def fib_naive(n):
    global naive_calls
    naive_calls += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ---------------- TOWER OF HANOI ----------------
def hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    hanoi(n - 1, auxiliary, source, destination)


# ---------------- BINARY SEARCH ----------------
def binary_search(arr, key, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    elif key < arr[mid]:
        return binary_search(arr, key, low, mid - 1)
    else:
        return binary_search(arr, key, mid + 1, high)


# ---------------- MAIN ----------------
if __name__ == "__main__":

    print("===== FACTORIAL =====")
    for n in [0, 1, 5, 10]:
        print("factorial(", n, ") =", factorial(n))

    print("\n===== FIBONACCI =====")
    for n in [5, 10, 20]:
        naive_calls = 0
        memo_calls = 0
        print("\nFor n =", n)
        print("Naive:", fib_naive(n), " Calls:", naive_calls)
        print("Memo :", fib_memo(n), " Calls:", memo_calls)

    print("\n===== TOWER OF HANOI (N=3) =====")
    hanoi(3, 'A', 'B', 'C')

    print("\n===== BINARY SEARCH =====")
    arr = [1,3,5,7,9,11,13]
    for key in [7,1,13,2]:
        print("Search", key, "->", binary_search(arr, key, 0, len(arr)-1))