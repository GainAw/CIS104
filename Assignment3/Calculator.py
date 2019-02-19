def calculator():
    first_num = None
    cont = True
    while cont == True:
        right = True
        if first_num == None:
            first_num = int(input ("What is yo first number? "))
        second_num = int(input ("What is yo second number? "))
        opr = input (
        """
        What do you wish to do with the numbers?\n
        +: add\n
        -: subtract\n
        *: multiply\n
        /: divide\n
        ^: to power of\n
        """)
        if opr == "+":
            answer = first_num + second_num
        elif opr == "-":
            answer = first_num - second_num
        elif opr == "*":
            answer = first_num * second_num
        elif opr == "/":
            answer = first_num / second_num
        elif opr == "^":
            answer = first_num ** second_num
        else:
            print("Please enter a correct operation!")
            right = False
        if right == True:
            print("{} {} {} = {}".format(first_num, opr, second_num, answer))
            first_num = answer
        else:
            print("Please try again!")
            continue
        roon = input ("Would you like to continue? Y/N ")
        if roon == "y" or roon == "Y":
            cont = True
        elif roon == "n" or roon == "N":
            cont = False
        return (cont)

if __name__ == '__main__':
    calculator()