class Building:
    def __init__(self, l, h, r):
        self.left = l
        self.right = r
        self.ht = h
    
class Strip:
    def __init__(self, l, h):
        self.left = l
        self.ht = h

def strip_append(arr, strip):
    n = len(arr)
    if n > 0 and arr[n-1].ht == strip.ht:
        return
    if n > 0 and arr[n-1].left == strip.left:
        arr[n - 1].ht = max(arr[n - 1].ht, strip.ht)
        return
    
    arr.append(strip)

def merge(L, R):
    skyline = []
    i = j = 0
    h1 = h2 = 0

    while i < len(L) and j < len(R):
        if L[i].left < R[j].left:
            h1 = L[i].ht
            x1 = L[i].left
            hmax = max(h1, h2)
            strip_append(skyline, Strip(x1, hmax))
            i+=1
        else:
            h2 = R[j].ht
            x2 = R[j].left
            hmax = max(h1, h2)
            strip_append(skyline, Strip(x2, hmax))
            j+=1
        
    while i < len(L):
        strip_append(skyline, L[i])
        i+=1

    while j < len(R):
        strip_append(skyline, R[j])
        j+=1

    return skyline

def Skyline(arr, l, h):
    if l == h:  #caso base
        skyline = []
        strip_append(skyline, Strip(arr[l].left, arr[l].ht))
        strip_append(skyline, Strip(arr[l].right, 0))
        return skyline

    #aplicacao da HI
    m = (l+h)//2
    sk1 = Skyline(arr, 0, m)
    sk2 = Skyline(arr, m+1, h)

    #conquista
    skyline = merge(sk1, sk2)
    return skyline

def print_skyline(arr):
    for i in range(len(arr)):
        print("left: " + str(arr[i].left) + "; height: " + str(arr[i].ht))


def main():
    builds =[[1, 11, 5 ], [2, 6, 7 ], [3, 13, 9 ], [12, 7, 16 ], [14, 3, 25 ], [19, 18, 22 ], [23, 13, 29 ], [24, 4, 28 ]] #exemplo do Udi Manber
    arr = []
    for i in range(len(builds)):
        arr.append(Building(builds[i][0], builds[i][1], builds[i][2]))
    n = len(arr)
  
    print_skyline(Skyline(arr, 0, n - 1))
    return 0

if __name__ == "__main__":
    main()
