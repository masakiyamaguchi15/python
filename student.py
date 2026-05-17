# Pythonの例
age = 20
is_student = False

if age >= 18:  # 最外側の条件：年齢が18歳以上か
    if is_student:  # 内側の条件：学生かどうか
        print("学生割引が適用されます。") #処理①
    else:
        print("大人料金です。") #処理②
else:
    print("未成年者は入場できません。") #処理③
