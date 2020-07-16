# Time Complexity: O(mxn)
# Auxiliary Space: O(m)

def distance(s1, s2):
    
    DP = [[0 for x in range(len(s2) + 1)] for x in range(len(s1) + 1)] 
 
    for i in range(0, len(s1) + 1):
        DP[0][i] = i

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if (j == 0):
                DP[i % 2][j] = i 
            elif (s1[j - 1] == s2[i - 1]):
                DP[i % 2][j] = DP[(i - 1) % 2][j - 1]; 
            
            else:
                DP[i % 2][j] = 1 + min(DP[(i - 1) % 2][j], min(DP[i % 2][j - 1],DP[(i - 1) % 2][j - 1])); 
     
  
    return DP[len(s2) % 2][len(s1)]

print(distance('biting', 'sitting'))