class Person:
    def __init__(self, name, height, weight):
        """
        初期化メソッド
        :param name: 氏名
        :param height: 身長 (m)
        :param weight: 体重 (kg)
        """
        self.name = name
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        """
        BMIを算出し、戻り値として返すメソッド
        :return: BMI値 (浮動小数点数)
        """
        # BMI = 体重 / 身長の2乗
        bmi = self.weight / (self.height ** 2)
        return bmi

# --- 動作確認用のコード ---
# インスタンスの生成 (例: 山田さん 身長1.75m, 体重68kg)
p1 = Person("山田", 1.75, 68.0)

# BMI算出メソッドの呼び出し
bmi_value = p1.calculate_bmi()

print(f"{p1.name}さんのBMIは {bmi_value:.2f} です。")