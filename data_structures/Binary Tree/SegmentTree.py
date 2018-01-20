from __future__ import print_function
import math

class SegmentTree:
    
    def __init__(self, N):
        self.N = N
        self.st = [0 for i in range(0,4*N)] # approximate the overall size of segment tree with array N
        
    def left(self, idx):
        return idx*2

    def right(self, idx):
        return idx*2 + 1

    def build(self, idx, l, r, A):
        if l==r:
            self.st[idx] = A[l-1]
        else :
            mid = (l+r)//2
            self.build(self.left(idx),l,mid, A)
            self.build(self.right(idx),mid+1,r, A)
            self.st[idx] = max(self.st[self.left(idx)] , self.st[self.right(idx)])
    
    def update(self, idx, l, r, a, b, val): # update(1, 1, N, a, b, v) for update val v to [a,b]
        if r < a or l > b:
            return True
        if l == r :
            self.st[idx] = val
            return True
        mid = (l+r)//2
        self.update(self.left(idx),l,mid,a,b,val)
        self.update(self.right(idx),mid+1,r,a,b,val)
        self.st[idx] = max(self.st[self.left(idx)] , self.st[self.right(idx)])
        return True

    def query(self, idx, l, r, a, b): #query(1, 1, N, a, b) for query max of [a,b]
        if r < a or l > b:
            return -math.inf
        if l >= a and r <= b:
            return self.st[idx]
        mid = (l+r)//2
        q1 = self.query(self.left(idx),l,mid,a,b)
        q2 = self.query(self.right(idx),mid+1,r,a,b)
        return max(q1,q2)

    def showData(self):
        showList = []
        for i in range(1,N+1):
            showList += [self.query(1, 1, self.N, i, i)]
        print (showList)
            

if __name__ == '__main__':
    A = [1,2,-4,7,3,-5,6,11,-20,9,14,15,5,2,-8]
    N = 15
    segt = SegmentTree(N)
    segt.build(1,1,N,A)
    print (segt.query(1,1,N,4,6))
    print (segt.query(1,1,N,7,11))
    print (segt.query(1,1,N,7,12))
    segt.update(1,1,N,1,3,111)
    print (segt.query(1,1,N,1,15))
    segt.update(1,1,N,7,8,235)
    segt.showData()
