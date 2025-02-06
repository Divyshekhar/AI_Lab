def AND (a, b):
 
    if a == 1 and b == 1:
        return True
    else:
        return False
def NAND (a, b):
    if(a == 1 and b == 1):
        return False
    else:
        return True
def OR (a, b):
    if(a == 1 or b == 1):
        return True
    else:
        return False
def NOR(a, b):
    if(a == 0 and b == 0):
        return True
    else:
        return False
       
def XOR(a, b):
    if(a != b):
        return True
    else:
        return False
def XNOR(a, b):
    if(a == b):
        return True
    else:
        return False
def NOT(a):
   return not(a)

if __name__ == '__main__':
   print("choose from the following     ")
   choice = int(input("\n1) AND \n 2) OR \n 3) XOR \n 4) NAND \n 5) NOR \n 6) XNOR \n 7) NOT"))
   data = input("enter the logics in format x y: ")
   a, b = map(int, data.split())
   if(choice == 1):
        result = AND(a , b)
        print (result)
   elif(choice == 2):
       result = OR(a, b)
       print (result)
       
   elif(choice == 3):
       result = XOR(a, b)
       print(result) 
   elif(choice == 4):
       result = NAND(a, b)
       print(result)
   elif(choice == 5):
       result = NOR(a, b)
       print(result)
   elif(choice == 6):
       result = XNOR(a, b)
       print(result)
   elif(choice == 7):
       result = NOT(a,b)
       print(result)
   else:
       print("wrong input")
