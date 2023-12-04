First task:
    def determine_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"

    if (player1 == "rock" and player2 == "scissors") or \
       (player1 == "paper" and player2 == "rock") or \
       (player1 == "scissors" and player2 == "paper"):
        return "Player 1 wins."

    if (player2 == "rock" and player1 == "scissors") or \
       (player2 == "paper" and player1 == "rock") or \
       (player2 == "scissors" and player1 == "paper"):
        return "Player 2 wins."

    return "This input is not valid for our game!"

player1_choice = input("Player 1? ").lower()
player2_choice = input("Player 2? ").lower()

print(determine_winner(player1_choice, player2_choice))

Second task:
  
  for i in range(1, 8):
    print('*' * i)

for i in range(6, 0, -1):
    print('*' * i)
    
 Third task:
  a = [2, 2, 3, 1, 1, 1, 1, 3, 2, 2, 6, 5, 4, 7, 8, 31]
b = [2, 7, 4, 6, 7, 4, 2, 31, 2, 5, 11, 1, 2, 1, 3, 1, 7, 9, 5]

common_elements = list(set(a) & set(b))
print(common_elements)
a = [2, 2, 3, 1, 1, 1, 1, 3, 2, 2, 6, 5, 4, 7, 8, 31]
b = [2, 7, 4, 6, 7, 4, 2, 31, 2, 5, 11, 1, 2, 1, 3, 1, 7, 9, 5]

common_elements_one_line = list(set(a) & set(b))
print(common_elements_one_line)

Fourth task:
    def is_palindrome(s):
    s = s.lower()  # Convert the string to lowercase for case-insensitivity
    s = ''.join(c for c in s if c.isalnum())  # Remove non-alphanumeric characters
    return s == s[::-1]

user_input = input("Enter a string: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    
Fifth task:
        
        my_list = [2, 5, 4, 4, 6, 7, 5, 6, 9, 22, 23, 44, 32]
odd_elements = list(filter(lambda x: x % 2 != 0, my_list))
print (odd_elements)
        
