vards=input("Ievadi savu vārdu nominatīvā locijumā (Kas?):")

vards=vards.lower() 
# funkcija .lower()- visus burtus kovertē par mazajiem burtiem.

vards=vards.capitalize()
# funkcija .capitalize()- simbolu virknē pirmo burtu konvertē par lielo.

UzminiVardu="saies"

minejums=None

while UzminiVardu!=minejums:
    # cikls strādā, kamēr netiek ievadīts vārds "saies"
    # ! = nav vienāds
    minejums=input(f"Uzmini vārdu {UzminiVardu[1]+UzminiVardu[2]+UzminiVardu[0]+UzminiVardu[4]+UzminiVardu[3]}: ")

print("Pareizi!")

UzminiVardu="kaķis"

while True:
    minejums=input(f"Uzmini vārdu {UzminiVardu[1]+UzminiVardu[2]+UzminiVardu[0]+UzminiVardu[4]+UzminiVardu[3]}: ")

    if UzminiVardu==minejums:
        print("Pareizi!")
        break

UzminiVardu="skola"

meginajumi=2

for i in range(3):
    minejums=input(f"Uzmini vārdu {UzminiVardu[1]+UzminiVardu[2]+UzminiVardu[0]+UzminiVardu[4]+UzminiVardu[3]}: ")

    if UzminiVardu==minejums:
        print("Pareizi!")
        break
    else:
        print(f"Neuzminēji, tev palikuši {meginajumi} mēģinājumi.")
        meginajumi-=1
print("Spēles beigas!")