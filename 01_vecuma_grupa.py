print("Vecuma grupa")

vecums = int(input("Ievadi savu vecumu: "))
if vecums <= 6:
    grupa= "bērns"
elif vecums <= 17:
    grupa= "pusaudzis"
elif vecums <= 39:
    grupa= "pieaugušais"
elif vecums <= 50:
   grupa= "seniors"

 # TODO: Pievienots vecuma grupas uzdevums ar if


print(f"Jusu vecuma grupa ir {grupa}")