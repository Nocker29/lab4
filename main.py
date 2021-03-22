# #zad1
# plik=open('zad1.txt','w+',encoding="utf-8")
# lista=[x for x in range(41) if x%4==0]
# plik.write(str(lista))
# plik.close()
#
# #zad2
# plik=open('zad1.txt','r',encoding="utf-8")
# print(plik.read())
# plik.close()

# # zad3
# with open('zad1.txt','r+') as plik:
#     plik.write("Zapisany tekst do pliku ")
#
# with open('zad1.txt','r') as plik:
#     zawartosc=plik.read()
# print(zawartosc)

# #zad4
# class NaZakupy:
#     def __init__(self,nazwa,ilosc,jednostka,cena):
#         self.nazwa_produktu=nazwa
#         self.ilosc=ilosc
#         self.jednostka_miary=jednostka
#         self.cena_jed=cena
#     def wyswietl_produkt(self):
#         tekst=self.nazwa_produktu+" "
#         tekst+=str(self.ilosc)+" "
#         tekst+=self.jednostka_miary+" "
#         tekst+=str(self.cena_jed)
#         return tekst
#     def ile_produktu(self):
#         return str(self.ilosc)+str(self.jednostka_miary)
#     def ile_kosztuje(self):
#         return self.ilosc*self.cena_jed
# zakupy=NaZakupy('ziemniaki',1,'kg',4)
# print(zakupy.wyswietl_produkt())
# print(zakupy.ile_produktu())
# print(zakupy.ile_kosztuje())

# #zad5
# class CiagArytmetyczny():
#     def __init__(self):
#         self.a1 = None
#         self.r = None
#         self.n = None
#         self.ciag = []
#     def wyświetl_dane(self):
#         for elem in self.ciag:
#             print(elem)
#     def pobierz_elementy(self):
#         while True:
#             element = input("Podaj liczbę lub wpisz 'koniec': ")
#             if element != 'koniec':
#                 self.ciag.append(float(element))
#             else:
#                 break
#     def pobierz_parametry(self):
#         a = input("Wprowadź parametr a: ")
#         self.a1 = int(a)
#         r = input("Wprowadź parametr r: ")
#         self.r = int(r)
#         n = input("Wprowadź parametr n: ")
#         self.n = int(n)
#     def policz_sume(self):
#         return sum(self.ciag)
#     def policz_elementy(self):
#         if (self.a1 is not None) & (self.r is not None) & (self.n is not None): # lub if None not in self.__dict__.values():
#             indeks = 1
#             self.ciag.append(self.a1)
#             while indeks != self.n:
#                 self.a1 += self.r
#                 self.ciag.append(self.a1)
#                 indeks += 1

# #zad6
# class Robaczek:
#     def __init__(self,x,y,krok):
#         self.x=x
#         self.y=y
#         self.krok=krok
#     def idz_w_gore(self,ile_krokow):
#         self.y+=(ile_krokow*self.krok)
#     def idz_w_dol(self,ile_krokow):
#         self.y-=(ile_krokow*self.krok)
#     def idz_w_lewo(self,ile_krokow):
#         self.x-=(ile_krokow*self.krok)
#     def idz_w_prawo(self, ile_krokow):
#         self.x+=(ile_krokow*self.krok)
#     def pokaz_gdzie_jestes(self):
#         return self.x,self.y
# gra=Robaczek(0,0,1)
# print(gra.pokaz_gdzie_jestes())
# gra.idz_w_prawo(5)
# gra.idz_w_gore(10)
# print(gra.pokaz_gdzie_jestes())
# gra.idz_w_lewo(15)
# gra.idz_w_dol(50)
# print(gra.pokaz_gdzie_jestes())