def main():
    # 入力受け取り
    N, v = map(int, input().split())
    a = [int(x) for x in input().split()]
    # 初期化としてあり得ない数値を代入
    found_id = -1
    for i in range(N):
        if a[i] == v:
            found_id = i
    print(found_id)
if __name__ == '__main__':
    main()