from module1 import *
ikood=""
while True:
    ikood=input("Sisesta isikood: ")
    if pikkus(ikood)==False:
        print("Liiga pikk või lühike isikukood")
    else:
        s=sugukontroll(ikood)
        if s=="viga":
            print("Eesimene täht ei ole õige")
        else:
            print(s)
            if sünnipäev(ikood)=="viga":
                print("2-7 tähed on valesti sisetatud")
            else:
                lause(ikood)
              