

def nadal(p:list,t:list)->list:
    """Täidab päevade ja tundide nimekirjad
    :param list p: Päevad järjend
    :param list t: Tundi järjend
    :rtype: list, list
    """
    while True:
        try:
            for i in range(len(p)):
                tund=int(input(f"Tundide arv {p[i]}'al:"))
                t.append(tund)
            break
        except:
            print("Vale Andmetüüp")
            t.clear
        

def paev_tund(p:list,t:list)->list:
    """Näitab päevi ja tunde
    :param list p: Päevad järjend
    :param list t: Tundi järjend
    :rtype: list, list
    """
    n=len(p)
    for i in range(n):
        print(p[i], "-", t[i],"tundi")

def max_min(p:list,t:list):
    """Näitab kõige rohkem/vähem tunde ja päeva
    :param list p: Päevad järjend
    :param list t: Tundi järjend
    """
    while True:
        try:
            o=int(input("1 - rohkem, 2 - vähem\n"))
            if o==1:
                tund=max(t)
                ind=t.index(tund)
                paev=p[ind]
                print(f"Kõige rohkem töötati {paev}, {tund} tundi")
                break
            elif o==2:
                tund=min(t)
                ind=t.index(tund)
                paev=p[ind]
                print(f"Kõige vähem töötati {paev}, {tund} tundi")
                break
            else:
                print("Võib olla ainult 1 või 2")
        except:
            print("Vale Andmetüüp")

def tund_nadal(p:list,t:list):
    """Mitu töötundi nädala jooksul
    :param list p: Päevad järjend
    :param list t: Tundi järjend
    """
    summa=sum(t)
    print(f"Inimene on töötanud {summa} tundi nädalas.")

def tunnipalk(p:list,t:list):
    """Arvutage nädala palgad. Küsige tariifi kasutajalt
    :param list p: Päevad järjend
    :param list t: Tundi järjend
    """
    while True:
        try:
            summa=sum(t)
            tp=int(input("Kui palju on tunnipalk? "))
            tp*=summa
            print(f"Nädalapalk võrdub: {tp} eurot")
            break
        except:
            print("Vale Andmetüüp")

def keskmine(p:list,t:list):
    """Arvutab keskmist tundide arvu päevas.
    :param list p: Päevad järjend
    :param list t: Tundi järjend
    """
    kesk=sum(t)/len(p)
    print(f"Keskmine tundide arv: {kesk}")
