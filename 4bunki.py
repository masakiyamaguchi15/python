print('ホットにしますか？ isHot (y/n)')
isHot = input('=>')
print('ミルクをいれますか？ isMilk (y/n)') 
isMilk = input('=>')

if isHot == 'y':
    if isMilk == 'y':
        print('ホットカフェオレ isHot=y,isMilk=y 処理①') 
    else:
        print('ホットコーヒー isHot=y,isMilk=n 処理②') 
else:
    if isMilk == 'y':
        print('アイスカフェオレ isHot=n,isMilk=y 処理③')
    else:
        print('アイスコーヒー isHot=n,isMilk=n 処理④')
