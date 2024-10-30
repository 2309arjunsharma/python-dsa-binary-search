def next_greatest_letter(letters, target):
    """
    Return the smallest character in letters that is lexicographically greater than target.

    Parameters:
    letters (List[char]): Sorted array of characters.
    target (char): The target character.

    Returns:
    char: The smallest character greater than target, or the first character if no such character exists.
    """
    # Implement the function logic
    l,r=0,len(letters)
    while l<r:
        mid=l+(r-l)//2
        if letters[mid]>target:
            r=mid
        else:
            l=mid+1 
            
    return letters[l%len(letters)]
    
print(next_greatest_letter(['c','f','j'],'k'))
