import re

def addBinaryNumbers(num1, num2, choice=0):
    resultant =""
    if choice ==0:
        binaryNum1, binaryNum2 = decimalToBinary(num1), decimalToBinary(num2)
        sum_binary_character =0
        for i in range(BITS_SYSTEM, 0, -1):
            sum_binary_character += eval(binaryNum1[i-1]+ "+" +binaryNum2[i-1])
            sum_binary_character, resultantCharacter= divmod(sum_binary_character, BASE_NUMBER)
            resultant += str(resultantCharacter)
    else:
# One complement addition
        if choice ==1:
            binaryNum1, binaryNum2 = decimalToBinary(num1), decimalToBinary(num2)
            sum_binary_character =0
            for i in range(BITS_SYSTEM, 0, -1):
                sum_binary_character += eval(binaryNum1[i-1]+ "+" +binaryNum2[i-1])
                sum_binary_character, resultantCharacter= divmod(sum_binary_character, BASE_NUMBER)
                resultant += str(resultantCharacter)
#                when the first binary character at index 0 is added and then possess a 1 or zero it returns to the bottom of the last binary character at index 4
                if i == 1:  
                    result =""
                    for ch in resultant:
                        sum_binary_character += eval(ch)
                        sum_binary_character, resultCharacter= divmod(sum_binary_character, BASE_NUMBER)
                        result += str(resultCharacter)   
                    resultant = result
                    
# Two complement addition 
        if choice == 2:
            binaryNum1, binaryNum2 = twoComplement(num1), twoComplement(num2)
            sum_binary_character =0
            for i in range(BITS_SYSTEM, 0, -1):
                sum_binary_character += eval(binaryNum1[i-1]+ "+" +binaryNum2[i-1])
                sum_binary_character, resultantCharacter= divmod(sum_binary_character, BASE_NUMBER)
                resultant += str(resultantCharacter)
                    
    return resultant[len(resultant)::-1]

def twoComplement(decimalvalue):
    binary_number = decimalToBinary(decimalvalue)
    add_binary_character_to_end =1
    two_complement_binary_number = ""
    for i in range(BITS_SYSTEM, 0, -1):
        add_binary_character_to_end += eval(binary_number[i-1])
        add_binary_character_to_end, resultantCharacter= divmod(add_binary_character_to_end, BASE_NUMBER)
        two_complement_binary_number  += str(resultantCharacter)
    return  two_complement_binary_number[len(two_complement_binary_number)::-1]
    
def oneCompliment(ch):
    if ch == '1':
        return '0'
    else:
        return '1'

def decimalToBinary(decimalvalue):
    global BITS_SYSTEM
    global BASE_NUMBER
    BASE_NUMBER =2
    BITS_SYSTEM =8    
    binaryNumber = ""
    
#     normal binary with no complement 
    if not decimalvalue.strip().isdigit():
        for i in range(BITS_SYSTEM):
            decimalvalue, binaryCharcter = divmod(abs(int(decimalvalue)), BASE_NUMBER)
            binaryNumber += oneCompliment(str(binaryCharcter))
        return binaryNumber[len(binaryNumber)::-1]
    
#  returns complement    
    else:
        for i in range(BITS_SYSTEM):
            decimalvalue, binaryCharcter = divmod(abs(int(decimalvalue)), BASE_NUMBER)
            binaryNumber += str(binaryCharcter)
        return binaryNumber[len(binaryNumber)::-1]

def display(numbers):
    if not (numbers[0].strip().isdigit() and numbers[1].strip().isdigit()):
        choice = int(input("Enter a valid method of solution \n(1)Onecomplement or (2)Twocomplement: "))
        while not 1<=choice<=2:
            print("Wrong entry, pls put in the correct choice")
            choice = int(input("Enter a valid method of solution\n(1)Onecomplement or (2)Twocomplement: "))
        if choice ==1:
            print("{:<2s} {:2s}\n{:<2s} {:2s}\n____________\n{:<2d} {:>4s}".format(numbers[0].strip(), decimalToBinary(numbers[0]), numbers[1].strip(), decimalToBinary(numbers[1]), eval(numbers[0]+"+"+numbers[1]), addBinaryNumbers(numbers[0], numbers[1], choice)))
        else:
            print("{:<2s} {:2s}\n{:<2s} {:2s}\n____________\n{:<2d} {:>4s}".format(numbers[0].strip(), twoComplement(numbers[0]), numbers[1].strip(), twoComplement(numbers[1]), eval(numbers[0]+"+"+numbers[1]), addBinaryNumbers(numbers[0], numbers[1], choice)))
    else:
         print("{:<2s} {:2s}\n{:<2s} {:2s}\n____________\n{:<2d} {:>4s}".format(numbers[0].strip(), decimalToBinary(numbers[0]), numbers[1].strip(), decimalToBinary(numbers[1]), eval(numbers[0]+"+"+numbers[1]), addBinaryNumbers(numbers[0], numbers[1])))

def main():
    numbers = input("Enter values to be added in binary form seperated by a space or comma: ")
    values = re.split("[,\\s]", numbers)
    while len(values) !=2:
        numbers = input("Enter values to be added in binary form seperated by a space or comma: ")
        values = re.split("[,\s]", numbers)
    display(values)           

main()
