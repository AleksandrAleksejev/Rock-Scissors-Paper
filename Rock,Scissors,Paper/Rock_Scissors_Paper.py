from random import *
 
b=0; p=0; c=0; d=0; e=0;
game=True
tab=[0]
tab1=[0]
print("********************** Добро пожаловать в игру! **********************")
print("*************************Rock,Paper,Scissors!*************************")
print()
Win=int(input("Выбери число раундов: "))
print()
while game:#Выбор игрока 
        a=int(input("Выбор: 1- Камень, 2- Ножницы, 3- Бумага "))
        print()
        if a==1:
            print("Камень")
            b=1
        elif a==2:
            print("Ножницы")
            b=2
        elif a==3:
            print("Бумага")
            b=3
        else:
            print("Error, выбери число от 1 до 3!")
            print()
        bot=["Камень","Ножницы","Бумага"]#Выбор бота 
        a=randint(1,3)
        if a==1:
          print("Бот выбрал: Камень")
          e=1
        if a==2:
          print("Бот выбрал: Ножницы")
          e=2
        if a==3:
          print("Бот выбрал: Бумага")
          e=3
        if b==e: #нахождение победителя 
          p=0
        if b == 1 and e == 3:
          p=2
        if b == 2 and e == 1:
          p=2
        if b == 2 and e == 3:
          p=1   
        if b == 3 and e == 1:
          p=1
        if b == 3 and e == 2:
          p=2
        if p==0:#Выводим кто победил и выводим счёт
          print("Draw.")
          print("P1:",tab)
          print("Bot:",tab1)
          print()
        if p==1:
          print("You win!")
          schet[0]+=1
          print("P1",tab)
          print("Bot:",tab1)
          print()
        if p==2:
          print("Bot win.")
          schet1[0]+=1
          print("P1:",tab)
          print("Bot:",tab1)
          print()
        if schet==[Win]:
            print("Игра закончена,Ты победил!")
            break
        if schet1==[Win]:
            print("Игра закончена,Бот победил.")
            break



