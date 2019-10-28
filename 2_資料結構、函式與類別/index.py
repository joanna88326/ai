'''
# 資料結構
1. list：串列，若有大量資料可以使用，避免宣告過多變數, len, *n, min, append, reverse
2. tuple：元組，結構與串列相同，但值和個數都不能改變，效能較佳
3. set：集合，不重複 set([1, 3, 4, 5, 4, 1])
4. dict：字典，使用 key-value  len, clear, copy, get, items, keys, values
'''
'''
1.list串列: 用[],可改變値跟個數
'''
students = ['Amy', 'Leo', 'Jack']
print(students)
print(students[2])
print(students[1:3]) #從1開始到3終止(不含3)
'''
那事實上在 Python 裡面有滿多可以去使用的工具，我們來 run 一次看看
就是 Lulu 跟 Amy，也就是說呢它是從  1 開始然後 到 3 是中止
那就是說不含 3 啦，
所以說 0 1 2 3
就是 Lulu 跟 Amy
就不含這個 3 的結尾

'''
print(len(students))#取得陣列長度
students.append('Lucy')#增加一個値在陣列後面
print(students)

'''
2.tuple元組: 用(),値跟個數不可改變,效能較好
'''

students1 = ['Tony', 'LuLu', 'Amy', 'Jack']
students2 = ('Tony', 'LuLu', 'Amy', 'Jack')

students1[0] = 'Leo'
#students2[0] = 'Leo'
print(students1)
print(students2)
'''
以上，我們就發現 tuple 這邊發現錯誤 就是說
它沒辦法再給定值了  就是說它是不能修改的
值和個數都是不能修改的
這是 tuple 的一個特性
那這樣的話比起 list 它有一個好處就是說 它的效能比較佳
那 另外一個好處就是說
它可以避免一些 side effect → 你希望你的內容是不要被修改到的話
'''

'''
3. set集合: 用([ ]),不重複
'''
new_set = set([1, 3, 4, 12, 3, 4]) # set 處理重複的資料
print(new_set) #{1,3,4,12}

'''
4. dict字典: 用{ },元素名稱為字串,,{元素名稱:値}
'''

student = {
  'name': 'newmedia',
  'age': 20
}

print(student['name'])  #newmedia
print(student['age'])   #20
print(student.keys())   #dict_keys(['name', 'age'])
print(student.values()) #dict_values(['newmedia', 20])
print(student.items()) 
 #  得到的內容
 #  dict_items([('name', 'newmedia'), ('age', 20)]) 裡面是 tuple

print(student.get('name', 'YES')) #newmedia 
print(student.get('namFe', 'YES')) #YES

'''
get 的好處是說
你後面可以放一些 default 值
那如果說你這個 key 如果沒有的話
事實上可以去裡面加 default 值
像是這邊 我們來輸入一下
YES
也就是說當我們這個
key 不存在的時候 我們先故意把它寫錯
它就回傳後面這個 default 值回來

'''


'''
# 迴圈
1. for：固定次數
for else, break, continue
2. while：不確定次數
'''


for student in students:
  print(student)
  # Amy
  # Leo
  # Jack


result = 0

while(result < 10):
  result += 1 # result = result + 1
  print(result)

'''
# 函式
將程式拆解成一個個小單元，方便維護和分工。函式是一種抽象，對流程的抽象
Python 裡面函式叫 def
自建函式


def function_name(*args):
  return args

1. 全域變數
2. 區域變數

global

內建函式
len(x)、round(x) range(x)
'''
#自建函式(有傳入參數)
def add(a, b):
  return a + b

c = add(1, 5)

print(c)

'''
def mutiple(e, f):
  return e * f

g = mutiple(2, 5) #call function

print(g)
'''
'''
call function 就是說你去呼叫這個函式的名字
那有可能你是沒有傳參數進去的
也有可能是你需要傳參數進去
這都不一定 主要是看你的函式怎麼定義的

'''
#自建函式(沒有傳入參數)
def hello():
  print('hello world')

hello()



# 1. 全域變數 2. 區域變數

w = 12  # 全域變數

def mutiple(r, s):
  #print(w)#找不到w,print不出來

  #global w #用這個把區域變數變成全域變數
  w = 13  # 區域變數  區域變數只存活在整個 function 之內
  print(w)

  return r * s

t = mutiple(3, 5) #call function

print(t)
print(w)


print(len([1, 2])) #取得串列長度
# len 一個串列
# 那我想要它的長度 
# 我們要 print 一個
# 這樣的話就是 2
# 因為串列長度是 2

print(list(range(0, 5)))#從0開始到5終止(不含5)
# range
# 這一個提供我們 一個依序的整數
# 那我們這邊 print 要把它轉成 list 才看得出來
# 它就會印出 0 1 2 3 4
# 依序的一個整數 不含 5
# 這個是結尾不含




'''
Class 類別
當某些狀態與功能需要黏在一起時使用類別
類別就像一個鬆餅機一樣可以基於鬆餅類別（class）製作出一個個鬆餅實例（instance）

類別一般會定義 data attribute, data method

繼承

妙蛙種子
小火龍
傑尼龜

bulbasaur
charmander
squirtle

class Pokemon:
  def __init__(self, name):
    self.name = name
    
  def eat(self):
    print('yani yami')

class Charmander(Pokemon):
    def __init__(self, name):
      self.name = name
    def fire(self):
      print('fire!!!')
    
bulbasaur = Pokemon('妙蛙種子')
bulbasaur.eat()
print(bulbasaur.name)

squirtle = Pokemon('傑尼龜')
squirtle.eat()
print(squirtle.name)

class Charmander(Pokemon):
  def __init__(self, name):
    super().__init__(name)
  def fire(self):
    print('fire!!!')  
    
charmander = Charmander('小火龍')
charmander.fire()
print(charmander.name) 
'''

class Pokemon:
  def __init__(self, name):
    self.name = name
  def eat(self):
    print('yami yami')


bulbasaur = Pokemon('妙蛙種子') 
bulbasaur.eat()
print(bulbasaur.name)

squirtle = Pokemon('傑尼龜')
squirtle.eat()
print(squirtle.name)

   
class Charmander(Pokemon):
  def __init__(self, name):
    super().__init__(name)
  def fire(self):
    print('fire!!!') 


charmander = Charmander('小火龍')
charmander.eat()
charmander.fire()
print(charmander.name) 

'''
來談一個比較進階的議題  就是說我今天
要宣告一個叫做小火龍的類別
就是說我希望製造出一堆小火龍

我們要繼承的是 pokeomon
就是說我希望能夠繼承
這個 pokemon 所有的屬性跟方法
接著我們來製作我們這個小火龍的製造機
小火龍的 class

那這邊呢 它事實上已經繼承了 pokemon 的屬性跟方法
我們需要把它 initial 一下
我們這邊也有一個自己的 initial
我們這邊把 name 傳進來
我們這邊使用一個叫 super   super會呼叫我們 pokemon 這個 繼承的
initial 

'''
   
