import math
def solution(str1, str2):
    answer = 0
    def is_alpha(s) :
        if 65<=ord(s.upper())<=90 :
            return True
        return False
    
    list1 = [(str1[i]+str1[i+1]).upper() for i in range(len(str1)-1) if is_alpha(str1[i]) and is_alpha(str1[i+1])]
    list2 = [(str2[i]+str2[i+1]).upper() for i in range(len(str2)-1) if is_alpha(str2[i]) and is_alpha(str2[i+1])]
    
    intersection = set(list1) & set(list2)
    union = set(list1) | set(list2)
    
    if len(union) == 0 :
        return 65536
    
    len_intersection = sum([min(list1.count(i), list2.count(i)) for i in intersection])
    len_union =  sum([max(list1.count(i), list2.count(i)) for i in union])

    answer = math.trunc((len_intersection/len_union)*65536)
    
    return answer

import math
def solution(str1, str2):
    answer = 0
    def get_list(s) :
        l = []
        for i in range(len(s)-1) :
            a = s[i].upper()
            b = s[i+1].upper()
            if 65<=ord(a)<=90 and 65<=ord(b)<=90 :
                l.append(a+b)
        return l
    list1 = get_list(str1)
    list2 = get_list(str2)
    
    len1 = len(list1)
    len2 = len(list2)
    if len1 == 0 and len2 == 0 :
        return 65536
    elif len1 == 0 or len2 == 0 :
        return 0
    
    intersection = []
    for i in list1 :
        if i in list2 : 
            intersection.append(i)
            list2.remove(i)
    
    union = len1 + len2 - len(intersection)
    answer = math.trunc((len(intersection)/union)*65536)
    
    return answer
