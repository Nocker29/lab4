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

