while True:
    import colorama
    from colorama import Fore,Back,Style
    colorama.init(autoreset=True)
    print('************************')
    print(Fore.RED+Style.BRIGHT+'Welcome to the Matchem Program!')
    print('************************')
    print('------------------------')
    print(Fore.BLUE+'We here are a bunch of class 12th Students who wanted a handy resource to use during our Chemistry studies\nwhen we came up with this idea.\nThere are several things in this program that you will be able to access.\nHope this helps you!')
    print('------------------------')
    print(Fore.GREEN+'Enter the section of this program that you would like to use:')
    print('Some of these modules take time to load......so hang on there!\n')
    selec=input(Fore.YELLOW+Style.BRIGHT+'\nI-Sophisticated Temprature Calculator->>\n\nII-Sophisticated Physical Chemistry information about elements->>\n\nIII-Reaction Balancer->>\n\nIV-Periodic Table information->>\n\nV-Mathematical Buddy->>\n\nVI-Trignoemtry Value Helper->>\n\nVII-EXIT\n\n')



    #Tempcalci starts here
    if selec=='I':
        while True:
                print("\nPlease select the conversion....")
                inp=input("Press 1 :for Celsius to Fahrenheit\nPress 2 :for Celsius to Kelvin\nPress 3 :for Fahrenheit to Celsius\nPress 4 :for Fahrenheit to Kelvint\nPress 5 :for Kelvin to Celsius\nPress 6 :for Kelvin to Fahrenheit\nPress 7 :exit\n-------> ")

                if inp=='1':
                    ctk=int(input("Please enter the temprature in Celsius : "))
                    k=ctk+273
                    print("The temprature in Kelvin is : ",k , "K")

                if inp=='2':
                    ktc=int(input("Please enter the temprature in Kelvin : "))
                    c=ktc-273
                    print("The temprature in Celsius is : ",c ,"°C")

                if inp=='3':
                    ctf=int(input("Please enter the temprature in Celsius : "))
                    f=((ctf*1.8)+32)
                    print("The temprature in Fahrenheit is : ",f ,"F")

                if inp=='4':
                    ctf=int(input("Please enter the temprature in Fahrenheit : "))
                    c=((ctf-32)*5/9)
                    print("The temprature in Celsius is : ",c ,"°")

                if inp=='5':
                    ftk=int(input("Please enter the temprature in Fahrenheit : "))
                    k=(((ftk-32)*5/9)+273.15)
                    print("The temprature in Kelvin is : ",k ,"K")

                if inp=='6':
                    ktf=int(input("Please enter the temprature in Kelvin : "))
                    f=(((ktf-273.15)*9/5)+32)
                    print("The temprature in Fahrenheit is : ",f ,"F")

                if inp=='7':
                    loop4= input("Do you want to continue? (y/n): ")
                    if loop4== "n":
                        break
    #Tempcalci ended here
    #Mendeleev program starts here
    if (selec=='II'):
        while True:
            from mendeleev import *
            a=print('Enter the alphabet for the operation that you need->>')
            inp=input('A: atomic number\nB: atomic weight\nC:electrons\nD:electronic configuratrion\nE:neutrons\nF:protons\nG:period\nH:Oxidation State\n')
            if inp=='A':
                i=input("Please enter the element's name--->")
                thing_you_need = element(i)
                print('Atomic number for the element is->>',thing_you_need.atomic_number)
            elif inp=='B':
                j=input("Please enter the element's name--->")
                thing_you_need = element(j)
                print('Atomic weight for the element is->>',thing_you_need.atomic_weight)
            elif inp=='C':
                k=input("Please enter the element's name--->")
                thing_you_need = element(k)
                print('Electrons for the element is->>',thing_you_need.electrons)
            elif inp=='D':
                m=input("Please enter the element's name--->")
                thing_you_need = element(m)
                print('Electronic configuration for the element is->>',thing_you_need.ec.conf)
            elif inp=='E':
                n=input("Please enter the element's name--->")
                thing_you_need = element(n)
                print('Neutrons for the element is->>',thing_you_need.neutrons)
            elif inp=='F':
                o=input("Please enter the element's name--->")
                thing_you_need = element(o)
                print('Protons for the element is->>',thing_you_need.protons)
            elif inp=='G':
                p=input("Please enter the element's name--->")
                thing_you_need = element(p)
                print('Period for the element is->>',thing_you_need.period)
            elif inp=='H':
                q=input("Please enter the element's name--->")
                thing_you_need = element(q)
                print('Oxidation State for the element is->>',thing_you_need.oxidation.state)
            else:
                print('there seems to be some error here, please check later')
            loop1= input("Do you want to continue? (y/n): ")
            if loop1== "n":
                break
    #Mendeleev program ended there
    #Balancing program starts there
    if selec=='III':
        while True:
            from chemlib import Compound, Reaction
            print('---------------------')
            print('NOTE')
            print('---------------------')
            print(Fore.RED+"\nThis section of the module is case sensitive. So if you need to find a balanced equation\nyou will need need to put everthing in capitals......")
            print(Fore.RED+'\nAlso put the number of molecules you are going to use for that specific element.')
            print(Fore.BLUE+'\nFor ex.........H2 in first reactant and O in the send reactant to get the required output')
            x=Compound(input("\nEnter The First Reactant:"))
            y=Compound(input("Enter The Second Reactant:"))
            z=Compound(input("Enter The Final Product:"))
            r=Reaction(reactants=[x,y],products=[z])
            print("Given Formula -->",r.formula)
            if (r.is_balanced==False):
                r.balance()
                print("Balanced Formula -->",r.formula)
            else:
                print("Equation Is Already Balanced")
            loop3= input("Do you want to continue? (ya/nope): ")
            if loop3== "nope":
                break
    #Balancing program ended there
    #Periodic Table starts there
    if selec=='IV':
        while True:
            import csv, sys, re

            # Read in all the data from periodictable.csv.
            elementsFile = open('periodictable.csv', encoding='utf-8')
            elementsCsvReader = csv.reader(elementsFile)
            elements = list(elementsCsvReader)
            elementsFile.close()

            ALL_COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name',
                        'Group', 'Period', 'Atomic weight', 'Density',
                        'Melting point', 'Boiling point',
                        'Specific heat capacity', 'Electronegativity',
                        'Abundance in earth\'s crust']

            LONGEST_COLUMN = 0
            for key in ALL_COLUMNS:
                if len(key) > LONGEST_COLUMN:
                    LONGEST_COLUMN = len(key)

            ELEMENTS = {}
            for line in elements:
                element = {'Atomic Number':  line[0],
                        'Symbol':         line[1],
                        'Element':        line[2],
                        'Origin of name': line[3],
                        'Group':          line[4],
                        'Period':         line[5],
                        'Atomic weight':  line[6] + ' u',
                        'Density':        line[7] + ' g/cm^3',
                        'Melting point':  line[8] + ' K',
                        'Boiling point':  line[9] + ' K',
                        'Specific heat capacity':      line[10] + ' J/(g*K)',
                        'Electronegativity':           line[11],
                        'Abundance in earth\'s crust': line[12] + ' mg/kg'}

                for key, value in element.items():
                    # Remove the [roman numeral] text:
                    element[key] = re.sub(r'\[(I|V|X)+\]', '', value)

                ELEMENTS[line[0]] = element  # Map the atomic number to the element.
                ELEMENTS[line[1]] = element

            print('Periodic Table of Elements')
            print()

            while True:
                print(Fore.RED+Style.BRIGHT+'                               Periodic Table of Elements')
                print('''
                ---------------------------------------------------------
                |1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18  |
                |1 H                                                  He|
                |2 Li Be                               B  C  N  O  F  Ne|
                |3 Na Mg                               Al Si P  S  Cl Ar|
                |4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr|
                |5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe|
                |6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn|
                |7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og|
                |                                                       |
                |        Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu      |
                |        Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr      |
                ---------------------------------------------------------
                ''')
                print('Enter a symbol or atomic number to examine, or QUIT to quit.')
                response = input('> ').title()
                if response == 'Quit':
                    sys.exit()
                if response in ELEMENTS:
                    for key in ALL_COLUMNS:
                        keyJustified = key.rjust(LONGEST_COLUMN)
                        print(keyJustified + ': ' + ELEMENTS[response][key])
                    input('Press Enter to continue...')
                    break
    #Periodic Table ended here

    #Maths begins here
    if selec=='V':

        print(Back.GREEN+"Math Module\n")

        #Basic operations

        #Addition
        def add(x, y):
            return x + y

        #Substraction
        def subtract(x, y):
            return x - y

        #Multiplication
        def multiply(x, y):
            return x * y

        #Division
        def divide(x, y):
            return x / y

        #Pi value
        def pi(x):
            return x*3.141592653589793238

        #Square
        def sq(x):
            return x**2

        #Cube
        def cube(x):
            return x**3

        #Power
        def power(x,y):
            return x**y

        #LOGARITHM TABLE
        def log(z):
            print(z)

        print("Select operation:\n\n1.Add\n\n2.Subtract\n\n3.Multiply\n\n4.Divide\n\n5.Pi value\n\n6.Square\n\n7.Cube\n\n8.Power x^y\n\n9.Logarithm Table\n")

        while True:
            oper = input("Enter the operation (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9): ")

            if oper in ('1', '2', '3', '4', '8'):
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if oper == '1':
                    print("Your answer : ", add(a, b))

                elif oper == '2':
                    print("Your answer : ", subtract(a, b))

                elif oper == '3':
                    print("Your answer : ", multiply(a, b))

                elif oper == '4':
                    print("Your answer : ", divide(a, b))

                elif oper == '8':
                    print("Your answer : ", power(a, b))


            if oper in ('5','6','7'):
                a = float(input("Enter the number: "))

                if oper == '5':
                    print("Your answer : ", pi(a))

                elif oper == '6':
                    print("Your answer : ", sq(a))

                elif oper == '7':
                    print("Your answer : ", cube(a))

            if oper in ('9'):
                    print("""
        LOGARITHM TABLE
        ---+------------------------------------------------------------+
        No.| 0.00  0.01  0.02  0.03  0.04  0.05  0.06  0.07  0.08  0.09 |
        ---+------------------------------------------------------------+
        1.0| 0.000 0.004 0.009 0.013 0.017 0.021 0.025 0.029 0.033 0.037|
        ---+------------------------------------------------------------+
        1.1| 0.041 0.045 0.049 0.053 0.057 0.061 0.064 0.068 0.072 0.076|
        ---+------------------------------------------------------------+
        1.2| 0.079 0.083 0.086 0.090 0.093 0.097 0.100 0.104 0.107 0.111|
        ---+------------------------------------------------------------+
        1.3| 0.114 0.117 0.121 0.124 0.127 0.130 0.134 0.137 0.140 0.143|
        ---+------------------------------------------------------------+
        1.4| 0.146 0.149 0.152 0.155 0.158 0.161 0.164 0.167 0.170 0.173|
        ---+------------------------------------------------------------+
        1.5| 0.176 0.179 0.182 0.185 0.188 0.190 0.193 0.196 0.199 0.201|
        ---+------------------------------------------------------------+
        1.6| 0.204 0.207 0.210 0.212 0.215 0.217 0.220 0.223 0.225 0.228|
        ---+------------------------------------------------------------+
        1.7| 0.230 0.233 0.236 0.238 0.241 0.243 0.246 0.248 0.250 0.253|
        ---+------------------------------------------------------------+
        1.8| 0.255 0.258 0.260 0.262 0.265 0.267 0.270 0.272 0.274 0.276|
        ---+------------------------------------------------------------+
        1.9| 0.279 0.281 0.283 0.286 0.288 0.290 0.292 0.294 0.297 0.299|
        ---+------------------------------------------------------------+
        2.0| 0.301 0.303 0.305 0.307 0.310 0.312 0.314 0.316 0.318 0.320|
        ---+------------------------------------------------------------+
        2.1| 0.322 0.324 0.326 0.328 0.330 0.332 0.334 0.336 0.338 0.340|
        ---+------------------------------------------------------------+
        2.2| 0.342 0.344 0.346 0.348 0.350 0.352 0.354 0.356 0.358 0.360|
        ---+------------------------------------------------------------+
        2.3| 0.362 0.364 0.365 0.367 0.369 0.371 0.373 0.375 0.377 0.378|
        ---+------------------------------------------------------------+
        2.4| 0.380 0.382 0.384 0.386 0.387 0.389 0.391 0.393 0.394 0.396|
        ---+------------------------------------------------------------+
        2.5| 0.398 0.400 0.401 0.403 0.405 0.407 0.408 0.410 0.412 0.413|
        ---+------------------------------------------------------------+
        2.6| 0.415 0.417 0.418 0.420 0.422 0.423 0.425 0.427 0.428 0.430|
        ---+------------------------------------------------------------+
        2.7| 0.431 0.433 0.435 0.436 0.438 0.439 0.441 0.442 0.444 0.446|
        ---+------------------------------------------------------------+
        2.8| 0.447 0.449 0.450 0.452 0.453 0.455 0.456 0.458 0.459 0.461|
        ---+------------------------------------------------------------+
        2.9| 0.462 0.464 0.465 0.467 0.468 0.470 0.471 0.473 0.474 0.476|
        ---+------------------------------------------------------------+
        3.0| 0.477 0.479 0.480 0.481 0.483 0.484 0.486 0.487 0.489 0.490|
        ---+------------------------------------------------------------+
        3.1| 0.491 0.493 0.494 0.496 0.497 0.498 0.500 0.501 0.502 0.504|
        ---+------------------------------------------------------------+
        3.2| 0.505 0.507 0.508 0.509 0.511 0.512 0.513 0.515 0.516 0.517|
        ---+------------------------------------------------------------+
        3.3| 0.519 0.520 0.521 0.522 0.524 0.525 0.526 0.528 0.529 0.530|
        ---+------------------------------------------------------------+
        3.4| 0.531 0.533 0.534 0.535 0.537 0.538 0.539 0.540 0.542 0.543|
        ---+------------------------------------------------------------+
        3.5| 0.544 0.545 0.547 0.548 0.549 0.550 0.551 0.553 0.554 0.555|
        ---+------------------------------------------------------------+
        3.6| 0.556 0.558 0.559 0.560 0.561 0.562 0.563 0.565 0.566 0.567|
        ---+------------------------------------------------------------+
        3.7| 0.568 0.569 0.571 0.572 0.573 0.574 0.575 0.576 0.577 0.579|
        ---+------------------------------------------------------------+
        3.8| 0.580 0.581 0.582 0.583 0.584 0.585 0.587 0.588 0.589 0.590|
        ---+------------------------------------------------------------+
        3.9| 0.591 0.592 0.593 0.594 0.595 0.597 0.598 0.599 0.600 0.601|
        ---+------------------------------------------------------------+
        4.0| 0.602 0.603 0.604 0.605 0.606 0.607 0.609 0.610 0.611 0.612|
        ---+------------------------------------------------------------+
        4.1| 0.613 0.614 0.615 0.616 0.617 0.618 0.619 0.620 0.621 0.622|
        ---+------------------------------------------------------------+
        4.2| 0.623 0.624 0.625 0.626 0.627 0.628 0.629 0.630 0.631 0.632|
        ---+------------------------------------------------------------+
        4.3| 0.633 0.634 0.635 0.636 0.637 0.638 0.639 0.640 0.641 0.642|
        ---+------------------------------------------------------------+
        4.4| 0.643 0.644 0.645 0.646 0.647 0.648 0.649 0.650 0.651 0.652|
        ---+------------------------------------------------------------+
        4.5| 0.653 0.654 0.655 0.656 0.657 0.658 0.659 0.660 0.661 0.662|
        ---+------------------------------------------------------------+
        4.6| 0.663 0.664 0.665 0.666 0.667 0.667 0.668 0.669 0.670 0.671|
        ---+------------------------------------------------------------+
        4.7| 0.672 0.673 0.674 0.675 0.676 0.677 0.678 0.679 0.679 0.680|
        ---+------------------------------------------------------------+
        4.8| 0.681 0.682 0.683 0.684 0.685 0.686 0.687 0.688 0.688 0.689|
        ---+------------------------------------------------------------+
        4.9| 0.690 0.691 0.692 0.693 0.694 0.695 0.695 0.696 0.697 0.698|
        ---+------------------------------------------------------------+
        5.1| 0.708 0.708 0.709 0.710 0.711 0.712 0.713 0.713 0.714 0.715|
        ---+------------------------------------------------------------+
        5.2| 0.716 0.717 0.718 0.719 0.719 0.720 0.721 0.722 0.723 0.723|
        ---+------------------------------------------------------------+
        5.3| 0.724 0.725 0.726 0.727 0.728 0.728 0.729 0.730 0.731 0.732|
        ---+------------------------------------------------------------+
        5.4| 0.732 0.733 0.734 0.735 0.736 0.736 0.737 0.738 0.739 0.740|
        ---+------------------------------------------------------------+
        """)

            loop = input("Do you want to continue? (y/n): ")
            if loop == "n":
                break

        else:
                print("Invalid Input")
    #Maths ended
    #Trignometry Begins here
    if selec=='VI':
        while True:
            print(Back.MAGENTA+'This is the trignometry value finder.\n')
            a = 1
            while a >=0:
                operator=input('Enter your requirement\nsin/cos/tan/cosec/sec/cot:')
                angle=int(input('Enter the angle needed for you:'))

                if operator == 'sin':
                    if angle == 0:
                        print('sin0 equals to 0')

                    elif angle == 30:
                        print('sin30 equals 1/2')

                    elif angle == 45:
                        print('sin45 equals 1/√2')

                    elif angle == 60:
                        print('sin60 equals √3/2')
                        sin60 = '√3/2'
                    elif angle == 90:
                        print('sin90 equals 1')
                        sin90 = 1
                    else:
                        print('you didnt give me a string')

                elif operator == 'cos':
                        if angle == 0:
                            print('cos0 equals 1')
                            cos0 = 1
                        elif angle == 30:
                            print('cos30 equals √3/2')

                        elif angle == 45:
                            print('cos45 equals 1/√2')
                            cos45 = '1/√2'
                        elif angle == 60:
                            print('cos60 equals 1/2')
                            cos60 = 1/2
                        elif angle == 90:
                            print('cos90 equals 0')
                            cos90 = 0
                        else:
                            print('you didnt give me a string')

                elif operator == 'tan':
                    if angle == 0:
                        print('tan0 equals 0')
                    elif angle == 30:
                        print('tan30 equals 1/√3')
                    elif angle == 45:
                        print('tan45 equals 1')
                    elif angle == 60:
                        print('tan60 equals √3')
                    elif angle == 90:
                        print('tan90 is undefined')
                    else:
                        print('fatal error')

                elif operator == 'cosec':
                    if angle == 0:
                        print('cosec 0 is not defined')
                    elif angle == 30:
                        print('cosec equals 2')

                        print('cosesc equals √2')
                    elif angle == 60:
                        print('cosec equals 2/√3')
                    elif angle == 90:
                        print('cosec equals 1')
                    else:
                        print('wrong input')

                elif operator == 'sec':
                    if angle == 0:
                        print('sec0 is equal to 1')
                    elif angle == 30:
                        print('sec30 is equal to 2/√3')
                    elif angle == 45:
                        print('sec 45 is equal to √2')
                    elif angle == 60:
                        print('sec60 is equal to 2')
                    elif angle == 90:
                        print('sec90 is undefined')
                    else:
                        print('invalid input')

                elif operator == 'cot':
                    if angle == 0:
                        print('cot0 is undefined')
                    elif angle == 30:
                        print('cot30 is √3')
                    elif angle == 45:
                        print('cot45 is 1')
                    elif angle == 60:
                        print('cot60 is 1/√3')
                    elif angle == 90:
                        print('cot90 is 0')
                    else:
                        print('wrong input')


                else:
                    print('fatal error, please send ss of this to phatak he did mistakes again')

                loop1= input("Do you want to continue? (y/n): ")
                if loop1== "n":
                    break
    if selec== 'VII':
        break
print(Back.BLUE+'Thank you! Hope to see you again!')
