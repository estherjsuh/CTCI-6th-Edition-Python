#One Away

#Quick solution
def one_away(str1, str2):
    #edge case
    if abs(len(str1) - len(str2)) > 1:
        return False

    for i in str1:
        if i in str2:
            str2 = str2.replace(i,"")
    return len(str2) <= 1

#Replace, Insert, Remove
def one_away(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    count = 0
    elif len(str1) == len(str2):
        for letter1, letter2 in zip(str1,str2):
            if letter1 != letter2:
                count += 1
        if count > 1:
            return False
        return True
           
    else: #fill this in
        
        
