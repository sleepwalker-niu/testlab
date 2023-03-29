import os
import xml.dom.minidom as mainfunc

path='/home/nrz/VOCdevkit/VOC2012/Annotations'
savepath='/home/nrz/VOCdevkit/VOC2012/Annotations'
files=os.listdir(path)
print(len(files))
for xml in files:
    dom= mainfunc.parse((os.path.join(path,xml)))
    root=dom.documentElement
    pathNode=root.getElementsByTagName('difficult')
    j=len(pathNode)
    for i in range(j):
        pathNode[i].firstChild.data="0"
        with open(os.path.join(savepath,xml),'w',encoding='utf8') as fh:
            dom.writexml(fh)