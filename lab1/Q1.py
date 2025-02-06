def convertToBinary(n):
    binary=""
    while n>0:
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
def AND (a, b):
    x = int(a)
    y = int(b)
    return str(x & y)
def NAND (a, b):
    x = int(a)
    y = int(b)
    return str(~(x & y))
def OR (a, b):
    x = int(a)
    y = int(b)
    return str(x | y)
def NOR(a, b):
    x = int(a)
    y = int(b)
    return str(~(x | y))
       
def XOR(a, b):
    x = int(a)
    y = int(b)
    return str(x ^ y)
def XNOR(a, b):
    x = int(a)
    y = int(b)
    return str(~(x ^ y))
def NOT(a):
   return str(~(a))

if __name__ == '__main__':
   data = input("enter the input in format x y: ")
   x, y = map(int, data.split())
   a = convertToBinary(x)
   print(f"Binary of {x} is {a}")
   b = convertToBinary(y)
   print(f"Binary of {y} is {b}")
   print("choose from the following     ")
   choice = int(input("\n1) AND \n 2) OR \n 3) XOR \n 4) NAND \n 5) NOR \n 6) XNOR \n 7) NOT"))
   if(choice == 1):
        result = AND(a , b)
        # resultBinary = convertToBinary(result)
        # print ("ResultBinary",resultBinary)
        resultDecimal = converToDecimal(result)
        print("result in Decimal", resultDecimal)
        resultBinary = convertToBinary(resultDecimal)
        print("result in Binary", resultBinary)
   elif(choice == 2):
       result = OR(a, b)
       resultDecimal = converToDecimal(result)
       print("result in Decimal", resultDecimal)
       resultBinary = convertToBinary(resultDecimal)
       print("result in Binary", resultBinary)
       
   elif(choice == 3):
       result = XOR(a, b)
       resultDecimal = converToDecimal(result)
       print("result in Decimal", resultDecimal)
       resultBinary = convertToBinary(resultDecimal)
       print("result in Binary", resultBinary)
   elif(choice == 4):
       result = NAND(a, b)
       resultDecimal = converToDecimal(result)
       print("result in Decimal", resultDecimal)
       resultBinary = convertToBinary(resultDecimal)
       print("result in Binary", resultBinary)
   elif(choice == 5):
       result = NOR(a, b)
       resultDecimal = converToDecimal(result)
       print("result in Decimal", resultDecimal)
       resultBinary = convertToBinary(resultDecimal)
       print("result in Binary", resultBinary)
   elif(choice == 6):
       result = XNOR(a, b)
       resultDecimal = converToDecimal(result)
       print("result in Decimal", resultDecimal)
       resultBinary = convertToBinary(resultDecimal)
       print("result in Binary", resultBinary)
   elif(choice == 7):
       result = NOT(a,b)
       resultDecimal = converToDecimal(result)
       print("result in Decimal", resultDecimal)
       resultBinary = convertToBinary(resultDecimal)
       print("result in Binary", resultBinary )  
   else:
       print("wrong input")
