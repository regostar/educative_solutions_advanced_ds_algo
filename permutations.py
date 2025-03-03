
from typing import List

def permutations(letters: List)->List:
    """
    """
    def dfs(path, used, res):
        # if soln found
        if len(path) == len(letters):
            res.append(path[:])
            # deep copy
            return
        
        # let's traverse 
        for i, letter in enumerate(letters):
            # can we add 
            if used[letter] == True: # using list with positions having used or not used to allow duplicate chars
                # No
                continue
            # add to path 
            path.append(letter)
            used[letter] = True
            dfs(path, used, res)

            # now backtrack
            path.pop()
            # remove this char and try
            used[letter] = False

    
    res = []
    used_char = {l: False for l in letters}
    dfs([], used_char, res)
    return res



inputs = ['abc', 'ab']
for i in range(len(inputs)):
    print("Permutations : ", permutations(inputs[i]))
