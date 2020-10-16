def main():
    n = int(input())
    m = len(str(n))
    def dfs(A):
        # nよりも大きくなったら0を返す
        if int(A) > n:
            return 0
        # 入力されたものが七五三数ならcnt=1としていく
        cnt = 1 if all(A.count(c) > 0 for c in '753') else 0
        # 実際に用件を満たすような文字列の出力
        if cnt == 1:
            print(A[1:])
        for i in '753':
            cnt += dfs(A + i)
        return cnt
    print('入力値', n, 'の753数は', dfs('0'))
if __name__ == '__main__':
    main()