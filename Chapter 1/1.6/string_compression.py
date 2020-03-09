#String Compression

def string_compression(s):
    if len(s) <= 1:
        return s
    compressed_string = ""
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            compressed_string = compressed_string + s[i]+ str(count)
            count = 1
        i += 1
    compressed_string = compressed_string + s[-1] + str(count)
    if len(s) < len(compressed_string):
        return s
    else:
        return compressed_string
