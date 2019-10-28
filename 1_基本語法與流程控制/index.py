'''
# 變數
1. 變數是一個暫時儲存資料的盒子

2. 顧名思義是一個裡面內容是可以『變』的

3. 當我們宣告一個變數時，系統會配置一塊記憶體區塊給它，而因為資料型別（數字、字串）不同，配置大小也有所不同

4. 變數名稱可以使用大小寫字母、數字和 _ 、英文大小寫字母視為不同變數，注意不要使用到 Python 保留字（Ex. if, def）
'''


name = 'Tony'
print(name)
name = 'Lulu'
print(name)

'''
# 資料型別
Python 變數不需要宣告就可以使用，在指定變數值時給定資料型別
input, type, print

1. 數值（包含整數 int 和浮點數 float）：
num1 = 5566
num2 = 12.34 
2. 布林值（True, False）：
isShow = True
3. 字串：
str123 = ‘翟雲’ 
'''
name = input('what is your name?')
#print'what is your name?' 且name是這個的input値
print(name)
#print(type(name))


'''
# 運算式和運算子
指定資料做哪一種運算的是運算子，進行運算的資料稱為運算元

ex.
sum = 1 + 2
print(sum)

1. 算數運算子

+、-、*、/、%、//

result = 13 % 2
print(result)

2. 關係運算子

==、!=、>=、<=、>、<

a = 13
b = 1

3. 邏輯運算子
not、and、or

'''
a = True
b = False
print(a and b)
print(a or b)
print(not a)
'''
4. 賦值運算子
sum = 13

'''
a = 2
a += 1  # a =a +1
print(a)

b = 3
b -= 1
print(b)

b = 3
b **= 2  # b = b ** 2
print(b)
'''

5. 複合指定運算子
+=、-=、*=、/=、%=、//=、**= 次方

若是字串相加則串連字串
'''

'''
# 條件判斷
一般而言程式是循序式執行，
但若有設定條件判斷則會『根據條件』
跳躍執行
1. 單向判斷（if...）

2. 雙向判斷（if...else）

3. 多向判斷（if...elif...else）
'''
age = 17
if age >= 18:
    print('you are adult!!')
else:
    print('you are a kid')


grade = 90

if grade >= 90 and grade < 100:
  print('A')
elif grade >= 80 and grade < 90:
  print('B')
else:
  print('C')


if grade >= 90 and grade < 100:
  print('A')

  
