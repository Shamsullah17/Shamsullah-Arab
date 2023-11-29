def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    start = int(input("Enter the starting positive integer: "))
    end = int(input("Enter the ending positive integer: "))

    prime_numbers = find_primes(start, end)

    print("Prime numbers between", start, "and", end, "are:", prime_numbers)

    if prime_numbers:
        average = sum(prime_numbers) / len(prime_numbers)
        print("Average of prime numbers:", average)
    else:
        print("No prime numbers found in the given range.")


def main():
    N = int(input("Enter a positive integer N: "))

    result = N * 2 if N % 2 != 0 else N * 3

    print("Result:", result)

def rotate_array(arr, direction, d):
    n = len(arr)

    if direction == 'left':
        rotated_array = arr[d % n:] + arr[:d % n]
    elif direction == 'right':
        rotated_array = arr[-d % n:] + arr[:-d % n]
    else:
        return "Invalid direction. Please choose 'left' or 'right'."

    return rotated_array

def main():
    array = [1, 2, 3, 4, 5, 6, 7]

    direction = input("Enter the rotation direction ('left' or 'right'): ")
    d = int(input("Enter the number of elements to rotate: "))

    result = rotate_array(array, direction, d)

    print("Original Array:", array)
    print(f"After {direction} rotation by {d} elements:", result)
def shift_2d_array(matrix, shift_type, direction, index, d):
    rows, cols = len(matrix), len(matrix[0])

    if shift_type == 'row':
        if direction == 'left':
            matrix[index] = matrix[index][d % cols:] + matrix[index][:d % cols]
        elif direction == 'right':
            matrix[index] = matrix[index][-d % cols:] + matrix[index][:-d % cols]
        else:
            return "Invalid direction for row shift. Please choose 'left' or 'right'."
    elif shift_type == 'column':
        column = [matrix[i][index] for i in range(rows)]
        if direction == 'top':
            column = column[d % rows:] + column[:d % rows]
        elif direction == 'down':
            column = column[-d % rows:] + column[:-d % rows]
        else:
            return "Invalid direction for column shift. Please choose 'top' or 'down'."
        for i in range(rows):
            matrix[i][index] = column[i]
    else:
        return "Invalid shift type. Please choose 'row' or 'column'."

    return matrix