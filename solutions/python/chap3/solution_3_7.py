def main():
    # 入力受け取り
    s = input()
    n = len(s)
    ans = 0
    # 1 << i　は2進数表現で右からi番目(一番右は0番目)のみ1がである値のことなので
    # 2**iと同義
    # 数文字の間に'+'を入れるかどうかなので2**(n-1)パターンある
    for bit in range(1 << (n-1)):
        formula = s[0]
        # bitの立ち方確認用
        bits = []
        for i in range(n-1):
            bits.append((bit>>i)&1)
            if ((bit>>i)&1) == 1:
                formula += '+'
            formula += s[i+1]
        # 状況確認用
        print('bit確認用：', bits)
        print('式確認用', formula)
        # split sum方式
        # ans += sum(map(int, formula.split('+')))
        # 評価方式
        ans += eval(formula)
    print(ans)
if __name__ == '__main__':
    main()
