def hanoi(n, x, y, z):
    global num
    if(n==1):
        print(x,'-->',z)
        num+=1
    else:
        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
        print(x,'-->',z)#将第n个从x移动到z上
        num+=1
        hanoi(n-1,y,x,z)#将n-1个盘子从y移动到z上
n = int(input('请输入盘子的数目：'))
num=0
hanoi(n,'x','y','z')
print('共移动',num,'次')
