from bisect import bisect_right

def main():
    n, k = map(int, input().split())
    A = [int(x) for x in input().split()]
    B = sorted([int(x) for x in input().split()])
    def check(x):
        # x以下の積の数がK個以上
        # a*b <= k　は b <= k//a
        cnt = 0
        for a in A:
            cnt += bisect_right(B, x // a)
        return cnt >= k
    # a. b の最大が10**9
    l = 0
    r = 10**18 + 1
    while r - l > 1:
        m = (r + l) // 2
        # m以下の積の数がK個以上ならmを右端に（現状のmより左側に答えが）
        if check(m):
            r = m
        # m以下の積の数がK個未満ならmを左端に（現状のmより右側に答えが）
        else:
            l = m
    # 全パターンを順番に並べた
    print('全パターンを順番に並べると')
    print(sorted(a * b for a in A for b in B))
    # 最後は右を答える
    print('小さい方から', k, '番目の値', r)
            
if __name__ == '__main__':
    main()