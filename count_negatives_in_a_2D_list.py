def countNegatives(grid):
    def count_negatives_in_row(row):
        l,r=0,len(row)
        while l<r:
            mid=(l+r)//2
            if row[mid]<0:
                r=mid
            else:
                l=mid+1 
                
        return len(row)-l
        
    total_negatives=0
    for row in grid:
        total_negatives+=count_negatives_in_row(row)
        
    return total_negatives
    
print(countNegatives([[4,3,2,1],[3,2,1,-1],[1,1,0,-1,-2],[-1,-2,-3,-4]]))
    
