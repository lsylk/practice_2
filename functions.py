################################################################
# PART ONE


# 1. Write a function that does not take any arguments and
#    prints "Hello World".


def hello_world():
    """Print Hello World.

        >>> hello_world()
        Hello World!
    """

    print "Hello World!"

# 2. Write a function that takes a name as a string and
#    prints "Hi" followed by the name.


def greet_user(name):
    """Greets the user.

        >>> greet_user("Karen")
        Hi Karen!

        >>> name = "Jordan"
        >>> greet_user(name)
        Hi Jordan!
    """

    print "Hi %s!" % name

# 3. Write a function that takes two integers and multiplies
#    them together. Print the result.


def multiplication(num1, num2):
    """Type casts num1 and num2 into integers, and multiplies num1 and num2.

        >>> multiplication(8,39)
        312

        >>> multiplication("5",39)
        195

        >>> multiplication(8,"0")
        0

        >>> multiplication("8",-9)
        -72
    """

    print int(num1) * int(num2)

# 4. Write a function that takes a string and an integer and
#    prints the string that many times


def print_string_n_times(string, n):
    """Prints the string n times.

        >>> print_string_n_times("apples", 5)
        applesapplesapplesapplesapples

        >>> print_string_n_times("a-b-", 3)
        a-b-a-b-a-b-

        >>> print_string_n_times(81, 3)
        818181
    """

    print str(string) * n

# 5. Write a function that takes an integer and prints "Higher
#    than 0" if higher than zero and "Lower than 0" if lower
#    than zero. If the integer is 0 print "Zero".


def compare_num_to_zero(num):
    """Type casts num into a int, then assess if the num is higher, less or equal to zero.

        >>> compare_num_to_zero(89)
        Higher than zero

        >>> compare_num_to_zero(-8)
        Less than zero

        >>> compare_num_to_zero(0)
        Zero

        >>> compare_num_to_zero("56")
        Higher than zero
    """

    num = int(num)

    if num > 0:

        print "Higher than zero"

    elif num < 0:

        print "Less than zero"

    else:
        print "Zero"


# 6. Write a function that takes an integer and returns a
#    boolean (True or False), depending on whether the number
#    is evenly divisible by 3.


def divisible_by_three(num):
    """Type casts num into integer. Checks if num is divisible by 3.

        >>> divisible_by_three(9)
        True

        >>> divisible_by_three(89)
        False

        >>> divisible_by_three("27")
        True
    """

    num = int(num)

    if num % 3 == 0:

        return True

    else:

        return False

# 7. Write a function that takes a sentence as one string and
#    returns the number of spaces.


def count_spaces(sentence):
    """Counts the spaces that the sentece has.

        >>> count_spaces("The sky is blue, the roses are red, what color is the moon?")
        12

        >>> count_spaces("Say Che ee ee ee se!")
        5
    """

    count = 0

    for char in sentence:

        if char == " ":

            count += 1

    return count


# 8. Write a function that can be passed a meal price and a
#    tip percentage. It should return the total amount paid
#    (price + price * tip). **However:** passing in the tip
#    percentage should be optional; if not given, it should
#    default to 15%.

def total_paid(meal_price, tip=0.15):
    """Calculates the total price of the meal including tip.

        >>> total_paid(8)
        9.2

        >>> total_paid(19, 0.15)
        21.85
    """

    return meal_price + (meal_price * tip)


# 9. Write a function that takes an integer as an argument and
#    returns two pieces of information as strings ---
#    "Positive" or "Negative" and "Even" or "Odd". The two strings
#    should be returned in a list.
#
#    Then, write code that shows the calling of this function
#    on a number and unpack what is returned into two
#    variables --- sign and parity (whether it's even or odd).
#    Print sign and parity.

def int_description(num):
    """Assess if the num is positive, negative, even and/or odd.

        >>> int_description(56)
        ['Positive', 'Even']

        >>> sign, parity = int_description(56)

        >>> print sign
        Positive

        >>> print parity
        Even

        >>> sign, parity = int_description(-3)

        >>> print parity
        Odd

        >>> print sign
        Negative
    """

    if num >= 0:

        sign = "Positive"

    else:

        sign = "Negative"

    if num % 2 == 0:

        parity = "Even"

    else:

        parity = "Odd"

    return [sign, parity]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Code below unpacks the what is returned from int_description function.

    # sign, parity = int_description(num)

    # print sign

    # print parity


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

def total_cost(price, state, tax=0.05):
    """Calculates the total price of an item including tax. It will apply 5%  for tax, except for CA which is 7%.

        >>> total_cost(15, "MI")
        15.75

        >>> total_cost(15, "CA")
        16.05

        >>> total_cost(18, "cA")
        19.26
    """

    if state.upper() == "CA":

        tax = 0.07

    return price + (price * tax)


# 2. Turn the block of code from the directions into a function.
#    Take a name and a job title as parameters, making it so the
#    job title defaults to "Engineer" if a job title is not passed in.
#    Return the person's title and name in one string.

def person_title(name, job_title="Engineer"):
    """Returns the name of the person and his/her title.

        >>> person_title("Jane")
        'ENGINEER JANE'

        >> person_title("Jack", "Pilot")
        'PILOT JACK'
    """

    return "%s %s" % (job_title.upper(), name.upper())


# 3. Given a recipient name & job title and a sender name,
#    print the following letter:
#
#       Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
#       Sincerely, SENDER_NAME.
#
#    Use the function from #2 to construct the full title for the letter's
#    greeting.

def print_letter(recipient_name, sender_name, job_title="Engineer"):

    """Prints the following letter:

        Dear JOB_TITLE RECIPIENT_NAME, I think you are amazing!
        Sincerely, SENDER_NAME.

            >>> print_letter("Jordan", "Megan", "Lawyer")
            Dear LAWYER JORDAN, I think you are amazing! 
             Sincerely, MEGAN.

            >>> print_letter("Jane", "Annie")
            Dear ENGINEER JANE, I think you are amazing! 
             Sincerely, ANNIE.
    """

    print "Dear " + person_title(recipient_name, job_title) + ", I think you are amazing! \n Sincerely, %s." % sender_name.upper()


# 4. Turn the block of code from the directions into a function.
#    This function will take a number and append it to an existing list
#    called *numbers*. It doesn't need to return anything.

def add_num_to_list(num):
    """Adds a number to the numbers list and returns None.

    >>> add_num_to_list(8)
    >>> add_num_to_list(9)

    >>> type(add_num_to_list(9))
    <type 'NoneType'>
    """

    numbers = []

    numbers.append(num)

    return

#####################################################################
# Test all functions.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED!"
    print
