# Author:Vanyo
# login in commit
import getpass
users = [{'name':'joker','pwd':'coco801314'}]
_user_lock = []
#循环判断userlist中有没有存在的用户与当前输入的用户名密码匹配
#三次机会
i = 0
while i<3:
    #用户输入账号密码
    pass_go = False
    username = input("input your name:")
    password = getpass.getpass("input your password:")
    #判断用户输入的账号是否在锁定账户列表中，如果在就执行
    if username in _user_lock:
        print("this account has been locked for a while")
        break
    #判断用户输入的账号和密码是否匹配
    for user in users:
        if user['name'] == username:
            present_user_name = user['name']
            if user['pwd'] == password:
                pass_go = True
            else:
                #用户名的确存在，判断该情况下用户密码输错是否超出次数
                if i<2:
                    print("your password is wrong，please try again!")
                    #print(i)
                else:
                    _user_lock.append(present_user_name)
                    print("the account: ", present_user_name, "has been locked for a while")
                    #print(_user_lock)
        else:
            print("there is no user named: ",username)
    if pass_go == True:
        print("hello",present_user_name)
        break
    #步长加一，为下次循环做准备
    i +=1