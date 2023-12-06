Task 1:
    
def longest_substring_length(my_str):
    char_index = {}  
    max_length = 0
    start_index = 0

    for i, char in enumerate(my_str):
        if char in char_index and char_index[char] >= start_index:
            start_index = char_index[char] + 1

        char_index[char] = i
        current_length = i - start_index + 1
        max_length = max(max_length, current_length)

    return max_length

Task 2:
    
    def reverse_digits(number):
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return reversed_number

# Example usage:
number = 6842
result = reverse_digits(number)
print(result)

Task 3:

def first_missing_positive(numbers):
    i = 0
    n = len(numbers)

    while i < n:
        if 1 <= numbers[i] <= n and numbers[numbers[i] - 1] != numbers[i]:
            # Swap the numbers to their correct positions
            numbers[numbers[i] - 1], numbers[i] = numbers[i], numbers[numbers[i] - 1]
        else:
            i += 1

    for i in range(n):
        if numbers[i] != i + 1:
            return i + 1

    return n + 1

# Example usage:
numbers1 = [1, 2, 4, 6, 5, 0]
result1 = first_missing_positive(numbers1)
print(result1)

numbers2 = [3, 4, -1, 1]
result2 = first_missing_positive(numbers2)
print(result2)

Task 4:
 def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        current_interval = intervals[i]
        last_merged = merged[-1]

        if current_interval[0] <= last_merged[1]:
            # Merge overlapping intervals
            last_merged[1] = max(last_merged[1], current_interval[1])
        else:
            # Add non-overlapping interval to the result
            merged.append(current_interval)

    return merged

# Example usage:
intervals1 = [[1, 4], [3, 6], [9, 11], [14, 19]]
result1 = merge_intervals(intervals1)
print(result1)

intervals2 = [[1, 4], [3, 4], [4, 5]]
result2 = merge_intervals(intervals2)
print(result2)

Task 5:
def calculate_grade(homework, exam):
    total_grade = (homework + exam) / 10
    return total_grade

def determine_result(grade):
    if grade >= 8:
        return "Excellent"
    elif grade >= 6:
        return "Good"
    elif grade >= 4:
        return "Acceptable"
    else:
        return "Failed"

students = {
    'A1': {'homework': 15, 'exam': 68},
    'A2': {'homework': 7, 'exam': 18},
    'A3': {'homework': 14, 'exam': 48},
    'A4': {'homework': 20, 'exam': 40}
}

for reg_num, scores in students.items():
    homework_score = scores['homework']
    exam_score = scores['exam']
    
    total_grade = calculate_grade(homework_score, exam_score)
    result = determine_result(total_grade)
    
    if result == 'Failed':
        print(f"The student with registration number {reg_num} has failed.")
    else:
        print(f"The student with registration number {reg_num} has passed, with final grade {result}.")

