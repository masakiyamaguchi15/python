array = ['ai','baby','cake','doll','egg']
key = input('key=>')

# ここから
result = False
for e in array:
    if key == e:
        result = True
        break
# ここまで
print(result)

# 次の書式でもOK
if result == True:
#if result:
    print('Found')
else:
    print('Not Found')