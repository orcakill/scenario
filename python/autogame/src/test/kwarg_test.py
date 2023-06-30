# @Time    : 2023年06月30日 11:56
# @Author  : orcakill
# @File    : kwarg_test.py
# @Description : TODO

def cs_test1(s: str, **kwargs):
    print(s)
    print(kwargs)
    cs_test2(s, **kwargs)


def cs_test2(s: str, **kwargs):
    print(kwargs)


if __name__ == '__main__':
    cs_test1("1", tenp=1)
