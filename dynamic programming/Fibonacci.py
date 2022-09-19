class Fibonacci:

    def fibo(self, n: int):
        if n <= 2:
            return 1
        return self.fibo(n-1) + self.fibo(n-2)


    # Memoization
    def fibo_memo(self, n: int, memo={}):
        if n in memo.keys():
            return memo[n]
        if n <= 2:
            return 1
        memo[n] = self.fibo_memo(n-1, memo) + self.fibo_memo(n-2, memo)
        return memo[n]

    # Tabularization
    def fibo_tabu(self, n: int):
        table = [0,1]
        for i in range(2, n+1):
            table.append(table[i-1] + table[i-2])
        
        return table[-1]
