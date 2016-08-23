################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".

def hello_world():

    print "Hello World"

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.


# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.


# 4. Write a function that takes a string and an integer and
#    prints the string that many times


# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.


################################################################
# PART TWO


# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).
#
#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.
#
#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

# 2. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

# 3. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #2 to construct the full title for the letter's
#    greeting.

# 4. Turn the block of code from the directions into a function.
#    This function will take a number and append it to an existing list
#    called *numbers*. It doesn't need to return anything.
