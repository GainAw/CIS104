def calculator():
    cont = True
    opr_list = ["+","-","*","/","^"]
    func_list = ["","","","","","","","","",""]
    while cont == True:
        right = True
        first_num = input("What is first stuff either number or operator ")
        try:
            first_num = float(first_num)
        except ValueError:
            try:
                if answer == None:
                    print("Ya dingus you would need to do an operation first!!!")
                    continue
            except NameError:
                print("Ya dingus you would need to do an operation first!!!")
                continue
            if first_num in opr_list:
                opr_list.index(first_num)
                opr = first_num
                first_num = answer
        else:
            print (first_num)
        second_num = float(input ("What is yo second number? "))
        print (second_num)
        try:
            if opr == None:
                opr = input (
        """
        What do you wish to do with the numbers?\n
        +: add\n
        -: subtract\n
        *: multiply\n
        /: divide\n
        ^: to power of\n
        """)
        except NameError:
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
        else:
            print("Please try again!")
            continue
        roon = input ("Would you like to continue? Y/N ")
        if roon == "y" or roon == "Y":
            cont = True
        elif roon == "n" or roon == "N":
            cont = False
            return (cont)
