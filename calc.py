def add(a, b):
    # Ensure both numbers are strings and handle negative numbers
    a, b = str(a), str(b)
    if len(a) < len(b):  # Pad the shorter number with leading zeros
        a, b = b, a
    b = b.zfill(len(a))

    carry = 0
    result = []
    for i in range(len(a) - 1, -1, -1):  # Process digits from right to left
        total = int(a[i]) + int(b[i]) + carry
        carry = total // 10
        result.append(str(total % 10))
    if carry:
        result.append(str(carry))
    return ''.join(result[::-1])
def subtract(a, b):
    a, b = str(a), str(b)
    if len(a) < len(b):  # Pad the shorter number with leading zeros
        a, b = b, a
    b = b.zfill(len(a))

    borrow = 0
    result = []
    for i in range(len(a) - 1, -1, -1):  # Process digits from right to left
        diff = int(a[i]) - int(b[i]) - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(diff))
    # Remove leading zeros
    return ''.join(result[::-1]).lstrip('0') or '0'
def subtract(a, b):
    a, b = str(a), str(b)
    if len(a) < len(b):  # Pad the shorter number with leading zeros
        a, b = b, a
    b = b.zfill(len(a))

    borrow = 0
    result = []
    for i in range(len(a) - 1, -1, -1):  # Process digits from right to left
        diff = int(a[i]) - int(b[i]) - borrow
        if diff < 0:
            diff += 10
            borrow = 1
        else:
            borrow = 0
        result.append(str(diff))
    # Remove leading zeros
    return ''.join(result[::-1]).lstrip('0') or '0'

def multiply(a, b):
    a, b = str(a), str(b)
    result = '0'
    for i in range(len(b) - 1, -1, -1):
        carry = 0
        temp_result = ['0'] * (len(b) - 1 - i)  # Shift by position
        for j in range(len(a) - 1, -1, -1):
            product = int(a[j]) * int(b[i]) + carry
            carry = product // 10
            temp_result.append(str(product % 10))
        if carry:
            temp_result.append(str(carry))
        result = add(result, ''.join(temp_result[::-1]))
    return result

def divide(a, b):
    a, b = str(a), str(b)
    if b == '0':
        raise ValueError("Division by zero")

    quotient = ''
    remainder = ''
    for digit in a:
        remainder += digit
        count = 0
        while subtract(remainder, b) not in ('0', remainder):  # Perform subtraction
            remainder = subtract(remainder, b)
            count += 1
        quotient += str(count)
    return quotient.lstrip('0') or '0', remainder

def modulo(a, b):
    _, remainder = divide(a, b)
    return remainder

def exponentiate(a, b):
    result = '1'
    for _ in range(int(b)):
        result = multiply(result, a)
    return result

def factorial(n):
    result = '1'
    for i in range(2, int(n) + 1):
        result = multiply(result, str(i))
    return result


def repl():
    """
    Entry point of the repl
    """
    print("Welcome to the Arbitrary-Precision Integer Calculator")
    print("Supported operations: +, -, *, /, %, ^, ! (factorial)")
    print("Type 'exit' to quit.")
    
    while True:
        try:
            expr = input(">>> ").strip()
            if expr.lower() == 'exit':
                print("Goodbye!")
                break

            # Parse expression
            if '!' in expr:  # Factorial
                n = expr.replace('!', '').strip()
                print(factorial(n))
            elif '^' in expr:  # Exponentiation
                a, b = map(str.strip, expr.split('^'))
                print(exponentiate(a, b))
            elif '+' in expr:  # Addition
                a, b = map(str.strip, expr.split('+'))
                print(add(a, b))
            elif '-' in expr:  # Subtraction
                a, b = map(str.strip, expr.split('-'))
                print(subtract(a, b))
            elif '*' in expr:  # Multiplication
                a, b = map(str.strip, expr.split('*'))
                print(multiply(a, b))
            elif '/' in expr:  # Division
                a, b = map(str.strip, expr.split('/'))
                quotient, remainder = divide(a, b)
                print(f"Quotient: {quotient}, Remainder: {remainder}")
            elif '%' in expr:  # Modulo
                a, b = map(str.strip, expr.split('%'))
                print(modulo(a, b))
            else:
                print("Invalid expression.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    repl()
