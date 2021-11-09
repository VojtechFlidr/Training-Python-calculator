def calculate():
    operation = input('''
    Definujte jakou funkci budete chtit pouzit
    + pro scitani
    - pro odecitani
    * pro nasobeni
    / pro deleni
    '''
    )
    cislo_jedna = int(input("Zadej prvni cislo: "))
    cislo_dva = int(input("Zadej druhe cislo: "))

    if operation == '+':
        print('{} + {} = '.format(cislo_jedna, cislo_dva))
        print(cislo_jedna + cislo_dva)

    elif operation == '-':
        print('{} - {} = '.format(cislo_jedna, cislo_dva))
        print(cislo_jedna - cislo_dva)

    elif operation == '*':
        print('{} * {} = '.format(cislo_jedna, cislo_dva))
        print(cislo_jedna * cislo_dva)

    elif operation == '/':
        print('{} / {} = '.format(cislo_jedna, cislo_dva))
        print(cislo_jedna / cislo_dva)

    else:
        print ("Napiste prosim spravnou funkci a opakujte akci")

    again()

def again():
    again_definice = input ('''
    Chcete vypocitat dalsi priklad?
    Pokud ano, napiste Y, pokud ne napiste N
    ''')
    if again_definice.upper() == "Y":
        calculate()
    elif again_definice.upper() == "N":
        print ('Navidenou')
    else:
        again()

calculate()
