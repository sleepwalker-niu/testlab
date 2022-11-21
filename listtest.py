# e=[1]
# print(e)
# e.append(2)
# print(e)
def test1():
    global a
    global b
    a.append(7)

    print(a,b)
    b = a[:]
    print(a,b)


def test2():
    a = []
    b = []

    test1()



test2()




