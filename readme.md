# Stack of pizzas

You have three stacks of pizzas where each pizza has the same diameter, but they may vary in
height. You can change the height of a stack by removing and eating its topmost pizza any
number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same
height. This means you must remove zero or more cylinders from the top of zero or more of the
three stacks until they are all the same height, then return the height.

*Note: Code has to be runnable via console.*

Example:

    h1 = [1, 2, 1, 1]
    h2 = [1, 1, 2]
    h3 = [1, 1]

There are 4, 3 and 2 pizzas in the three stacks, with their heights in the three arrays. Remove
the top 2 pizzas from h1 (heights = [1, 2]) and from h2 (heights = [1, 1]) so that the three stacks
all are 2 units tall. Return 2 as the answer.

*Note: An empty stack is still a stack.*

### Function Description

    int equalStacks(int h1[], h2[], h3[])

Write an equalStacks function with the following parameters:
- *int* h1[n1]: the first array of heights
- *int* h2[n2]: the second array of heights
- *int* h3[n3]: the third array of heights

Returns
*int*: the height of the stacks when they are equalized


## Solution

Run:

    python3 pizzatest.py < inputtest.txt

Input example:
    
    3, 2, 1, 1, 1
    4, 3, 2
    1, 1, 4, 1

Output example:

    Please enter pizza heights in each stack (use comma or space as a separator).
    STACK #1: STACK #2: STACK #3: 
    Height: 5
