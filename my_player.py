class DVDPlayer:
    def __init__(self):
        self.has_disc = False
        self.is_playing = False
        self.current_disc_name = None

    def insert_disc(self, disc_name):
        if not self.has_disc:
            self.has_disc = True
            self.current_disc_name = disc_name
            print(f"『{disc_name}』を挿入しました。")
        else:
            print("既にディスクが入っています。")

    def play(self):
        # アクティビティ図のロジックを反映
        if not self.has_disc:
            print("エラー：ディスクが入っていません。")
            return
        
        if not self.is_playing:
            print(f"『{self.current_disc_name}』の再生を開始します...")
            self.is_playing = True
        else:
            print("既に再生中です。")

    def pause(self):
        if self.is_playing:
            print("再生を一時停止しました。")
            self.is_playing = False
        else:
            print("再生中ではないため一時停止できません。")

    def stop(self):
        if self.is_playing or self.has_disc:
            print("再生を停止しました。")
            self.is_playing = False
        else:
            print("既に停止しています。")

    def eject_disc(self):
        if self.has_disc:
            print(f"『{self.current_disc_name}』を取り出しました。")
            self.has_disc = False
            self.current_disc_name = None
            self.is_playing = False
        else:
            print("ディスクが入っていません。")

# --- 実行例 ---
my_player = DVDPlayer()

my_player.play()           # ディスクなしでのエラー確認
my_player.insert_disc("Interstellar")
my_player.play()           # 再生
my_player.pause()          # 一時停止
my_player.eject_disc()     # 取り出し