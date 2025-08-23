try:
    x = int(input("Enter a number: "))
    result = 10 / x
except ValueError:
    print("That’s not a number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("Some other error:", e)

