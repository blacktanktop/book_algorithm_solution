def main():
    def tribo_list(n):
        d = [0] * (n+1)
        # d[0]とd[1]とd[2]を規定。
        d[0] = 0
        d[1] = 0
        d[2] = 1
        # 3~nまでを見る必要がある
        for i in range(3, n+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
        return d
    def tribo_rec(n):
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 1
        ans = tribo_rec(n-1) + tribo_rec(n-2) + tribo_rec(n-3)
        return ans
    print('0以上の整数を標準入力するとTribonacci sequenceを出力する')
    n = int(input())
    if n >= 0:
        print('Tribonacci list', tribo_list(n))
        # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149,
        #  274, 504, 927, 1705, 3136, 5768, 10609, 19513,
        #  35890, 66012, 121415, 223317, 410744, 755476]
        # 項数は0から始まる
        print('再帰によるTribonacci sequenceの第', n, '項の計算の値：', tribo_rec(n), sep='')
        # 755476
    else:
        print('0以上の整数を標準入力するとTribonacci sequenceを出力する')
    
if __name__ == '__main__':
    main()