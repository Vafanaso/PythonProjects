def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1: raise ValueError("Classification is only possible for positive integers.")
    numbers:list[int] = []
    for factor in range(1,number):
        if number % factor == 0: numbers.append(factor)
    if sum(numbers) == number: return "Perfect"
    if sum(numbers) < number: return "Defcient"
    return "Abundant"
print(classify(8))
