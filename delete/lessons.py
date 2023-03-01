# Files. Таск 1
file = open('test7.txt') 
for line in file.readlines(9): 
    print(line) 
file.close()

# Files. Таск 2
file = open('test7.txt')
i = file.readlines()
for line in i:
    print(line)
file.close()

# Files. Таск 3
with open('task3.txt', 'a+') as file:
    file.write('0*1*2*3*4*5*6*7*8*9*')
    file.seek(0)
    print(file.read())
# Files. Таск 4
with open('task3.txt','r') as file: 
    print(len(file.readlines()))    
# Files. Таск 5
with open('task5.txt', 'r') as f: 
    list_ = f.readlines() 
    list_ = [line.replace('\n', '')for line in list_] 
    list1 = [] 
    for i in list_:
        i = int(i)
        list1.append(i)
        a = min(list1)
        b = max(list1) 
with open('task6.txt', 'w') as fw:
    fw.write(f'{a}-{b}')
# Files. Таск 6
#def read_last(lines, filename):
    with open(filename) as file:
        list_ = file.readlines()
        if lines < len(list_):
            i = 0 
            reversed_list_ = list_[::-1]
            while i<lines:
                print(reversed_list_[i].replace('\n', '')) 
                i+=1 
        else:
            list_.reverse()
            for i in list_:
                print(i.replace('\n', '')) 
read_last(9, 'article.txt')    
# Files. Таск 7
def longest_words(filename:str): 
    with open(filename,'r') as file:
        listData=file.readlines()
        listData1=[]
        for x in listData:
            if '\n' in x:
                x=x.replace('\n','')
            else:
                pass
                if ' ' in x:
                    var=x.split()
                    listData1.extend(var)
                else:
                    listData1.append(x)
                    maximum=[]
                    for j in listData1:
                        if len(j)==len(max(listData1,key = len)):
                            maximum.append(j) 
                        else:
                            pass
                            if len(maximum)==1:
                                print(maximum[0])
                            else:
                                print(maximum)
longest_words('info.txt')


# JSON. Таск 1
import json
file1 = open('task1.json')
python_obj = json.loads(file1.read())
file1.close()
with open('task1.py', 'w') as file2: 
    file2.write(str(python_obj))
# JSON. Таск 7
import json 
with open('db.json') as file: 
    dict_ = json.load(file) 
    for product in dict_: 
        product["description"] = "..." 
        js_dict = json.dumps(dict_) 
        with open('new_db.json', 'w') as f1: 
            f1.write(js_dict)
# JSON. Таск 6
import json 
json_products = '[{"title":"iphone","price":700,"rating":4.8},{"title":"asus","price":1300,"rating":3.9},{"title":"macbook pro","price":1500,"rating":4.9},{"title":"samsung","price":150,"rating":5.0}]' 
file = json.loads(json_products) 
for x in file: 
    if x["rating"]>4: 
        print(x['title']) 


        
                   