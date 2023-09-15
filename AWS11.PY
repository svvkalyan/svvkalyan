try:
    # Simulate a NameError by trying to print an undefined variable
    print(undefined_variable)

    # Simulate a TypeError by adding a string to an integer
    result = 10 + "5"
except NameError as ne:
    print(f"NameError occurred: {ne}")
except TypeError as te:
    print(f"TypeError occurred: {te}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("No errors occurred.")
finally:
    print("This code always runs, regardless of exceptions.")