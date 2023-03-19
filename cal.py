#!/usr/bin/env python3
import cgi

# Function to calculate the sum of digits in a number
def digit_sum(n):
    if n < 0:
        return "Error: Please enter a positive integer."
    elif n == 0:
        return "The sum of digits in 0 is 0."
    else:
        # Calculate the sum of digits using a loop
        sum = 0
        for digit in str(n):
            if digit.isdigit():
                sum += int(digit)
        return f"The sum of digits in {n} is {sum}."

# Get user input from form
form = cgi.FieldStorage()
number = form.getvalue("number")

# Generate HTML page
print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Digit Sum Calculator</title>")
print("</head>")
print("<body>")
print("<h1>Digit Sum Calculator</h1>")
print("<form method='post'>")
print("<label for='number'>Enter a positive integer:</label>")
print("<input type='text' id='number' name='number'>")
print("<input type='submit' value='Calculate'>")
print("</form>")

# Calculate and display digit sum if user input is valid
if number:
    try:
        number = int(number)
        print("<p>" + digit_sum(number) + "</p>")
    except ValueError:
        print("<p>Error: Please enter a valid integer.</p>")
        
print("</body>")
print("</html>")
