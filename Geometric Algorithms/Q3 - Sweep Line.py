class Ponto:
    def __init__(self, id, x, y, tipo):
        self.id = id
        self.x = x
        self.y = y
        self.tipo = tipo
        self.ordem = None

def mergeSort(arr):
    if len(arr) > 1:
        m = len(arr)//2
        L = arr[:m]
        R = arr[m:]
  
        mergeSort(L)
        mergeSort(R)
        merge(arr, L, R)

def merge(arr, L, R):
    i=j=k=0

    while i < len(L) and j < len(R):
            if L[i].y < R[j].y:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
  
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

class No(object):
    def __init__(self, val, y):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.root = None
        self.arv = AVL2()
        self.y = y

class AVL(object): 
    def insert(self, root, key, y):
        if not root:
            no = No(key, y)
            no.root = no.arv.insert(no.root, y)
            return no
        elif key < root.val:
            root.left = self.insert(root.left, key, y)
        else:
            root.right = self.insert(root.right, key, y)
 
        root.height = 1 + max(self.getHeight(root.left),
                          self.getHeight(root.right))

        balance = self.getBalance(root)
 
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def delete(self, root, key):

        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)
 
        if root is None:
            return root
 
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.getHeight(z.left),
                          self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                          self.getHeight(y.right))
 
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
    
    def busca(self, root, x):
        if root:
            if root.val == x:
                return root
            elif root.val > x:
                return self.busca(root.left, x)
            else:
                return self.busca(root.right, x)

class No2(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
        self.root = None

class AVL2(object):
 
    def insert(self, root, key):
        if not root:
            no = No2(key)
            return no
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
 
        root.height = 1 + max(self.getHeight(root.left),
                          self.getHeight(root.right))

        balance = self.getBalance(root)
 
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
 
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
 
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def delete(self, root, key):

        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key)
 
        elif key > root.val:
            root.right = self.delete(root.right, key)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            root.val = temp.val
            root.right = self.delete(root.right,
                                      temp.val)
 
        if root is None:
            return root
 
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        return root
 
    def leftRotate(self, z):
 
        y = z.right
        T2 = y.left
 
        y.left = z
        z.right = T2
 
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
 
        return y
 
    def rightRotate(self, z):
 
        y = z.left
        T3 = y.right
 
        y.right = z
        z.left = T3
 
        z.height = 1 + max(self.getHeight(z.left),
                          self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                          self.getHeight(y.right))
 
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)

    def busca_menor_igual(self, root, x):
        if root:
            if root.val <= x:
                return root
            elif root.val > x:
                return self.busca_menor_igual(root.left, x)
            else:
                return self.busca_menor_igual(root.right, x)


def sweepLine(P, n):
    mergeSort(P)
    T = AVL()
    root = None
    cont = 0
    for i in range(n):
        no = T.busca(root, P[i].x)
        if P[i].tipo == "inf":
            if no:
                no.root = no.arv.insert(no.root, P[i].y)
            else:
                root = T.insert(root, P[i].x, P[i].y)
        elif P[i].tipo == "sup":
            p = [p for p in P if p.id == P[i].id-1]
            no.root = no.arv.delete(no.root, p[0].y)
            aux = no.arv.busca_menor_igual(no.root, p[0].y)
            if aux:
                cont +=1

    print("Numero de segmentos contidos em outro segmento = " + str(cont))

def print_pontos(P):
    print("*------------------------------------------------------------------------------*")
    for i in range(len(P)):
        if P[i] != None:
            print("Ponto " + str(i+1) + " = x: " + str(P[i].x) + "; y: " + str(P[i].y))

def main():
    print("Imagens do exemplo implementado disponiveis em: https://github.com/atila-b/L6-PAA-images.git")
    p1 = Ponto(1, 3, 2, "inf")
    p2 = Ponto(2, 3, 8, "sup")
    p3 = Ponto(3, 3, 4, "inf")
    p4 = Ponto(4, 3, 7, "sup")
    p5 = Ponto(5, 6, 6, "inf")
    p6 = Ponto(6, 6, 9, "sup")
    p7 = Ponto(7, 8, 3, "inf")
    p8 = Ponto(8, 8, 13, "sup")
    p9 = Ponto(9, 8, 5, "inf")
    p10 = Ponto(10, 8, 11, "sup")
    p11 = Ponto(11, 3, 5, "inf")
    p12 = Ponto(12, 3, 6, "sup")
    p13 = Ponto(13, 6, 5, "inf")
    p14 = Ponto(14, 6, 8, "sup")
    '''
    p1 = Ponto(1, 2, 2, "inf")
    p2 = Ponto(2, 2, 15, "sup")
    p3 = Ponto(3, 2, 5, "inf")
    p4 = Ponto(4, 2, 10, "sup")
    p5 = Ponto(5, 2, 8, "inf")
    p6 = Ponto(6, 2, 20, "sup")
    '''
    P = []
    P.extend([p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14])
    #P.extend([p1, p2, p3, p4, p5, p6])
    print_pontos(P)
    n = len(P)
    sweepLine(P, n)


if __name__ == "__main__":
    main()


