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

# #zad5
# class ciagi_arytmetyczne:
#     def __init__(self,ciag):
#         self.ciag=ciag
#         self.a1=''
#         self.r=''
#     def wyswietl_dane(self):
#         return self.ciag
#     def pobierz_parametry(self,a1,r,ilosc):
#         self.a1=a1
#         self.r=r
#         self.ilosc=ilosc
#     def policz_sume(self):
#         suma=0
#         for x in range(0,len(self.ciag),1):
#             suma+=self.ciag[x]
#         return suma
#     def policz_elementy(self):
#         if (self.a1!='' & self.r!=''):
#             return len(self.ciag)
#         else:
#             return 'Nie ma podanych a1 i r'
# ciag=[1,3,5,7,9]
# ciagi=ciagi_arytmetyczne(ciag)
# print(ciagi.policz_sume())
# print(ciagi.policz_elementy())
# ciagi.pobierz_parametry(1,2,5)
# print(ciagi.policz_elementy())

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