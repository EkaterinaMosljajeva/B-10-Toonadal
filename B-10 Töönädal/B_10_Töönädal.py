from moodul import *

paevad=["Esmaspaev","Teisipaev","Kolmapaev","Neljapaev","Reede"]
tundide_arv=[]

nadal(paevad,tundide_arv)
try:
    while True:
        menu=int(input("\nValik:\n1-Näita nädalapäevad ja tunnid\n2-Kõige rohkem/väiksem tundide arv\n3-Tundide arv nädalas\n4-Nädala palgad\n5-Keskmine tundide arv päevas\n"))
        if menu==0:
            break
        elif menu==1:
            paev_tund(paevad,tundide_arv)
        elif menu==2:
            max_min(paevad,tundide_arv)
        elif menu==3:
            tund_nadal(paevad,tundide_arv)
        elif menu==4:
            tunnipalk(paevad,tundide_arv)
        elif menu==5:
            keskmine(paevad,tundide_arv)
        else:
            print("Vale väärtus")
except:
    print("Vale Andmetüüp")