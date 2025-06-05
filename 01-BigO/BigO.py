# print('hello world')
# this is O(n) - number of operations. O- operations. n - number.


# O(n)
def print_items(n):
    for i in range(n):
        print(i)

print_items(10)

# O(2n) - So this constant can be dropped and called as O(n)
def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)

# O(n^2) - for nested for loop

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print_items(10)


# O(n^2 + n) - Drop non-dominants, so it's O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)

print_items(10)


# O(1) - constant time
# O(n) - linear time
# O(n^2) - quadratic time 
# O(n^3) - cubic time
# O(2^n) - exponential time
