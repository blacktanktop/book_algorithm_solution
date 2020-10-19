from bisect import bisect_left

def main():
    def binary_search(list, n):
        # 左右のindexで考える
        l = 0
        h = len(list) - 1
        flag = False
        while l <= h:
            mid = (l+h) // 2
            tmp = list[mid]
            if n == tmp:
                flag = True
                break
            elif tmp < n:
                l = mid + 1
            elif tmp > n:
                h = mid - 1
        return mid
    
    a = [int(x) for x in input().split()]
    # 二分探索するためにソート
    a_s = sorted(a)
    print('ソートされたa', a_s)
    for i in a:
        print('i', i)
        print('（index的に）何番目に小さいか(自作関数)', binary_search(a_s, i))
        print('（index的に）何番目に小さいか（組み込み関数）', bisect_left(a_s, i))
if __name__ == '__main__':
    main()