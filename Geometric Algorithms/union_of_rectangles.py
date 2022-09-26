class Building:
    def __init__(self, l, h, r, b):
        self.left = l
        self.right = r
        self.ht = h
        self.bt = b
    
class Strip:
    def __init__(self, l, h, b):
        self.left = l
        self.ht = h
        self.bt = b

def strip_append(arr, strip):
    n = len(arr)
    if n > 0 and (arr[n-1].ht == strip.ht  and arr[n-1].bt == strip.bt):
        return
    if n > 0 and arr[n-1].left == strip.left:
        arr[n - 1].ht = max(arr[n - 1].ht, strip.ht)
        arr[n - 1].bt = min(arr[n - 1].bt, strip.bt)
        return
    
    arr.append(strip)

def merge(L, R):
    skyline = []
    i = j = 0
    h1 = h2 = 0
    b1 = b2 = float('inf')

    while i < len(L) and j < len(R):
        if L[i].left < R[j].left:
            h1 = L[i].ht
            b1 = L[i].bt
            x1 = L[i].left
            hmax = max(h1, h2)
            bmin = min(b1, b2)
            strip_append(skyline, Strip(x1, hmax, bmin))
            i+=1
        else:
            h2 = R[j].ht
            b2 = R[j].bt
            x2 = R[j].left
            hmax = max(h1, h2)
            bmin = min(b1, b2)
            strip_append(skyline, Strip(x2, hmax, bmin))
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
        strip_append(skyline, Strip(arr[l].left, arr[l].ht, arr[l].bt))
        strip_append(skyline, Strip(arr[l].right, 0, 0))
        return skyline

    #aplicacao da HI
    m = (l+h)//2
    sk1 = Skyline(arr, 0, m)
    sk2 = Skyline(arr, m+1, h)

    #conquista
    skyline = merge(sk1, sk2)
    return skyline

def calcula_area(skyline, n):
    area = 0
    for i in range(n-1):
        area += (skyline[i+1].left - skyline[i].left)*(skyline[i].ht-skyline[i].bt)
    return area



def print_skyline(arr):
    for i in range(len(arr)):
        print("left: " + str(arr[i].left) + "; height: " + str(arr[i].ht) + "; bot: " + str(arr[i].bt))


def main():
    builds =[[1, 11, 5, 6], [2, 6, 7, 0], [3, 13, 9, 0], [12, 7, 16, 0], [14, 3, 25, 0], [19, 18, 22, 0], [23, 13, 29, 0], [24, 4, 28, 0]] #array de builds
    arr = []
    for i in range(len(builds)):
        arr.append(Building(builds[i][0], builds[i][1], builds[i][2], builds[i][3]))
    n = len(arr)
  
    skyline = Skyline(arr, 0, n - 1)
    print_skyline(skyline)
    print("area da interseccao dos retangulos = " + str(calcula_area(skyline, len(skyline))))
    return 0

if __name__ == "__main__":
    main()
