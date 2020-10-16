def main():
    
    def f_memo(i, w, A):
        if i == 0:
            if w == 0:
                return True
            else:
                return False
        # すでにメモに計算結果がが合ったらそのメモの値を返す        
        if memo[i][w] != -1:
            # print('メモ利用', 'i=', i, 'w=', w, 'A[i]=', A[i])
            return memo[i][w]
        if f_memo(i-1, w, A):
            memo[i][w] = True
            print('i =', i, 'w =', w, 'A[', i-1, ']=', A[i-1], 'を選ばない')
            return memo[i][w]
        if f_memo(i-1, w-A[i-1], A):
            memo[i][w] = True
            print('i =', i, 'w =', w, 'A[', i-1, ']=', A[i-1], 'を選ぶ')
            return memo[i][w]
        memo[i][w] = False
        return memo[i][w]

    n, w = map(int, input().split())
    a = [int(x) for x in input().split()]
    # 1つのリストの要素数がw, それがn個ある多重リスト
    memo = [[-1]*(w+1) for _ in range(n+1)]
    if f_memo(n, w, a):
        # print(memo)
        print('Yes')
    else:
        # print(memo)
        print('No')

    # def f_rec(i, w, A):
    #     if i == 0:
    #         if w == 0:
    #             return True
    #         else:
    #             return False
    #     if f(i-1, w, A):
    #         return True
    #     if f(i-1, w-A[i-1], A):
    #         return True
    #     return False
    # n, w = map(int, input().split())
    # a = [int(x) for x in input().split()]
    # if f(n, w, a):
    #     print('Yes')
    # else:
    #     print('No')

if __name__ == '__main__':
    main()