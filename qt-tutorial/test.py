fun_list = []


def test1():
    for i in range(10):
        def fun(index=i):
            print(index)

        fun_list.append(fun)


def test2():
    for i in range(10):
        fun_list.append(lambda i=i: print(i))


if __name__ == '__main__':
    test1()
    for fun in fun_list:
        fun()
    fun_list.clear()
    print("*" * 40)
    test2()
    for fun in fun_list:
        fun()
