from cs110 import expect, summarize
from typing import List

"""
# Midterm 1 General instructions

Welcome to the CPSC 110 Midterm. We are testing the first half of
CPSC 110, with the last topic being data design, including classes.

1. For all questions, interpret to the best of your ability and write down any
assumptions you make.

2. Answer all questions except 3.1 in this file.

3. The exam is closed book except for your paper cheat sheet. Using any other
program or source will be grounds for immediate failure.

4. ONLY when instructed, you may open Canvas to submit this file.

5. If you need to use the washroom, raise your hand, demonstrate that your
phone is left on your desk, and take nothing with you.

6. The only questions that can be answered are having to do with serious
technical failures. Otherwise, you are required to simply write your interpretation.

7. Your code must run for full marks, but write down anything you can for part
marks if you are unable to get it to run.

Good luck!

"""

"""
-------------------------------------------------------------------------
# 1. Design a Simple Function

This question is testing your ability to use the HtDF recipe to
solve a simple problem. You will be graded on using the whole HtDF
formula correctly, including using correct typing, spacing and style.

Design a function called `nextNumber` that takes a whole number and
produces the next whole number. Write exactly one example and test case.
You do not need to include `summarize()` but you are welcome to use it.
-------------------------------------------------------------------------
"""

"""
-------------------------------------------------------------------------
# 2. Design the Signature, Purpose, and Examples

This question is testing your ability to choose the appropriate
collections (i.e., iterable data types) for a given problem. 

Choose the **best** collection and give the signature, purpose,
and at least one example for each given purpose statement.
You should copy the purpose statement to your solution.
-------------------------------------------------------------------------
"""

"""
-------------------------------------------------------------------------
2.1.
Purpose: Finds the index of a number that is closest
to the average of a collection of numbers.
-------------------------------------------------------------------------
"""

"""
-------------------------------------------------------------------------
2.2.
Purpose: Takes a start and end index and produces a
collection of all whole numbers between the indices.
-------------------------------------------------------------------------
"""

"""
-------------------------------------------------------------------------
2.3. 
Purpose: Takes an element and adds it to a collection of elements
only if the element doesn't already exist in the collection.
-------------------------------------------------------------------------
"""

"""
-------------------------------------------------------------------------
2.4.
Purpose: Takes a collection, a key, and a value and produces the a
modified collection where the key is associated with a value.
-------------------------------------------------------------------------
"""

"""
-------------------------------------------------------------------------
2.5.
Purpose: Takes two numbers and produces an
immutable collection of the two numbers.
-------------------------------------------------------------------------
"""

"""
-------------------------------------------------------------------------
# 3. Read an Accumulator pattern

This question is testing your ability to understand the point
of a function by tracking its execution.

Given the following function:
(1) Draw the workflow execution on the provided piece of paper
(2) Explain in plain English what it does in this file.
(3) Construct three example cases to illustrate your explanation.
-------------------------------------------------------------------------
"""

def fn_for_lon(lon: List[int | float]) -> int | float:
    acc = dict()
    for n in lon:
        if n in acc:
            acc[n] = acc[n] + 1
        else:
            acc[n] = 1

    maximum = lon[0]
    for n in acc:
        if acc[n] > maximum:
            maximum = n
    return maximum


"""
-------------------------------------------------------------------------
# 4. Using Classes for Data Design
This question is testing your ability to design
a class given a real-world problem. 

Imagine that you have been hired to design a database for
a local restaurant chain like Milestone's. They are interested
in the following data about their customers:

- The customer's birthday year
- The customer's birthday month
- The customer's birthday day
- The customer's name
- The customer's email address
- Menu items that they have bought
- Counts of the menu items that they have bought

Design a single `Customer` class that represents the data given above.
-------------------------------------------------------------------------
"""







"""
-------------------------------------------------------------------------
# 5. HtDW: Using HtDF for Classes

These questions are testing your ability to design functions for classes.
Use the HtDF formula for each function you design.
-------------------------------------------------------------------------
"""


"""
-------------------------------------------------------------------------
## 5.1. Birthday Calculator

Given the following dictionary, design a function that
consumes a `Customer` and produces a string that represents the
month and day that is a week before their birthday.
-------------------------------------------------------------------------
"""

days_in_month = {
    "January" : 31, 
    "February" : 28, 
    "March" : 31, 
    "April" : 30, 
    "May" : 31, 
    "June" : 30, 
    "July" : 31, 
    "August" : 31, 
    "September" : 30, 
    "October" : 31,
    "November" : 30,
    "December" : 31 
}


"""
-------------------------------------------------------------------------
## 5.2. Adding items to Customer

Given the following dictionaries that represent bills, design a
function that takes a bill and `Customer` and returns a `Customer`
with bill added to their menu item count totals.
-------------------------------------------------------------------------
"""

bill_01 = {
    "Fish Taco": 2,
    "Sushi Roll": 2,
    "Espresso": 2
}

bill_02 = {
    "Tiramisu": 1,
    "Chocolate Lava Cake": 1,
}


bill_03 = {
    "Spaghetti": 1,
    "Garlic Bread": 5,
    "Espresso": 3
}

"""
-------------------------------------------------------------------------
## 5.3. Total amount of spending

Given the following dictionary that represents a menu, design
a function that takes a `Customer`, a string item, and calculates
the total amount they have spent on that item.
-------------------------------------------------------------------------
"""

menu_items = {
    "Spaghetti": 23.99,
    "Salad": 12.50,
    "Fish Taco": 8.99,
    "Cheeseburger": 14.99,
    "Grilled Chicken Sandwich": 11.49,
    "Steak Frites": 29.99,
    "Margherita Pizza": 16.25,
    "Vegetable Stir Fry": 13.75,
    "Lobster Bisque": 18.50,
    "French Fries": 5.99,
    "BBQ Ribs": 24.99,
    "Chicken Caesar Salad": 13.99,
    "Buffalo Wings": 9.99,
    "Sushi Roll": 15.49,
    "Vegan Burger": 14.25,
    "Garlic Bread": 4.75,
    "Shrimp Scampi": 22.50,
    "Tiramisu": 7.99,
    "Chocolate Lava Cake": 8.50,
    "Espresso": 3.50
}



"""
-------------------------------------------------------------------------
6. Open Design Challenge (Bonus)

Finish this question last. Marks will not be given for it if
the other questions are not complete.

This question is testing your ability to perform data
design given a general problem. You will be marked on how your data
design is a useful and realistic description of things in the real world.

Choose another business that you want to model. It can be any business
that has to deal with real, physical inventory. Model as many aspects
of the business as you can in your remaining exam time with data classes.

Top marks will be given for data classes that include methods that
follow the HtDF formula, but you can stop at the Stub. For example,
a method for the `Customer` class from the previous question could be:

def get_total(self) -> float:
    '''
    Purpose: Returns the total amount that a customer has spent.
    Examples:
       c = Customer("1992", "January", 1, "Paul", "paul.bucci@ubc.ca", { "Fish Taco": 2 })
       c.get_total() -> menu_items["Fish Taco"] * 2 == 8.99 * 2 == 17.98
    '''
    return 0.0 # stub
    
c = Customer("1992", "January", 1, "Paul", "paul.bucci@ubc.ca", { "Fish Taco": 2 })
expect(c.get_total(), menu_items["Fish Taco"] * 2)
-------------------------------------------------------------------------
"""