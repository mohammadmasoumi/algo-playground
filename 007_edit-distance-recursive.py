

def edit_distance(s1, s2, n, m):
    if n == 0:
        return m
    elif m == 0:
        return n
    elif s1[n-1] == s2[m-1]:
        return edit_distance(s1, s2, n-1, m-1)
    else:
        return 1 + min(min(edit_distance(s1, s2, n-1, m-1), edit_distance(s1, s2, n-1, m)), edit_distance(s1, s2, n, m-1))
    

str1 = "geek"
str2 = "gesek"
print(edit_distance(str1, str2, len(str1), len(str2)))


str1 = "GEEXSFRGEEKKS"
str2 = "GEEKSFORGEEKS"
print(edit_distance(str1, str2, len(str1), len(str2)))

str1 = "sunday"
str2 = "saturday"
print(edit_distance(str1, str2, len(str1), len(str2)))

"""
Time Complexity: O(3^m), when length of “str1” >= length of “str2” and O(3^n), when length of “str2” > length of “str1”. Here m=length of “str1 and n=length of “str2”
Auxiliary Space: O(m), when length of “str1” >= length of “str2” and O(n), when length of “str2” > length of “str1”. Here m=length of “str1 and n=length of “str2”
"""