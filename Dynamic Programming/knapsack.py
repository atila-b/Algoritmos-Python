def Knapsack_ilimitado(W, n, val, p):
    dp = [0 for i in range(W + 1)]
    for i in range(W + 1):
        for j in range(n):
            if (p[j] <= i):
                dp[i] = max(dp[i], dp[i - p[j]] + val[j])
    return dp[W]

def main():
    W = 100
    val = [10, 30, 20]
    p = [5, 10, 15]
    n = len(val)
    
    valor_max = Knapsack_ilimitado(W, n, val, p)
    print("Valor máximo da mochila : " + str(valor_max))

if __name__ == "__main__":
    main()
