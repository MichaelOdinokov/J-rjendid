#Самостоятельная работа
spisok=[]
l=["Kapibara"]
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
            l_list.index
            print(l_list)

    elif valik==10:
        g=lambda g:g[0]
        l_list.sort(key=g)
        for i in l:
            print(i)
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
