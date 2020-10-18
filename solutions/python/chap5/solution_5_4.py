def main():
    n, w, k = map(int, input().split())
    a = [int(x) for x in input().split()]
    print('w', w)
    print('k', k)
    print('a:', a)
    # dp[i+1][j]はi番目(indexにおいて)までの整数の中からいくつか選んで総和jにできる方法をすべて考えたときに選んだ整数の個数の最小値
    # dpの枠の用意(indexとn, wを合わせるので+1する)
    INF = float('inf')
    dp = [[INF] * (w+1) for _ in range(n+1)]
    # dpの初期値(0個の整数の和は0個なので)
    dp[0][0] = 0
    # ２重のfor文でO(nw)
    for i in range(n):
        for j in range(w+1):
            # a[i]を選ばない場合
            dp[i+1][j] = dp[i][j]
            # a[i]を選ぶ場合
            if j >= a[i]:
                dp[i+1][j] = min(dp[i][j], dp[i][j-a[i]] + 1)
    print('===============================================')
    print(a, 'から', k, '個以下を選んで総和を', w, 'にした時の整数の個数の最小値は', dp[n][w])
    print(a, 'から', k, '個以下を選んで総和を', w, 'にできるか？')
    if dp[n][w] <= k:
        print('Yes')
    else:
        print('No')
    print('===============================================')
    print('forの回転数は', (i+1) * j)
    print('n x w　は', n * w)
if __name__ == '__main__':
    main()