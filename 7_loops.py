# Циклы
# в пайтоне их только 2
#  оператор while 

# бесконечный цикл можно вырубить команду бесконечной в терминале сочетанием кнопок ctr+C
#while True:
    #print("hello")

# бесконечный цикл с прерыванием
#while True:
 #   val = input("Введите имя:")
 #   if val == "stop":
 #       print("Bye-Bye!")
  #      break
   # print(f"Hello, {val}")


# Цикл с условием
#v0 = 0

#while v0 <= 10:
#    print(f"value = {v0}")
    # инкремент
    #v0 = v0 + 1
    #v0 +=1 (2й вариант, такая же команда)

# print("while is stopped")

#v1 = 10
#while v1 >= -10:
#    print(f"value = {v1}")
    # декремент
 #   v1 -= 2

# пропуск части кода тела цикла
v2 = -5

#while v2 < 15:
#    # 1 кусок кода
#    print(f"value = {v2}")
#    v2 += 1

 #   if v2 < 5:
#        continue

    # 2 кусок кода
#    print("hello")


#  оператор for

# 1. чтение значения обьекта с последовательностью
# 2. считанное значение приваивается в собственную переменную
# 3. выполняет код своего тела

#for v in "python":
#    print(v)

lst0 = [10, 20, 30, 4, 4526, 273468273, 0]

#for val in lst0:
#    val += 100
#    print(val)

# класс range()

r = range(10)
r = range(10, 20)
r = range(-10, 10, 2)

#print(r)

#for num in r:
#    print(num)

#for num in range(10):
#    print(num)

#  безымянная переменная
#for _ in range(5):
#    print("Hello")

dict_0 = dict(a=100, b=200, c=300)

print(dict_0)

#for i in dict_0:
#    print(i)
#
#for i in dict_0.values():
#    print(i)    

#кортежи
for i in dict_0.items():
    print(i)  