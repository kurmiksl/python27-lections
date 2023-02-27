i = 1
while i < 10:
    j = 1
    while j < 10:
        print("%4d" % (i * j), end="")
        j += 1
    print()
    i +=1   
# Типы данных. Списки. Цикл for. Таск 3
name_of_list = ['Helloworld!']
new_list = name_of_list[0]
i = len(new_list)
if i % 2 == 0:
    new_list = name_of_list[0][i//2:] + name_of_list[0][:i//2]
else:
    new_list = name_of_list[0][i//2+1:] + name_of_list[0][:i//2+1]
    print(list(new_list)) 
    print(name_of_list[0][i//2:] + name_of_list[0][:i//2])
    print(new_list[i//2:])
    print(new_list[0])
