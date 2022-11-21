path='test.txt'

f=open(path,'r')

lists=f.read().splitlines()
for i in lists:
    each_line_split=[]
    each_line_split=i.split(',')
    print(each_line_split)
print(lists)
