﻿from random import*
#praktiline töö
#6



#5
lists=[['крот', 'белка', 'выхухоль'], ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'], ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']]

def normalize_list(lst):
    max_len = max([len(s) for s in lst])
    return [s.ljust(max_len, '_') for s in lst]
result=[normalize_list(l) for l in lists]
print(result)



print()
#4
numbers=[3, -4, 1, -2, 6, -5]
s_numbers=sorted(numbers, key=lambda x: abs(x)) # сортировка по возрастанию абсолютного значения
print(s_numbers)
s_numbers=sorted(numbers, key=lambda x: abs(x), reverse=True)# сортировка по убыванию абсолютного значения
print(s_numbers)


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

#Самостоятельная работа
spisok=[]
l=["Kapibara", "Kot"]
b=["Belka"]
l_list=list(l)
print(l_list)

while True:
    print("1 - доббавить животное")
    print("2 - добавить белку")
    print("3 - добавить еще животное, на какуюто позицию ")
    print("4 - Разворачивает список ")
    print("5 - Удаляет i-ый элемент и возвращает его. Если индекс не указан.")
    print("6 - Копия списка")
    print("7 - Очищает список")
    print("8 - Удаляет первый элемент в списке, имеющий значение x")
    print("9 - Возвращает положение первого элемента от start до end со значением x")
    print("10 - Сортирует список на основе функции")

    valik=int(input())
    if valik==1:
        a=input("доббавить животное")
        l_list.append(a)
        print(f"{l}", l_list)

    elif valik==2:
        l_list.extend(b)
        print(l_list)

    elif valik==3:
        a=input("Введи ещё одно животное:")
        i=int(input("Введи позиции:"))
        l_list.insert(i-1,a) #0,1,2...
        print(l_list)

    elif valik==4:
        l_list.reverse(l) 
        print(l_list)

    elif valik==5:
        a=int(input("Введи позиции, которую хочешь убрать"))
        if a>=0 and a<len(l_list):
            l_list.pop(a-1)
            print(l_list)
        else:
            print("Ei ole see postion")

    elif valik==6:
        l_list.copy(l)
        print(l_list)

    elif valik==7:
        l_list.clear(l)
        print(l_list)

    elif valik==9:
            index=l.index("Kapibara")
            print(index)


    elif valik==10:
        l.sort(key=lambda x: len(x))
        print(l)

    elif valik==8:
        a=input("Введи , которую хочешь удалить")
        a=a.lower()
        listcopy_list=[]
        for t in (l_list):
            listcopy_list.append(t.lower())
        print(listcopy_list)

        n=l_list.count(a)
        if n>0:
           for i in range(n):
                l_list.remove(a)

        else:
            print("Искомой буквы нет")
        print(l_list)
    


   








spisok=[] #Пустой список
numbers=[1,2,3,4,5]
abc=["A", "B", "C"]
slovo="Programmeerimine"
slovo_list=list(slovo)
print(slovo)
print(slovo_list)

while True:
    print("1-добавить букву в список")
    print("2-склеить список\n3-добавить букву на i - позицию")
    print("4-удалить элемент")
   
    valik=int(input())
    if valik==1:
        a=input("Введи букву")
        slovo_list.append(a) 
        print(f"Добавили {a} новый список", slovo_list)
    elif valik==2:
        slovo_list.extend(abc)
        print(slovo_list)
    elif valik==3:
        a=input("Введи букву, которую хочешь добавить")
        i=int(input("Введи позиции, куда хочешь добавить б"))
        slovo_list.insert(i-1,a) #0,1,2,3,4,5...
        print(slovo_list)
    elif valik==4:
        a=input("Введи букву, которую хочешь удалить")
        n=slovo_list.count(a)
        if n>0:
           for i in range(n):
                slovo_list.remove(a)
        else:
            print("Искомой буквы нет")
        print(slovo_list)
