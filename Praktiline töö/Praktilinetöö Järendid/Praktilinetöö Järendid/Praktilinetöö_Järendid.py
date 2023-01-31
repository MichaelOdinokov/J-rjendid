from random import*
#4

print()
#3
arvud=[]
kogus=int(input("Kogus: "))
for i in range(kogus):
    arvud.append(randint(-100,100))
    print(arvud)
    max_arv=max(arvud)
    ind=arvud.index(max_arv)
    print(ind)
max_arv=round(max_arv/kogus,2)
arvud.insert(ind, max_arv)
arvud.pop(ind+1)
print(arvud)
print()
    



#2
s=""
l=["Kot", "Enot", "Belka"]
l_list=list(l)

osa1=[]
osa2=[]
print(l_list)
while True:
    try:
        if len(l)%2==0 and len(l)>=2:
            n=int(len(l)/2)
            for i in range(1, n+1):
                osa1.append(l[i])
            for j in range(n+1, len(l)+1):
                osa2.append(l([j]))
            osa1.revers()
            osa2.revers()
            osa2.extend(osa1)
            print(osa2)
    except:
        print("!!")
        




#1
i=""# i-index
m=["Tallinn", "Narva", "K-Järve", "Ida-Virumaa", "Tartu", "Tartumaa", "Viljandi", "Pärnumaa", "Saarema."]

while True:
    try:
        i=int(input("Anna index: "))
        if i<99999 and i>10000:
            break
    except:
        print("Anna õgie index")
i=i//10000 #1,2,3-9.
print(f"{i} on {m[i-1]}")#0,1-8.
if i in [1,2,3]:
    print("Jätke kodu")
else:
    print("Kanna maske")







