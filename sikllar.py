#siklar ustida amallar 1 daraja 1dan 10 gacha bolgan sonlarni chiqarish
# Bo'sh list yaratamiz
sonlar = []

# for tsikli orqali 1 dan 10 gacha sonlarni listga qo'shamiz
for i in range(1, 11):
    sonlar.append(i)

# Natijani chop etamiz
print(sonlar) 

# siklaar ustida amallar 2 daraja 5 marta "tur pedaraz" sozini yozish
i = 1
while i <= 5:
    print("tur pedaraz")
    i += 1

# Sikl ustida amallar 3 daraja 1 Dan 100 gacha juft va tqb sonlarni chiqarish
juft = []
toq = []
for i in range(1, 101):
    if i % 2 == 0:
        juft.append(i)
    else:
        toq.append(i)
print(juft)
print(toq)

#sikllar ustida amallar 4 daraja 10 Dan 1 gacha teskari smash
teskari_sanoq = []
#yangi list ochvolamiz
for i in range(10, 0, -1):
    
    #har bir sonni yangi listga joylaymiz
    
    teskari_sanoq.append(i)
print(teskari_sanoq)

#sikllae ustida amallar 5 daraja listdagi sonlar yigindisini topish sum ishlatmasdan
nums = [4, 6, 8, 12]

#total = 0 bilan boshlaymiz.shunda har bir sonni 0 GA qoshadi
total = 0

#for funksiyasi orqali sonlarni har biriga aylantirib qoshamiz
for n in nums:
        total += n
print(total)

#sikllar ustida amallar 6 daraja sonni faktarialini topamiz
n = 5

#result = 1 Dan boshlaymiz.1 Dan n gacha kopaytirib boramiz
result = 1
for i in range(1, n + 1):
        result *= i
print(result)

#sikllar ustida amallar 7 daraja Fibonacci ketmaketligi n ta element uchun
n = 50
a, b = 0, 1
fib = []
for i in range(n):
        fib.append(a)
        a, b = b, a + b
print( fib[-1])

#sikllar ustida amallar 8 daraja 1 Dan n gacha bolgan juft va toq sonlarni topish

#alohida list yaratib olamiz
positive = []
negative = []

#n sonni kiritamiz
n = 60

#har bir son uchun for sikli boyicha bolivchilarni tekshiramiz
for i in range(1, 51):
            if i % 2 == 0:
                positive.append(i)
            else:
                negative.append(i)
print(positive)
print(negative)

#sikllar ustida amallar 9 daraja ikki olchamli list matritsa chiqarish
matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]
for row in matrix:
            for col in row:
                print(col)
                
#sikllar ustida amallar 10 daraja while sikli yordamida sonni topish oyini yaratish
import random
secret = random.randint(1, 100)
guess = 0
while guess != secret:
            guess = int(input("Sonni kiriting"))
            if guess > secret:
                print("Kichikroq son. Yana uruning.")
            elif guess < secret:
                print("Kattaroq son. Yana uruning.")
print("Tabrikliman! Topdingiz! 🎉🎉🎊🎊")
            



        


