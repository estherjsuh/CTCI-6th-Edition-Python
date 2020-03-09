#One Away

def one_away(str1, str2):
    #edge case
    if abs(len(str1) - len(str2)) >= 2:
        return False

    for i in str1:
        if i in str2:
            str2 = str2.replace(i,"")
    return len(str2) <= 1
