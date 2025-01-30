def mysum(*args):
    """
    This function takes in any number of arguments and returns the sum of the numbers using a for loop.
    """
    total = 0
    for i in args:
        total += i
    return print(f"The sum of the numbers is: {total}")

mysum(1,2,3)
mysum(10,20,30,40,50)