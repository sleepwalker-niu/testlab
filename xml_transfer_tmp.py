import os
import xml.dom.minidom as mainfunc

xmlfile='tmp.xml'


dom= mainfunc.parse(xmlfile)
root=dom.documentElement
pathNode=root.getElementsByTagName('name')
j=len(pathNode)
for i in range(j):
    pathNode[i].firstChild.data="fish"
    with open(xmlfile,'w',encoding='utf8') as fh:
        dom.writexml(fh)