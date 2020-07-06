def two_sum(list, k): 
    
    # Create an empty hash set 
    s = set() 
    
    for i in range(len(list)): 
        temp = k-list[i] 
        if (temp in s): 
            return True
        s.add(list[i])
    return False

print(two_sum([4,7,1,-3,2], 5))