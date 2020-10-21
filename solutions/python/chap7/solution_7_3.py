def main():
    n = int(input())
    dt = [list(map(int, input().split())) for _ in range(n)]
    # O(nlogn)
    dt_s = sorted(dt, key=lambda x: x[1])
    print('bを基準にソート')
    print(dt_s)
    d_sum = 0
    # O(n)
    for d, t in dt_s:
        d_sum += d
        print('仕事時間の合計:', d_sum, 'この仕事の締め切り:', t)
        if d_sum > t:
            print('No')
            exit()
    print('Yes')
if __name__ == '__main__':
    main()