import getopt, sys


def main():
    try:
        optlist, args = getopt.getopt(sys.argv[1:],'o:n:m:', ['operacion=', 'num1=', 'num2='])

    except getopt.GetoptError as err:
        print("err")
        sys.exit(2)

    for opt, args in optlist:
        if opt in ('-o', '--operacion'):
            operacion = args
            
        elif opt in ('-n', '--num1'):
            num1 = args
            
        elif opt in ('-m', '--num2'):
            num2 = args
            
    if operacion == '+':
        cuenta = int(num1) + int(num2)
    elif operacion == '-':
        cuenta = int(num1) - int(num2)
    elif operacion == '*':
        cuenta = int(num1) * int(num2)
    elif operacion == '/':
        cuenta = int(num1) / int(num2)


    print(num1,operacion,num2,'=',cuenta)

if __name__ == '__main__':
    main()