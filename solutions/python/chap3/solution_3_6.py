def main():
    k, n = map(int, input().split())
    cnt = 0
    # 0-kまで探索 
    for x in range(k+1):
        # 0-kまで探索
        for y in range(k+1):
            # z = n - x - yなので0以上k以下ならカウントする
            if 0 <= n - x - y <= k:
                cnt += 1
    print(cnt)
if __name__ == '__main__':
    main()