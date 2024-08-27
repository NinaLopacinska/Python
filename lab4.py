#ZAD.1


print("Zadanie 1")
a= int(input("Podaj długość ciągu: "))
ciag=[]
for _ in range(a):
  ciag.append(input("Podaj wyrazy ciagu: "))
  ciagInt= [int(x) for x in ciag ]

for y in ciagInt:
  if y%2==0:
    print("licza parzysta: ", y)
else:
    {
        print("Brak parzystych wyrazow ciagu. ")
    }




#ZAD.2

print("Zadanie 2")
a= int(input("Podaj długość ciągu: "))
ciag=[]
for _ in range(a):
  ciag.append(input("Podaj wyrazy ciagu: "))
  ciagInt= [int(x) for x in ciag ]

for y in ciagInt:
  if y%3==0:
    print("licza podzielna przez 3: ", y)
else:
    {
        print("Brak wyrazow ciagu podzielnych przez 3. ")
    }


#ZAD.3

print("Zadanie 3")
a= int(input("Podaj ilość miast, którą chcesz podać: "))

miastaLudnosc={}

for i in range(a):
  miasto= (input("Podaj nazwe miasta: "))
  ludnosc=(input("Podaj ludność tego miasta: "))
  miastaLudnosc[miasto]= ludnosc

for x,y  in miastaLudnosc.items():
  if int(y) >=300000:
    print("Miasta powyżej 300 000 ludzi: ", x )
else:
    {
        print("Podane miasta maja mniej niz 300000 mieszkancow. ")
    }



#ZAD. 4

print("Zadanie 4")
a= int(input("Podaj długość ciągu: "))
ciag=[]
for _ in range(a):
  ciag.append(input("Podaj wyrazy ciagu: "))
  ciagInt= [int(x) for x in ciag ]

for y in ciagInt:
    text= f"{y}"
    if len(text) == 3 and text[0] == text[2]:
        print("Odp: ", text)
    else:
        {
            print(y, "-" , "Podana liczba nie spelnia warunku.")
        }



#ZAD.5

print("Zadanie 5")
a= int(input("Podaj długość ciągu: "))
ciag=[]
for _ in range(a):
  ciag.append(input("Podaj wyrazy ciagu: "))
  ciagInt= [int(x) for x in ciag ]

for y in ciagInt:
    text= f"{y}"
    if len(text) == 4:
      text2= int(text[0]) + int(text[3])
      if (text2)%2==0:
        print("Odp: ", text)



