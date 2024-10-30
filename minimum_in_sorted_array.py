def findMin(nums):
    # Implement your solution here
    l=0
    r=len(nums)-1
    while l<r:
        mid=(r+l)//2
        if nums[mid]<nums[r]:
            l=mid+1
        else:
            right=mid
                
    return nums[l]
            
print(findMin([4,5,6,7,0,1,2]))
            
        
