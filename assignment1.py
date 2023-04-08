def login():
    # leitourgia login gia ton xristi
    username = input("Give the username please: ")
    # cheackareu an to username einai swsto
    if username in log:
        # chekarei to password
        password = int(input("Give the password please: "))
        # an to password einai swsto tote ektelei tin mainp
        if log[username] == password:
            print("\nLogin successful!")
            mainp()
        else:
            # elenxgi to lathos password
            print("Wrong password! Please try again!")
            login()
    else:
        # elexgi to lathos username
        print("Username does not exist! Try again!")
        login()

def mainp():
    print()
    print("What would you like to do? \n")                        #Dinei tis 4 epilogi ston xristi gia na xekinisi to programma
    print("1: Add a new order.")
    print("2: Show stats.")
    print("3: Export files.")
    print("4: End shift.")

    cho = int(input("Give me your option: "))
    if cho == 1: 
        add()
    elif cho == 2:
        show()
    elif cho == 3:
        printf()
    elif cho == 4:
        end()
     #elegxei ton xristi gia tyxon lathos epilogi
    else:
        print("Wrong input!")
        mainp()


def add():
    name = input("Give customer's name: ")                       #zitaei apo ton to onoma tou pelati, to poso tis paraggelias kai tin dieuthinsi
    order = float(input("Give me the order's amount: "))
    adr = input("Give customer's address: ")

    # eisagwgi twn stoixeiwn toy pelati stis listes
    address.append(adr)
    customers.append(name)
    amount.append(order)
    ordate.append(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    if name in cuscode:
        print("\nOrder registered successfully!\n")
        mainp()
    else:
        # tyxeio arithmos gia to onoma
        code = random.randint(100000, 999999)
        # eisagwgi tou kwdikou sti lista
        cuscode.update({name : code})
        # eisagwgi tou onomatos sti lista
    print("\nOrder registered successfully!\n")
    mainp()


def show():
    print("What would u like to see?? \n")                      #zitaei apo ton xristi poio statistiko arxeio thelei na dei apo tis 5 epiloges poy tou dinontai
    print("1: Number of orders.")
    print("2: Total amount of income recorded.")
    print("3: Customer list.")
    print("4: Amount of orders per customer.")
    print("5: Amount of income per customer.")
    opt = int(input("Choose an option: "))

    # dinei tis epiloges ston xristi
    if opt == 1:
        print("Number of completed orders: ", len(amount))   # ektipwnei to plithos twn paraggeliwn
    elif opt == 2:
        print("Income until now is: ", sum(amount))          # ektipwnei to poso twn paraggeliwn
    elif opt == 3:
        print("The customer list is: ", customers)          # ektipwnei tin lista me ta onomata twn pelatwn

    elif opt == 4:
        #dimioyrgi ena keno lexiko
        lex = {}
        # pernaei mesa apo lista me tous pelates
        for k in range(len(customers)):
            # arxikopoiei thn metablhth gia na apothikeytei o arithmos paraggelivn gia kathe pelati
            cn = 0
            # chekarei an o pelatis vrisketai idi sti lista
            if customers[k] in lex:
                # ean o pelatis einai idi stin lista
                cn = lex[customers[k]]
                # tha auksisei kata 1 ton arithmo twn paraggeliwn tou vste na metrisi kai i trexvn paraggelia stin lista
            cn += 1
            # to lexiko enimeronetai gia ton pelati me tin prosthiki tis kainourias paraggelias
            lex[customers[k]] = cn

        print(lex)

    elif opt == 5:
        lex1 = {}        # # Create an empty dictionary called lex1 to store the customer's name and the amount spent.

        # pernaei mesa apo lista me tous pelates
        for m in range(len(customers)):
            # arxikopoiei thn metablhth gia na apothikeytei to sinoliko poso gia ton pelati
            cm = 0
            # chearei sto lex1 gia na dei an o pelatis vrisketai idi sti lista
            if customers[m] not in lex1:
                # an o pelatis den einai sto lexiko, ton prosthetei me kleidi me tin timi miden
                lex1[customers[m]] = 0

                for n in range(len(customers)):

                    if customers[m] == customers[n]:   # sigkrinei an o pelatis einai idios me ton pelati stin lista

                        cm = lex1[customers[m]]        #dini to sinoliko poso

                        cm += amount[m]               # auksisei to sinoliko poso kata to poso tis paraggelias tou pelati

                        lex1[customers[m]] = cm    #enimeroni to lexiko me to sinoliko poso tou pelati

                print(lex1)

    else:
        print("Wrong input!")
        show()
        mainp()

def printf():
    i = 0
    print("\nWhat would u like to print? \n")               # rwtaei poio arxeio thelei na eksagwsei o xristis apo tis 3 epiloges
    print("1: Print customer names in a txt file.")
    print("2: Print order details per user.")
    print("3: Go back.")

    inp = int(input("Choose an option: "))
   
    if inp == 1:
    # anoigei to arxeio txt se append mode
        fa = open("Onomata.txt", "a+")
        fa.write("####This is the customer name file##### \r\n \r\n")   #grafei tin kefalida sto arxeio kai meta mpainei nea grammi

        for k in customers:          #pernaei apo tin lista tvn pelatwn
            fa.write("\r\n")         # nea grammi
            fa.write(k)              #to onoma tou pelati sto arxeio
    
        fa.write("\r\n####Finished...####")
        fa.close()                   #kleinei to arxeio
        mainp()

    elif inp == 2:
        fb = open("Paraggelies.txt", "a+")                                   #anoigei to arxeio txt
        fb.write("####This is the order per user file##### \r\n \r\n")       #grafei tin kefalida sto arxeio kai meta mpainei nea grammi

        fb.write("The following orders are from the user: ")
        user = input("Give Username: ")                                     #zitaei tpo ton xristi na dwsei to onoma tou pelati
        fb.write(user)                                                      #grafei to onoma tou pelati sto arxeio
        fb.write("\r\n \r\n")                                               #mpainei nea grammi

        #pernaei apo tin lista tvn pelatwn
        for i in range(len(customers)):

            # ginetai elexgos an to onoma toy trexon pelati einai idio me to onoma pou edose o xristis prin
            if customers[i] == user:

                fb.write("\r\tName: ")                             #grafei sto arxeio to onoma, to poso tis paraggelias tin imerominia
                fb.write(customers[i])
                fb.write("\r\t")
                fb.write("\r\tOrder: %d \r\t" %amount[i])
                fb.write("\r\tDate: ")
                fb.write(ordate[i])
                fb.write("\r\n")
     
        fb.write("\r\n####Finished...####")
        fb.close()
        mainp()
    elif inp == 3:
        mainp()
    else:
        print("Wrong input!")
     
        printf()
    mainp()
    

def end():
    # telos tou programmatos
    cl = input("\nDo you really want to log out and close the program? (y/n)")
    if cl == "y":
        return
    elif cl == "n":
        mainp()
    else:
        print("\nWrong input try again!")
        end()


import random     #eisanagwgi tyxeiou arithmou
import datetime   #eisagwgi hmeromhnias

# lista me ta onomata twn xristvn kai toys kwdikous tous, hmeromhnies kai posotites twn paraggeliwn kai tis dieuthinseis tvn pelatwn
log = {"User1":1234, "User2":1235, "User3":1236}
address = []
amount = []
customers = []
ordate = []
cuscode = {}
lex = {}
lex1 = {}
# arxi programmatos me to minima
print("###Welcome to coffee G shop !###")            #eisagwgh sto programma
login()                                              #xekiaei i sinartisi login
