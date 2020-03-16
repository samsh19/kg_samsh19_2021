import sys

def oa(s1, s2):
    if len(s1)>len(s2): return False
    s1li, s2li = [0]*26, [0]*26
    for i in s1: s1li[ord(i)-97]+=1
    for i in s2: s2li[ord(i)-97]+=1
    s1li.sort(reverse=True)
    s2li.sort(reverse=True)
    s1li, s2li = s1li[:s1li.index(0)], s2li[:s2li.index(0)]
    while s1li:
        if s1li[0] > s2li[0]:
            return False
        elif s1li[0] == s2li[0]: 
            s1li, s2li = s1li[1:], s2li[1:]
        else:
            s2li[0]-=s1li[0]
            s2li.sort(reverse=True)
            s1li = s1li[1:]
    return True

if __name__ == "__main__":
    print(oa(str(sys.argv[1]), str(sys.argv[2])))