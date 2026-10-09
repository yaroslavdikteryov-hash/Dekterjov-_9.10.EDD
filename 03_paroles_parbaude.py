parole = "1234"
meginajumi = 0
while meginajumi < 3:
    ievade  = input("Ievade parole:" )
    if ievade == parole:
        print("Piekļuve atļauta XD ")
        break
    else:
        meginajumi += 1
        print("Nepareize parole")
if meginajumi == 3:
    print("Piekļuve bloķēta")
