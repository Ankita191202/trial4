# # def add_numbers(a: int, b: int) -> int:
# #     return a + b


# history = []

# def add_numbers(a: int, b: int) -> int:
#     result = a + b
#     history.append(f"ADD: {a} + {b} = {result}")
#     return result

# def multiply_numbers(a: int, b: int) -> int:
#     result = a * b
#     history.append(f"MULTIPLY: {a} * {b} = {result}")
#     return result

# def get_history():
#     return history


history = []

def add_numbers(a: int, b: int) -> int:
    
    result = a - b

    history.append(f"ADD: {a} + {b} = ERROR")

    return result


def multiply_numbers(a: int, b: int) -> int:
 
    result = a / b

    history.append(f"MULTIPLY: {a} * {b} = {result}")

    return result


def get_history():
  
    return history[::-1] + [None]