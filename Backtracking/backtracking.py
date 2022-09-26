def backtracking(n, arr, i, S):
    print(arr)
    if i == n:
        return

    arr2 = []
    for j in range(i, n):
       arr2 = arr + [S[j]] 
       backtracking(n, arr2, j+1, S)


def main():
    S = [1, 5, 9]
    n = 3
    arr = []
    print("S = " + str(S))
    print("Conjunto potencia de S : ")
    backtracking(n, arr, 0, S)

if __name__ == "__main__":
    main()
