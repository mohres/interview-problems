# Time Complexity: O(mxn)
# Auxiliary Space: O(mxn)

def distance(s1, s2):
    # Create a table to store results of subproblems 
    dp = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(len(s1) + 1): 
        for j in range(len(s2) + 1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = j    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = i    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif s1[i-1] == s2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                dp[i][j] = 1 + min(dp[i][j-1],      # Insert 
                                   dp[i-1][j],      # Remove 
                                   dp[i-1][j-1]     # Replace 
                                  )
  
    return dp[len(s1)][len(s2)] 

print(distance('biting', 'sitting'))