def converToBinary(n):
    binary = ""
    while n > 0:
        binary = str(n%2) + binary
        n = n // 2
    return binary
def converToDecimal(n):
    decimal = 0
    power = len(str(n)) - 1
    for digit in n:
        decimal += int(digit) * 2**power
        power -= 1
    return decimal