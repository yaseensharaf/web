#!/usr/bin/env python

import cgi
import random

# Function to generate a random roll of the dice
def roll_dice(num_dices, max_value):
    return sum([random.randint(1, max_value) for _ in range(num_dices)])

# Create instance of FieldStorage 
form = cgi.FieldStorage()

# Get form input values
num_dices = int(form.getvalue('num_dices'))
max_value = int(form.getvalue('max_value'))
num_tries = int(form.getvalue('num_tries'))

# Check if form input is valid
if num_dices < 1 or num_dices > 10 or max_value < 1 or max_value > 100 or num_tries < 1 or num_tries > 1000:
    error_message = 'Invalid input. Number of dices must be between 1 and 10, largest dice value must be between 1 and 100, and number of tries must be between 1 and 1000.'
else:
    # Roll the dice and find the highest result
    results = [roll_dice(num_dices, max_value) for _ in range(num_tries)]
    highest_result = max(results)

    # Format the results string to display the number of dices, max value, and number of tries
    results_str = f'{num_dices} dice, {max_value} sides, {num_tries} tries: '

    # If there is a tie for the highest result, append all of the tied results to the string
    if results.count(highest_result) > 1:
        tied_results = [i+1 for i in range(len(results)) if results[i] == highest_result]
        results_str += f'Tie between rolls {tied_results} with a value of {highest_result}'
    else:
        results_str += f'Roll {results.index(highest_result) + 1} wins with a value of {highest_result}'

# Print the HTML content
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Dice Rolling Game Results</title>')
print('<style type="text/css">')
print('body { font-family: Arial, sans-serif; }')
print('h1 { text-align: center; margin-top: 50px; }')
print('p { text-align: center; font-size: 24px; margin-top: 50px; }')
print('</style>')
print('</head>')
print('<body>')
print('<h1>Dice Rolling Game Results</h1>')
if 'error_message' in locals():
    print(f'<p class="error-message">{error_message}</p>')
else:
    print(f'<p>{results_str}</p>')
print('</body>')
print('</html>')
