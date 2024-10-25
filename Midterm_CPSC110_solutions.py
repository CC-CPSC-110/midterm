from cs110 import expect, summarize
from typing import List, Dict, Any, Tuple, Set
from dataclasses import dataclass

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

def nextNumber(n: int) -> int:
    """
    Purpose: Takes a whole number and produces the next whole number.
    Examples:
        nextNumber(1) ->  1 + 1 == 2
    """
    return n + 1

expect(nextNumber(1), 2)



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
def indexOfAverage(lon: List[int | float]) -> int | float | None: # I'll accept either float or int, or None is fine too
    """
    Purpose: Finds the index of a number that is closest
    to the average of the collection of numbers
    Examples:
        indexOfAverage([1, 2, 3, 4]) -> 2
    """
    pass # not needed to be correct

"""
-------------------------------------------------------------------------
2.2.
Purpose: Takes a start and end index and produces a
collection of all whole numbers between the indices.
-------------------------------------------------------------------------
"""
def rangeBetween(start: int, end: int) -> List[int]:
    """
    Purpose: Takes a start and end index and produces a
    collection of all whole numbers between the indices.
    Examples:
        rangeBetween(0, 2) -> [0, 1, 2] # [1] would be fine too if you interpreted as strictly between
    """
    pass # not needed to be correct

"""
-------------------------------------------------------------------------
2.3. 
Purpose: Takes an element and adds it to a collection of elements
only if the element doesn't already exist in the collection.
-------------------------------------------------------------------------
"""
def ensure(mySet: Set[Any], element: Any) -> Set[Any]:
    """
    Purpose: Takes an element and adds it to a collection of elements
    only if the element doesn't already exist in the collection.
    Examples:
        ensure({1, 2}, 3) -> {1, 2, 3}
    """
    pass # not needed to be correct

"""
-------------------------------------------------------------------------
2.4.
Purpose: Takes a collection, a key, and a value and produces the a
modified collection where the key is associated with a value.
-------------------------------------------------------------------------
"""
def addToDict(dct: Dict[Any, Any], key: Any, value: Any) -> Dict[Any, Any]:
    """
    Purpose: Takes a collection, a key, and a value and produces the 
    modified collection where the key is associated with a value.
    Examples:
        addToDict({"a": 1}, "b", 2) -> {"a": 1, "b": 2}
    """
    pass # not needed to be correct

"""
-------------------------------------------------------------------------
2.5.
Purpose: Takes two numbers and produces an
immutable collection of the two numbers.
-------------------------------------------------------------------------
"""
def makeTuple(a: int, b: int) -> Tuple[int, int]:
    """
    Purpose: Takes two numbers and produces an
    immutable collection of the two numbers.
    Examples:
        makeTuple(1, 2) -> (1, 2)
    """
    pass # not needed to be correct


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
    """
    Purpose: This function goes through a list of numbers, 
             counting the occurance of each number, 
             then returns the number that occurs most frequently.
    Examples:
        fn_for_lon([1, 1, 2, 3]) -> 1
        fn_for_lon([1]) -> 1
        fn_for_lon([1, 1, 2, 2, 2]) -> 2
    """
    acc = dict() # create a dictionary for numbers
    for n in lon: # for each number in the lsit
        if n in acc: # if the number is in the list...
            acc[n] = acc[n] + 1  # increase the count by 1
        else: # if the number is not in the list...
            acc[n] = 1 # set count to 1

    maximum = lon[0] # set maximum to first number in the list
    for n in acc: # for each number in the list
        if acc[n] > maximum: # if there are more occurences of that number...
            maximum = n # set the maximum to that number
    return maximum # return the maximum


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
@dataclass
class Customer:
    year: int
    month: str # could be int
    day: int
    name: str
    email: str
    items: Dict[str, int] 
    # could also be split up, although this wouldn't be best
    # items: List[str]
    # counts: List[int]



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

def weekAhead(customer: Customer) -> str:
    """
    Purpose: produces a string that represents the month and day 
    that is a week before a Customer's birthday.
    Example:
        c = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", dict())
        weekAhead(c) -> December 29

    """
    month = customer.month
    day = customer.day

    # Handle case where the birthday is less than or equal to 7 days away
    if day <= 7:
        days = list(days_in_month.keys())
        month_number = days.index(month) - 1
        month = days[month_number]
        day = days_in_month[month] + day
    day = day - 7
    return f"{month} {day}"


c = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", dict())
expect(weekAhead(c), "December 29")



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
def addItems(customer: Customer, bill: Dict[str, int]) -> Customer:
    """
    Purpose: Adds items to a Customer's history from a bill.
    Examples:
        c0 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", dict())
        c1 = addItems(c0, bill_01) -> Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
                "Fish Taco": 2,
                "Sushi Roll": 2,
                "Espresso": 2
        }
        c2 = addItems(c1, bill_02) -> Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
                "Tiramisu": 1,
                "Chocolate Lava Cake": 1,
                "Fish Taco": 2,
                "Sushi Roll": 2,
                "Espresso": 2
        }
        c3 = addItems(c1, bill_02) -> Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
                "Tiramisu": 1,
                "Chocolate Lava Cake": 1,
                "Fish Taco": 2,
                "Sushi Roll": 2,
                "Espresso": 5,
                "Spaghetti": 1,
                "Garlic Bread": 5
        }

    """
    for item, count in bill.items():
        if item not in customer.items:
            customer.items[item] = count
        else:
            customer.items[item] += count
    return customer

c0 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", dict())
c1 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
        "Fish Taco": 2,
        "Sushi Roll": 2,
        "Espresso": 2
})
c2 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
        "Tiramisu": 1,
        "Chocolate Lava Cake": 1,
        "Fish Taco": 2,
        "Sushi Roll": 2,
        "Espresso": 2
})
c3 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
        "Tiramisu": 1,
        "Chocolate Lava Cake": 1,
        "Fish Taco": 2,
        "Sushi Roll": 2,
        "Espresso": 5,
        "Spaghetti": 1,
        "Garlic Bread": 5
})
expect(addItems(c0, bill_01).items, bill_01)
expect(addItems(c1, bill_02).items, {**bill_01, **bill_02})
expect(addItems(c2, bill_03).items, c3.items)


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

def total(customer: Customer, lookup: str) -> float:
    """
    Purpose: calculates the total amount a customer has spent on an item.
    Example:
        c0 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", dict())
        c1 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
                "Fish Taco": 2,
                "Sushi Roll": 2,
                "Espresso": 2
        })
        c2 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
                "Tiramisu": 1,
                "Chocolate Lava Cake": 1,
                "Fish Taco": 2,
                "Sushi Roll": 2,
                "Espresso": 2
        })
        c3 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
                "Tiramisu": 1,
                "Chocolate Lava Cake": 1,
                "Fish Taco": 2,
                "Sushi Roll": 2,
                "Espresso": 5,
                "Spaghetti": 1,
                "Garlic Bread": 5
        })
        total(c0, "Espresso") -> 0 * 3.50 ==  0.00
        total(c1, "Espresso") -> 2 * 3.50 ==  7.00
        total(c2, "Espresso") -> 2 * 3.50 ==  7.00
        total(c3, "Espresso") -> 5 * 3.50 == 17.50
    """
    acc = 0
    for item in customer.items:
        if item == lookup:
            acc += menu_items[item] * customer.items[item]
    return acc

c0 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", dict())
c1 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
        "Fish Taco": 2,
        "Sushi Roll": 2,
        "Espresso": 2
})
c2 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
        "Tiramisu": 1,
        "Chocolate Lava Cake": 1,
        "Fish Taco": 2,
        "Sushi Roll": 2,
        "Espresso": 2
})
c3 = Customer(1990, "January", 5, "Paul", "pbucci@corpuschristi.ca", {
        "Tiramisu": 1,
        "Chocolate Lava Cake": 1,
        "Fish Taco": 2,
        "Sushi Roll": 2,
        "Espresso": 5,
        "Spaghetti": 1,
        "Garlic Bread": 5
})
expect(total(c0, "Espresso"),    0)
expect(total(c1, "Espresso"),  7.0)
expect(total(c2, "Espresso"),  7.0)
expect(total(c3, "Espresso"), 17.5)

summarize()