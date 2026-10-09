skaitli = [4, 7, 2, 9, 7, 1]
meklet = int(input("Ievadi meklējamo skaitli: "))
atrasts = False
for i in range(len(skaitli)):
    if skaitli[i]==  meklet:
        print("Skitlis atrasts indeksā:", i)
        atrasts = True
        break
if atrasts == False:
    print("Nav atrasts")