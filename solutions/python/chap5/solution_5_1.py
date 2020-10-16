def main():
    n = int(input())
    abc = [list(map(int, input().split())) for _ in range(n)]
    # dp[i][0or1or2]のような形にして、i+1日目にある行動をした時の最大値という意味
    # dp[3][2]なら4日目にbをした時の最大値
    # dpの枠の用意
    dp = [[0] * 3 for _ in range(n)]
    # dpの初期値
    # 1日目の幸福度
    for i in range(3):
        dp[0][i] = abc[0][i]
    print('初期値(1日目)代入', dp)
    # 2日目以降のdpを代入
    # 当日のある行動の値は、前日の当日の行動でない残りのどちらかの行動 + ある行動の値
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1] + abc[i][0], dp[i-1][2] + abc[i][0])
        dp[i][1] = max(dp[i-1][0] + abc[i][1], dp[i-1][2] + abc[i][1])
        dp[i][2] = max(dp[i-1][0] + abc[i][2], dp[i-1][1] + abc[i][2])
        print(i, '日目の行動を考慮した',  i+1, '日目の行動別最大幸福', dp)
    # dpの最後の値の最大値が幸福度最大
    ans = max(dp[n-1])
    print(n, '日間の幸福度の最大値', ans)

if __name__ == '__main__':
    main()