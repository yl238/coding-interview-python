"""Merge sorted array b into sorted array a given that array a 
contains len(b) extra space at the end.
"""
def merge(a, b):
    bix = len(b) - 1
    aix = len(a) - len(b) - 1 # a has space b at the end
    
    while aix >= 0 and bix >= 0:
        if a[aix] > b[bix]:
            a[aix + bix + 1] = a[aix]
            aix -= 1
        else:
            a[aix + bix + 1] = b[bix]
            bix -= 1
    while bix >= 0:
        a[bix] = b[bix]
        bix -= 1
    
    return a

if __name__ == '__main__':
    a = [33, 44, 55, 66, 88, 99, None, None, None]
    b = [11, 22, 77]
   
    print(merge(a, b))