#Palindrome Permutation

def palin_perm(str):
    hash = {}
    for letter in str:
        if letter in hash:
            hash[letter] += 1
        else:
            hash[letter] = 1
    counter = 0 
    for key in hash:
        if hash[key] % 2 != 0:
            counter += 1
            
    if len(str) % 2 ==0:
        return counter == 0 
    else:
        return counter == 1
