def main():
    n, w = map(int, input().split())
    a = [int(x) for x in input().split()]
    print('w', w)
    print('a:', a)
    # dp[i+1][j]はi番目(indexにおいて)までの整数の中からいくつか選んで総和jにできる組み合わせの数
    # dp[3][2]ならaの2番目(indexにおいて)までの整数の中からいくつか選んで合計が2になる組み合わせの数
    # dpの枠の用意(indexとn, wを合わせるので+1する)
    dp = [[0] * (w+1) for _ in range(n+1)]
    # dpの初期値(0個から0は作れるので)
    dp[0][0] = 1
    # ２重のfor文でO(nw)
    for i in range(n):
        for j in range(w+1):
            # a[i]を選ばない場合
            dp[i+1][j] += dp[i][j]
            # a[i]を選ぶ場合
            if j >= a[i]:
                dp[i+1][j] += dp[i][j-a[i]]
    print('===============================================')
    print('0以上', w ,'以下に一致する組み合わせ数のそれぞれの数は', dp[n])
    print('1以上', w ,'以下で作ることができる整数の種類数は', sum([1 for i in dp[n] if i > 0]) - 1)
    print('===============================================')
    print('forの回転数は', (i+1) * j)
    print('n x w　は', n * w)
if __name__ == '__main__':
    main()