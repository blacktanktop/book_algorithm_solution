def main():
    # 入力受け取り
    N, v = map(int, input().split())
    a = [int(x) for x in input().split()]
    # 線形探索
    cnt = 0
    for i in range(N):
        if a[i] == v:
            cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()