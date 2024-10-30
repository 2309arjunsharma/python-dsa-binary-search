def searchRange(nums, target):
    # Implement your solution here
    def First(nums,target):
        l,r=0,len(nums)-1
        result=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                result=mid
                r=mid-1
            elif nums[mid]<target:
                l=mid+1 
            else:
                r=mid-1
        return result
    def Last(nums,target):
        l,r=0,len(nums)-1
        result=-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                result=mid
                l=mid-1
            elif nums[mid]<target:
                l=mid+1 
            else:
                r=mid-1
        return result
    start=First(nums,target)
    end=Last(nums,target)
    return  [start,end]
lst=[5,7,7,8,8,10]
result=searchRange(lst,8)
print(result)
lst1=[5,7,7,8,8,10]
result1=searchRange(lst1,6)
print(result1)
