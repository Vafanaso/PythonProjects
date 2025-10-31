def square_root(number):

    if number == (0 or 1):
        return number
    if number < 0:
        raise ValueError("Number must be bigger positive")
    mid = number // 2
    while mid*mid != number:
        if mid*mid < number:
            mid += 1
        if mid*mid > number:
            mid -= 1
    return mid
print (square_root(25))


#Binary search method is computationaly better
"""
def integer_sqrt(n):
    if n < 0:
        raise ValueError("Cannot compute square root of negative number")
    if n == 0 or n == 1:
        return n

    # Binary search range
    start, end = 1, n
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        square = mid * mid

        if square == n:
            return mid  # Perfect square
        elif square < n:
            start = mid + 1
            ans = mid  # store floor value
        else:
            end = mid - 1

    return ans  # integer square root (floor value)

"""