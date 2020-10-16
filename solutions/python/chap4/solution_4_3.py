import sympy as sym
def main():
    # 一般項f(n)
    fn = sym.simplify("f(n)")
    # 左辺が0になるように漸化式を書く
    y = sym.simplify("f(n)-f(n-1)-f(n-2)")
    # 初期条件
    init = sym.simplify({"f(0)": 0, "f(1)": 1})
    # 初期条件iniの漸化式sをfについて解く
    fib_n = sym.rsolve(y, fn, init)
    print('Fibonacci sequenceの一般項の式は')
    print(fib_n)
    print('------------------------------')
    # -sqrt(5)*(1/2 - sqrt(5)/2)**n/5 + sqrt(5)*(1/2 + sqrt(5)/2)**n/5

    def fib_g(n):
        x = sym.symbols('x', nonnegative=True, integer=True)
        fib = -sym.sqrt(5)*(1/2 - sym.sqrt(5)/2)**n/5 + sym.sqrt(5)*(1/2 + sym.sqrt(5)/2)**n/5
        # fibの式のxにnを代入
        formula = fib.subs(x, n)
        ans = int(sym.simplify(formula))
        print(formula, '=', ans)
        return ans
    print('0以上の整数を標準入力するとFibonacci sequenceの一般項の式と検算結果を出力する')
    n = int(input())
    print('検算結果')  
    print('第', n ,'項までの', 'Fibonacci sequence', [fib_g(n) for n in range(0, n)], sep='')

if __name__ == '__main__':
    main()