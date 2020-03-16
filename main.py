import sys

def helper(s1, s2):
    s1li, s2li = [0]*26, [0]*26
    for i in s1: s1li[ord(i)-97]+=1
    for i in s2: s2li[ord(i)-97]+=1
    if sum(s1li)>sum(s2li): return False
    s1li.sort(reverse=True)
    s2li.sort(reverse=True)
    s1li, s2li = s1li[:s1li.index(0)], s2li[:s2li.index(0)]
    while s1li:
        if s1li[0] > s2li[0]: return False
        elif max(s1li) == max(s2li): s1li, s2li = s1li[1:], s2li[1:]
        else: s2li[0], s2li, s1li = s2li[0]-s1li[0], sorted(s2li, reverse=True), s1li[1:]
    return True

if __name__ == "__main__":
    print(helper(str(sys.argv[1]), str(sys.argv[2])))