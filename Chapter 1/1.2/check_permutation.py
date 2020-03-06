#Check permutation


#Quick solution

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


#Solution 2

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    for letter in str2:
        if letter in str1:
            str1 = str1.replace(letter,'')
    return str1 == ''
 
 
#Solution 3 - using hash tables

def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    hash = {}
    
    for letter in str2:
        if letter in hash:
            hash[letter] += 1
        else:
            hash[letter] = 1
    
    for letter in str1:
        if letter in hash:
            hash[letter] -= 1
        else:
            hash[letter] = 1
    
    for key in hash:
        if hash[key] != 0:
            return False
        return True
