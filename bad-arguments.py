class NonIntArgumentException(Exception):
    pass

def handleNonIntArguments(func):
    def wrapper(*args, **kwargs):
        try:
            # Check for non-integer arguments within the wrapper
            for arg in args:
                if not isinstance(arg, int):
                    # Raise the custom exception here, so it's caught immediately by the except block below
                    raise NonIntArgumentException 
            
            # Return the result of the decorated function call only if all checks pass
            result = func(*args, **kwargs)
            return result
        
        except NonIntArgumentException:
            print("Not an integer! Try again :(")
        except TypeError as e:
            # This block might still handle edge cases, but should be rare with the check above
            print(f"A TypeError occurred: {e}")
            
    return wrapper

# Example function to be decorated
@handleNonIntArguments
def add_numbers(*args):
    # The check is now in the wrapper, so the function can just perform the sum
    return sum(args)

# Test cases
print("Trying test case: (1, 2, 3)")
# This will now print the 'Pass!' message instead of the result directly
add_numbers(1, 2, 3) 
print("\nTrying test case: (1, 2, '3')")
# This will trigger the NonIntArgumentException handling
add_numbers(1, 2, '3')

print("\nTrying test case: (1.0, 2.0, 3.0)")
# This will also trigger the NonIntArgumentException handling
add_numbers(1.0, 2.0, 3.0)
