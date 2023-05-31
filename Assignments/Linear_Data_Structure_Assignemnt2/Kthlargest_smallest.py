class smallest_largest:
    def __init__(self,*data):
        self.array=list(data)

    def kthSmallest(self,K):
        ascending=sorted(self.array)

        return ascending[K - 1]

    def kthLargest(self,K):
        descending=sorted(self.array,reverse=True)

        return descending[K-1]



x=smallest_largest(1,4,6,2,8,3,5)
K=3
smallest=x.kthSmallest(K)
largest=x.kthLargest(K)

print("K'th smallest element is",
          smallest)
print("K'th largest element is",
          largest)