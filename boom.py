import collections
class Solution(object):
    def numberOfBoomerangs2(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        cnt = 0
        for a, i in enumerate(points):
            dis_list = []
            for b, k in enumerate(points[:a] + points[a + 1:]):
                dis_list.append((k[0] - i[0]) ** 2 + (k[1] - i[1]) ** 2)
            for z in collections.Counter(dis_list).values():
                if z > 1:
                    cnt += z * (z - 1)
        return cnt

val=Solution()
n=int(input())
mat=[]
for i in range(n):
  arr=list(map(int,input().split()))
  mat.append(arr)
print(val.numberOfBoomerangs2(mat))      
