def main():
    # 入力受け取り
    N = int(input())
    a = [int(x) for x in input().split()]
    cnt = 0
    # aがすべて2で割り切れている（全部Trueなら回り続ける）
    while all([True if i % 2 == 0 else False for i in a]):
        cnt += 1
        a = [i / 2 for i in a]
    print(cnt)
if __name__ == '__main__':
    main()