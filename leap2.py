print('西暦を入れてください')
year = int(input('=>'))

# yearを400で割って余りが0のときはうるう年
if year%400 == 0:
    print("うるう年です")
elif year%100 == 0 or year%4 != 0:
    print("うるう年ではないです。")
else:
    print("うるう年です。")




