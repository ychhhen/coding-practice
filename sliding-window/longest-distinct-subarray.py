def longest_k_distinct_subarray(k,str1):
    strList = list(str1)
    # corner case
    # k == 0?
    # str1 is empty?
    if len(strList)<= k:
        return len(strList)
    if k == 0 or len(strList) == 0:
        return -1
    
    windowLen, indexStart = 0,0
    windowStr = []

    for indexEnd, ch in enumerate(strList):
        windowStr.append(ch)
        # update the result
        #bugFix: compare len(set()) with k not set()
        if len(set(windowStr)) <= k:
            windowLen = max(windowLen,indexEnd-indexStart+1)
        else:
            #update the window while break the k distinct condition
            while len(set(windowStr))>k:
                windowStr.pop(0)
                indexStart += 1

    return windowLen

def imp_with_dict(k, str1):

    windowLen, indexStart = 0,0
    # replace set() checking with a dict container
    char_frequency = {}

    for indexEnd, ch in enumerate(str1):
        # udpate the dict for the window
        if ch not in char_frequency:
            char_frequency[ch] = 0
        char_frequency[ch] += 1
        # shrink the window when reaching the limitation
        while len(char_frequency)>k:
            left_char = str1[indexStart]
            char_frequency[left_char] -= 1
            #bugFix: need to delete char with 0 appearance to avoid wrong calculation
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            indexStart += 1

        windowLen = max(windowLen,indexEnd-indexStart+1)
        

    return windowLen

def main():
    k = 1
    str1 = "araaci"
    print(longest_k_distinct_subarray(k,str1))
    print(imp_with_dict(k,str1))

main()