import os
targetfile= '/home/nrz/daduriver工作文件/rgb2gray_input/dataset_9_8_sixspecies/labels/val/' #'/home/nrz/daduriver工作文件/dataset_7_26_onlyfish/labels/val/'

txtlist=os.listdir(targetfile)
b=[]

for txtfile in txtlist:
    b.clear()
    e=open(os.path.join(targetfile,txtfile),'r')
    while True:
        _=e.readline()
        if _:
            b.append(_.split())
        else:
            break
    e.close()
    print(b)

    e = open(os.path.join(targetfile, txtfile), 'w+')
    for i in range(len(b)):
        if b[i][0] != '0':
            b[i][0] ='0'
        # elif b[i][0] == '3':
        #     b[i][0] ='3change0'
    print(b)
    for i in b:
        e.writelines(' '.join(i)+'\n')
    e.close()







