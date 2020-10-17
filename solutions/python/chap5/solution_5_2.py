def main():
    n, w = map(int, input().split())
    a = [int(x) for x in input().split()]
    # dp[i+1][j]はi番目(indexにおいて)までの整数の中からいくつか選んで総和jにできるかという意味
    # dp[3][2]ならaの2番目(indexにおいて)までの整数の中からいくつか選んで合計が2になるなら1とする
    # dpの枠の用意(indexとn, wを合わせるので+1する)
    dp = [[0] * (w+1) for _ in range(n+1)]
    # dpの初期値(0個から0は作れるので)
    dp[0][0] = 1
    # ２重のfor文でO(nw)
    for i in range(n):
        for j in range(w+1):
            if dp[i][j]:
                dp[i+1][j] = dp[i][j]
            if j >= a[i] and dp[i][j-a[i]]:
                    # a[i]を選んで成立するには
                    # dp[i][j-a[i]]がTrueである必要がある
                    dp[i+1][j] = dp[i][j-a[i]]
                    print(i+1, '個目までの整数のいくつかで', j, 'が作れるか')
                    print('選ぶ', dp)
    if dp[n][w]:
        print('Yes')
    else:
        print('No')
    print('forの回転数は', (i+1) * j)
    print('n x w　は', n * w)
    
if __name__ == '__main__':
    main()