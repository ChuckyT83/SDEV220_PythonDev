class Solution:
    def sort012(self,arr,n):
        arr.sort()
        return arr
    
    def binarysearch(self, arr, n, k):
        arr.sort()
        count = 0
      
        while count <= n:
            if arr[count] == k:
                  return count
            elif count == n - 1:
                  return -1
            else:
                  count = count + 1
print(Solution.sort012(0,[0,2,1,0,2], 5))
print(Solution.binarysearch(0,[0,14,23,4,5,7], 6, 23))