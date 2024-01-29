class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = len(nums1)
        b = len(nums2)
        k = 0

        if (a + b) % 2 == 0:
            k = 1
        
        aleft = 0
        aright = a

        bleft = 0
        bright = b

        for i in range(((a+b)//2)-k):
            if aleft == aright:
                bleft += 1
                bright -= 1
            elif bleft == bright:
                aleft += 1
                aright -= 1
            else:
                if nums1[aleft]<=nums2[bleft]:
                    aleft += 1
                else:
                    bleft += 1
                
                if aleft == aright:
                    bright -= 1
                elif bleft == bright:
                    aright -= 1

                else:
                    if nums1[aright-1]>= nums2[bright-1]:
                        aright -= 1
                    else:
                        bright -= 1
        
        if (a + b) % 2 == 0:
            if aright - aleft == 2:
                return (nums1[aleft]+nums1[aright - 1])/2
            elif bright - bleft == 2:
                return (nums2[bleft]+nums2[bright - 1])/2
            else:
                return (nums1[aleft]+nums2[bleft])/2
        else:
            if aright - aleft == 1:
                return nums1[aleft]
            else:
                return nums2[bleft]