skaits = int(input("Cik skaitļus ievadīsi?"))
if skaits <= 0:
    print("Kļūda: skaitam jābūt pozitīvam!")
else:
    for i in range(skaits):
        skaitlis = int(input("Ievādi skaitli: "))
        if i == 0:
            mazākais = skaitlis
            lielākais = skaitlis
        else:
            if skaitlis < mazākais:
                mazākais = skaitlis
            if skaitlis > lielākais:
                lielākais = skaitlis
    print("Mazākais skaitlis:", mazākais)
    print("Lielākais skaitlis:", lielākais)