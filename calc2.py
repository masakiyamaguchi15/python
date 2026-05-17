print('【Menu】 1.加算　2.減算　3.乗算　4.除算　q.終了')
while True:
    flag=input('=>')
    
    if flag =='q':
        break
    
    if flag !='q' and flag !='1' and flag !='2' and flag !='3' and flag !='4':
        print('Message Error: 1～4の数字を入力してください。')
        
    if flag == '1' or flag == '2' or flag == '3' or flag == '4':
        op1=int(input('１つ目の数は？'))
        op2=int(input('２つ目の数は？'))

    if flag=='1':
        answer=op1+op2
        print('答えは',answer,'です。')
    elif flag=='2':
        answer=op1-op2
        print('答えは',answer,'です。')
    elif flag=='3':
        answer=op1*op2
        print('答えは',answer,'です。')
    elif flag=='4':
        answer=op1/op2
        print('答えは',answer,'です。')
