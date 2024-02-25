import re

def camel_to_snake(camel_case):
    snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case).lower()
    return snake_case

camel_string = input("Enter the camel case string: ")
snake_string = camel_to_snake(camel_string)
print("Snake case string:", snake_string)