from utils import subtract_func, sum_func

"""
This is the latest working version in master branch.
Any further changes should be commited to dev branch
and merged via pull request to master.
"""

if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f'The sum is {sum_func(a, b)}')
    print(f'The difference is {subtract_func(a, b)}')
