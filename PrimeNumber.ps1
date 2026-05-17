function findPrimeNumbers {
    param (
        [int]$maxNum
    )
    <#
    引数で与えられた整数以下の、全ての素数だけを格納した配列を返す関数。
    ここで、引数に与える整数は2以上である。
    #>
    
    # 要素数0の配列 (Pythonのリストの挙動に合わせ、高速な List を使用)
    $pnList = [System.Collections.Generic.List[int]]::new()
    # i を 2 から maxNum まで 1 ずつ増やす (a = maxNum)
    for ($i = 2; $i -le $maxNum; $i++) {
        $divideFlag = $true
        # iの正の平方根の整数部分が2未満のときは、繰返し処理を実行しない
        $limit = [int][Math]::Floor([Math]::Sqrt($i))
        Write-Host $limit
        # j を 2 から iの正の平方根の整数部分 まで 1 ずつ増やす
        for ($j = 2; $j -le $limit; $j++) {
            if ($i % $j -eq 0) {
                # b = (i % j == 0) または (i が j で割り切れる)
                $divideFlag = $false
                break              # αの行から始まる繰返し処理を終了する
            }
        }
        if ($divideFlag) {
            $pnList.Add($i)
        }
    }
    # PowerShellの仕様で配列が分解されないよう、カンマをつけて一次元配列として返す
    return , $pnList.ToArray()
}
function main {
    # 動作確認 (例: 30以下の素数を求める)
    $result = findPrimeNumbers -maxNum 1000
    
    # 出力 (PowerShellで配列の要素をカンマ区切りにして表示)
    Write-Host "findPrimeNumbers(30): [$($result -join ', ')]"
}
# Pythonの if __name__ == "__main__": main() に相当する実行部分
main