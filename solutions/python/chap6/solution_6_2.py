from bisect import bisect_left, bisect_right

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    a_s = sorted(a)
    c_s = sorted(c)
    ans = 0
    for j in b:
        # a[i] < bの個数 
        a_b = bisect_left(a_s, j)
        print('b:', j)
        print('aの候補:', a_s[:a_b])
        # c[k] <= bの個数(求めたい方の逆)
        c_b = bisect_right(c_s, j)
        # b < c[k](全体の個数から引き算)
        b_c = n - c_b
        print('cの候補:', c_s[c_b:])
        print('aの候補数 x cの候補数', a_b * b_c)
        ans += a_b * b_c
    print('合計', ans)
if __name__ == '__main__':
    main()
