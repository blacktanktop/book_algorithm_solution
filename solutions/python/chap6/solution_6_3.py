from bisect import bisect_right

def main():
    # リストからx以下の最大値を得る
    def listmax(l, x):
        return l[bisect_right(l, x)-1]

    n, m = map(int, input().split())
    a = [0] + [int(input()) for _ in range(n)]
    q = sorted({i+j for i in a for j in a})
    print('aから重複（0も）許して２つ選んで足したリスト（qとする）', q)
    # m以下で抑えたいからx <= mの時に
    # qからm-x以下の最大値を得る
    # q = m-xのときはmぴったりになる
    qq = {x + listmax(q, m-x) for x in q if x <= m}
    print('qからmを超えないように2つ選んで足したリスト(qiごとに最大)', qq)
    ans = max(qq)
    print('最大値', ans)
if __name__ == '__main__':
    main()