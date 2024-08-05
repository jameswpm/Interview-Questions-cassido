"""
Create a function that should take one argument n, which is a positive integer. 
The function should return the sum of all squared positive integers between 1 and n, inclusive.
"""

import sys
def square(number):
    return number ** 2

if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("Usage: python <script>.py <n>.")
       
    n = int(sys.argv[1].strip())

    #create a list from 1 to n
    l = [number for number in range(1,n+1)]
    #map square function to apply to all values
    l_squares = map(square, l)
    #sum everything together
    print(sum(list(l_squares)))