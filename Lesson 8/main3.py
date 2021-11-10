def divide(a, b):
    return a/b

try:
    x, y = [int(x) for x in input().split()]
    result = divide(x, y)
    print(result)

except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Not numeric input")
else:
    print("No errors")