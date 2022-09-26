def Knapsack_ilimitado(W, n, val, p):
    li = []
    dp = [0 for i in range(W + 1)]
    for i in range(W + 1):
        for j in range(n):
            if (p[j] <= i):
                if max(dp[i], dp[i - p[j]] + val[j]) == dp[i - p[j]] + val[j]:
                    li.append(val[j])
                dp[i] = max(dp[i], dp[i - p[j]] + val[j])
    return dp[W]

def main():
    val = [2, 6, 8, 9, 10, 17, 17, 20]
    p = [1, 2, 3, 4, 5, 6, 7, 8]
    W = 4
    
    n = len(val)

    lucro_max = Knapsack_ilimitado(W, n, val, p)
    print("Lucro máximo de corte do fio: " + str(lucro_max) + " reais")

if __name__ == "__main__":
    main()
