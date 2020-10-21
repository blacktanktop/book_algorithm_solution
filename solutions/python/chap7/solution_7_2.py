def main():
    n = int(input())
    red = sorted([list(map(int, input().split())) for i in range(n)], \
        key=lambda x: x[1], reverse=True)
    blue = sorted([list(map(int, input().split())) for i in range(n)])    
    done = dict()
    cnt = 0
    print('最大数の仲良しペアの例は')
    for bx, by in blue:
        for rx, ry in red:
            if (rx, ry) in done:
                continue
            if rx < bx and ry < by:
                print('a:', rx, ry, 'b:', bx, by)
                done[(rx, ry)] = True
                cnt += 1
                break
    print('合計')
    print(cnt)
if __name__ == '__main__':
    main()