import math
print("Hello\ndoge","\n")
print("123",end="")
print(456)
x = 42
print(f"Value of x is {x}")
mathScores = [60,70,10,20,81,63,4]
firstItem = f"first item in mathScore is {mathScores[0]}"

for i in range(len(mathScores)):
    print(i,mathScores[i])
for i in mathScores:
    print(i)
family={"dad":"Homer","mom":"Marge","son":"Bard"}
for member in family.items():
    print(member)
[print(i) for i in mathScores]
[print(math.sqrt(i)*10) for i in mathScores]
#while
count = 0
while count <10:
    print(count,end="")
    count+=1
for score in mathScores:
    if score>80:
        break
    print(score)
#99乘法表
import random
r = random.randint(1,50)
print(r)
for a in range(1,10):
    for b in range (1,10):
        print(f"{a}*{b}={a*b}")
#哈囉五十次之後說我說完了拉
asd=1
while asd!=50:
    print("哈囉",end="")
    asd+=1
print("我說完了拉")
#輸入一個值後出現他前面的所有奇數
numbers=eval(input("輸入一個數產生所有奇數:"))
for i in range(numbers):
    if i%2 == 1:
        print(i,end=" ")
#隨機4X3陣列
column=eval(input("輸入欄數:"))
rows=eval(input("輸入列數:"))
sum=0
for r in range(rows):
    for c in range(column):
        asdf=random.randint(0,101)
        print(asdf,end=" ")
        sum+=asdf
    print("")
#計算陣列所有元素的總和
print(sum)
#創造兩個3X3的矩陣，將兩個矩陣相加後列出
for rounder in range(2):
    for i in range(3):
        for j in range(3):
            ting=random.randint(0,101)
            print(ting,end=" ")
        print()
    print()
print()


