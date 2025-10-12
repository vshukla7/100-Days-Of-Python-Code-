import utils.session
questions = [["What is the capital city of India?", ["Mumbai", "New Delhi", "Kolkata", "Chennai"], 10, 2],
            ["What is the capital city of France?", ["Paris", "London", "Berlin", "Madrid"], 20, 1],
            ["What is the old name of Patna?", ["Patliputra", "Patna", "London", "Madras"], 50, 1],
            ["What is the position of india world wide in area?", ["7th", "1st", "2ed", "4th"], 100, 1], 
            ["What is the position of india world wide in population?", ["1st", "2ed", "3rd", "7th"], 1000, 1], 
            ["how many states are there in india?", ["28", "29", "30", "31"], 10000, 1],
            ["how many union territories are there in india?", ["7", "8", "9", "10"], 100000, 3],
            ["why is india called the land of festivals?", ["because of its festivals", "because of its culture", "because of its people", "because of its food"], 1000000, 2],
            ["what is the national animal of india?", ["tiger", "lion", "elephant", "deer"], 10000000, 1]]

# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'
BOLD = '\033[1m'
print(CYAN + BOLD + "Welcome to KBC".center(50, "*") + RESET)
print(YELLOW + "You have to answer 10 questions to win the game\n One wrong answer will end the game" + RESET)

winnings = 0

for i in range(len(questions)):
  print(BLUE + BOLD + f"Question {i+1}: {questions[i][0]}" + RESET)
  for j in range(len(questions[i][1])):
    print(WHITE + f"{j+1}. {questions[i][1][j]}" + RESET)  
  answer = int(input(CYAN + "Enter your answer 1/2/3/4: " + RESET))
  if answer == questions[i][3]:
    print(GREEN + BOLD + "✓ Correct answer!" + RESET)
    winnings = questions[i][2]
    print(MAGENTA + f"Congratulations! You have won {winnings} rupees" + RESET)
  else:
    print(RED + BOLD + "✗ Wrong answer!" + RESET)
    winnings = 0
    print(RED + f"Sorry! Game over. You won {winnings} rupees" + RESET)
    break
    
if winnings != 0:
  print(GREEN + BOLD + "🎉 CONGRATULATIONS! 🎉" + RESET)
  print(MAGENTA + BOLD + f"Thank you for playing! You won {winnings} rupees" + RESET)
else:
  print(YELLOW + "Better luck next time!" + RESET)