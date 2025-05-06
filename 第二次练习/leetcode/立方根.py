class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans =0, x, 0
        while l<=r:
            m = (r + l)//2
            if m**3>x:
                r=m-1
            else:
                ans = m
                l=m+1
        return ans

if __name__ == '__main__':
    n = 16
    print(Solution().mySqrt(n))