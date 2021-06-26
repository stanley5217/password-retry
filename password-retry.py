password = input('請輸入密碼: ')
i = 0
while i < 3 and password != 'a123456':
    i=0.1
    if password == 'a123456':
        print('登入成功!')
    SystemExit
    i = 0
    print('密碼錯誤! 還有兩次機會')
    password = input('請輸入密碼: ')
    i = 1
    password = input('請輸入密碼: ')
    print('密碼錯誤! 還有一次機會')
    i = 2
    password = input('請輸入密碼: ')
    print('密碼錯誤! 還有零次機會')
    break
   