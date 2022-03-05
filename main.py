from utils import func

"""
This is the latest working version in master branch.
Any further changes should be commited to dev branch
and merged via pull request to master.
"""

if __name__ == "__main__":
    a = float(input())
    b = float(input())
    print(f'The result is {func(a, b)}')