#zad1
plik=open('zad1.txt','w+',encoding="utf-8")
lista=[x for x in range(41) if x%4==0]
plik.write(str(lista))
plik.close()
