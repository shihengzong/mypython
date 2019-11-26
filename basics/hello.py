print('hello python !')

n=10
while 1==1:
    print('请输入姓名: ')
    name = input()
    n-=1
    if name=="exit":
        break
    if name=="张三":
        print('身份正确 !')
        break
    else:
        if n<=0:
            print('验证次数已用完,请明天再试 !')
            break
        else:
            print('身份错误,还剩%d次机会!\n' % n )
            




