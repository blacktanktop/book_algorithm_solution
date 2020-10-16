def main():
    # 入力受け取り
    N = int(input())
    a = [int(x) for x in input().split()]
    # 最大・最小を求めて引き算
    # max, minの計算量はO(n)
    maxv = max(a)
    minv = min(a)
    ans = maxv - minv
    print(ans)
if __name__ == '__main__':
    main()