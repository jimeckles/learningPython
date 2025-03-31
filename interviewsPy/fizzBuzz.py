def fizzBuzz(n):
    response = []
    # check if n is less than 1
    if n < 1:
        return response
    # create fizzBuzz output for number list up to n
    for i in range(1, n + 1):
        label = ""
        # If number is divisible by 3 or has a 3 in it, print "Fizz"
        if i % 3 == 0 or "3" in str(i):
            label += "Fizz"
        # If number is divisible by 5 or has a 5 in it, print "Buzz"
        if i % 5 == 0 or "5" in str(i):
            label += "Buzz"
        response.append(str(i)) if label == "" else response.append(label)

    return response
