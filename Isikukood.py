from module1 import *
ikood=""
arvud=["100","1001","211","222"]
ikoodid=[]
while True:
    a=input("Kas sa tahad jätkata? jah=ja ei=ei :  ")
    if a=="ja":
        ikood=input("Sisesta isikood: ")
        if ikood=="-":break
        if pikkus(ikood)==False:
            print("Liiga pikk või lühike isikukood")
            arvud.append(ikood)
        else:
            s=sugukontroll(ikood)
            if s=="viga":
                print("Eesimene täht ei ole õige")
            else:
                print(s)
                if sünnipäev(ikood)=="viga":
                    print("2-7 tähed on valesti sisetatud")
                else:
                    print(lause(ikood))
                    if kontrollnr(ikood)==int(ikood[-1]):
                        print("Ok")
                        ikoodid.append(ikood)
                    else:
                        print("!!!")
print()
ikoodid=naised_mehed(ikoodid) 
print(ikoodid) 
arvud=arvud_sorted(arvud)
print(arvud)
