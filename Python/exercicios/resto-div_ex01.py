# Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers. (codewars)


# Se a divisão por 2 tiver resto 0 - "Even"
# Se não - "Odd"
# Even - Par
# Odd - ímpar

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    elif number % 0:
        return "Don't exist"
    else:
        return "Odd"
