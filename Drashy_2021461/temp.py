def findWildcardMin(n, pattern):
    ans = 0
    for i in range(len(pattern[0])):
        poss = set()
        for j in range(n):
            if pattern[j][i] != '?':
                poss.add(pattern[j][i])
            if len(poss) > 2:
                break
        if len(poss) >= 2:
            ans += 1
    
    return ans

p=["ha?????ank", "?a?ker?ank","??????????" ,"hacker?ank"]

print(findWildcardMin(4,p))