
#### This is the online assessment from Kargo 

## Problem:

Determine whether a one-to-one charachter mapping exists from one string, s1, to another string, s2.

Example1:<br>
>s1 = "abc"<br>
>s2 = "efg"<br>
>print(True)<br>

Example2:<br>
>s1 = "foo"<br>
>s2 = "bar"<br>
>print(False)<br>

Example3:<br>
>s1 = "bar"<br>
>s2 = "foo"<br>
>print(True)<br>

## Analysis:

Based on the example above, we can know that:<br>
1. one-to-one mapping (Example 1, 2) and one-to-many (Example 3) mapping are all valid<br>
2. the length of the two string might not be the same (no assumption in the problem)<br>
3. the order of the alphabet in strings cause no effect to the result<br>

## Solution:


```python
def oa(s1, s2):
    # part1
    s1li, s2li = [0]*26, [0]*26
    for i in s1: s1li[ord(i)-97]+=1
    for i in s2: s2li[ord(i)-97]+=1
    # part2
    if sum(s1li)>sum(s2li): return False
    # part3
    s1li.sort(reverse=True)
    s2li.sort(reverse=True)
    s1li, s2li = s1li[:s1li.index(0)], s2li[:s2li.index(0)]
    while s1li:
        if s1li[0] > s2li[0]: return False
        elif max(s1li) == max(s2li): s1li, s2li = s1li[1:], s2li[1:]
        else: s2li[0], s2li, s1li = s2li[0]-s1li[0], sorted(s2li, reverse=True), s1li[1:]
    return True
```

## Explaination:

s1 is the first string, s2 is the second string.

- #### part1:<br>
Construct 2 lists with 26's 0 per each, which represent the number of each alphabet for two strings, s1 and s2.<br>
Then, keep the alphabet that has shown up in s1, s2.<br>

- #### part2:<br>
Since the length of s1, s2 might not be the same. If the length of s1 is larger, there must be an element which cannot be mapping to s2<br>

- #### part3:<br>
Check the first element for mapping.<br>
If the first element in s1li (the maximum value in s1li) is larger than s2li (the maximum value in s2li), return False. (many-to-many mapping)<br>
If the first element in s1li and s2li are the same, mapping succeed. Then, remove the first elements of s1li and s2li.<br>
If the first element in s1li is smaller than s1li, deduct the mapping succeeded value and re-sorted the s2li for the next comparison.<br>
If s1li is empty, it means that every element in s1li has been mapped to the value in s2li with the corrected mapping method, return True.

## Basic Testing:


```python
# should pass
s1 = "abc"
s2 = "efg"
assert(oa(s1, s2) == True)
```


```python
# should fail
s1 = "foo"
s2 = "abc"
assert(oa(s1, s2) == True)
```


    ---------------------------------------------------------------------------

    AssertionError                            Traceback (most recent call last)

    <ipython-input-3-78596cb2e7a3> in <module>
          2 s1 = "foo"
          3 s2 = "abc"
    ----> 4 assert(oa(s1, s2) == True)
    

    AssertionError: 



```python
# should pass
s1 = "abc"
s2 = "foo"
assert(oa(s1, s2) == True)
```


```python
# should pass
s1 = "abcc"
s2 = "aaab"
assert(oa(s1, s2) == True)
```

## Random Case Testing:


```python
import random
import string

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def test_result(length_s1, length_s2):
    s1 = generate_random_string(length_s1)
    s2 = generate_random_string(length_s2)
    print(f"the length of s1 {length_s1}; the length of s2 {length_s2}")
    print("s1: ", s1)
    print("s2: ", s2)
    print("the sorted s1: ", "".join(sorted(s1)))
    print("the sorted s2: ", "".join(sorted(s2)))
    print(f"The result: {oa(s1, s2)}")
    print("-"*50)
```


```python
# test for the same length 
testing_times = 10
testing_length_range = (10, 30)
for _ in range(testing_times):
    length_s1 = length_s2 = random.randrange(*testing_length_range)
    test_result(length_s1, length_s2)
```

    the length of s1 27; the length of s2 27
    s1:  dnnrqdrgbfhzyoesvtudnmltpnm
    s2:  twfqulmrtjonpuuxcvrmokkdctq
    the sorted s1:  bdddefghlmmnnnnopqrrsttuvyz
    the sorted s2:  ccdfjkklmmnoopqqrrtttuuuvwx
    The result: False
    --------------------------------------------------
    the length of s1 19; the length of s2 19
    s1:  eehzlsjazyczhbqroaa
    s2:  unuzxjhuyxnlmulgagj
    the sorted s1:  aaabceehhjloqrsyzzz
    the sorted s2:  agghjjllmnnuuuuxxyz
    The result: True
    --------------------------------------------------
    the length of s1 13; the length of s2 13
    s1:  vlkkqipdehres
    s2:  avnoxdphoijwb
    the sorted s1:  deehikklpqrsv
    the sorted s2:  abdhijnoopvwx
    The result: False
    --------------------------------------------------
    the length of s1 27; the length of s2 27
    s1:  aoncofhfrjbesnkwziltlxjehoz
    s2:  pocipoahjuyhbzpghvtqltlsbwi
    the sorted s1:  abceeffhhijjkllnnooorstwxzz
    the sorted s2:  abbcghhhiijlloopppqsttuvwyz
    The result: True
    --------------------------------------------------
    the length of s1 29; the length of s2 29
    s1:  sknnpxvbznqtnwizazczldzlpmqtp
    s2:  fqecelzjhubrblgrmuznesqjqttjn
    the sorted s1:  abcdikllmnnnnpppqqsttvwxzzzzz
    the sorted s2:  bbceeefghjjjllmnnqqqrrsttuuzz
    The result: False
    --------------------------------------------------
    the length of s1 18; the length of s2 18
    s1:  likpcwtylpuayikiwu
    s2:  renesmqyfqziyffcjv
    the sorted s1:  aciiikkllpptuuwwyy
    the sorted s2:  ceefffijmnqqrsvyyz
    The result: False
    --------------------------------------------------
    the length of s1 27; the length of s2 27
    s1:  mcmldkdndrgotgsddqhpoejxkle
    s2:  azejinaorzpnubqklmbemvkefoj
    the sorted s1:  cdddddeegghjkkllmmnoopqrstx
    the sorted s2:  aabbeeefijjkklmmnnoopqruvzz
    The result: False
    --------------------------------------------------
    the length of s1 21; the length of s2 21
    s1:  bbtdrhnrgsuxpdnmrfzyp
    s2:  burvzpubmajswqsfcdaqd
    the sorted s1:  bbddfghmnnpprrrstuxyz
    the sorted s2:  aabbcddfjmpqqrssuuvwz
    The result: False
    --------------------------------------------------
    the length of s1 23; the length of s2 23
    s1:  bhzhnrdmxugmyujucjxjkmu
    s2:  eglbvvkamhtlkoyohmmzggi
    the sorted s1:  bcdghhjjjkmmmnruuuuxxyz
    the sorted s2:  abeggghhikkllmmmootvvyz
    The result: False
    --------------------------------------------------
    the length of s1 22; the length of s2 22
    s1:  kntnchdhjrqocuorobscci
    s2:  bguubydsqmniwufsmunjki
    the sorted s1:  bccccdhhijknnoooqrrstu
    the sorted s2:  bbdfgiijkmmnnqssuuuuwy
    The result: False
    --------------------------------------------------
    


```python
# test for the different length 
testing_times = 10
testing_length_range = (10, 30)
for _ in range(testing_times):
    length_s1 = random.randrange(*testing_length_range)
    length_s2 = random.randrange(*testing_length_range)
    test_result(length_s1, length_s2)
```

    the length of s1 18; the length of s2 13
    s1:  fwoznsanjwqcfcupjw
    s2:  onsrepbaxlfpv
    the sorted s1:  accffjjnnopqsuwwwz
    the sorted s2:  abeflnopprsvx
    The result: False
    --------------------------------------------------
    the length of s1 24; the length of s2 28
    s1:  xykuivmomfdyabaebxslxuok
    s2:  sxxbvipuxjywwvutlpxxkjpstnry
    the sorted s1:  aabbdefikklmmoosuuvxxxyy
    the sorted s2:  bijjklnppprssttuuvvwwxxxxxyy
    The result: True
    --------------------------------------------------
    the length of s1 17; the length of s2 20
    s1:  ckdlskzzhevflwxdh
    s2:  wpvpgavouwklqunrverc
    the sorted s1:  cddefhhkkllsvwxzz
    the sorted s2:  acegklnoppqrruuvvvww
    The result: True
    --------------------------------------------------
    the length of s1 26; the length of s2 13
    s1:  hfihyranowzxhsqpkirzsvyhth
    s2:  augtvzvzqtrvt
    the sorted s1:  afhhhhhiiknopqrrsstvwxyyzz
    the sorted s2:  agqrtttuvvvzz
    The result: False
    --------------------------------------------------
    the length of s1 17; the length of s2 13
    s1:  aziwzspeekxjadczi
    s2:  qtdqidaldknpm
    the sorted s1:  aacdeeiijkpswxzzz
    the sorted s2:  adddiklmnpqqt
    The result: False
    --------------------------------------------------
    the length of s1 17; the length of s2 27
    s1:  lstvqpsedntnhthbn
    s2:  ijnamzzfuacfgktfnnbidjeuzzh
    the sorted s1:  bdehhlnnnpqsstttv
    the sorted s2:  aabcdefffghiijjkmnnntuuzzzz
    The result: True
    --------------------------------------------------
    the length of s1 19; the length of s2 27
    s1:  kjriflsrijkhmvtwqry
    s2:  aqqeehqgltduiqmnlldazghalan
    the sorted s1:  fhiijjkklmqrrrstvwy
    the sorted s2:  aaaaddeegghhillllmnnqqqqtuz
    The result: True
    --------------------------------------------------
    the length of s1 16; the length of s2 18
    s1:  rscueirbjttwqkem
    s2:  zqgtuhvwpgmkhxlpev
    the sorted s1:  bceeijkmqrrsttuw
    the sorted s2:  egghhklmppqtuvvwxz
    The result: True
    --------------------------------------------------
    the length of s1 15; the length of s2 20
    s1:  mrsjgsqnttxaaug
    s2:  pmxattmmkuwdrkkoiszz
    the sorted s1:  aaggjmnqrssttux
    the sorted s2:  adikkkmmmoprsttuwxzz
    The result: True
    --------------------------------------------------
    the length of s1 21; the length of s2 11
    s1:  sgqreklksqzqjgiqacntc
    s2:  wgmjvgaumbu
    the sorted s1:  acceggijkklnqqqqrsstz
    the sorted s2:  abggjmmuuvw
    The result: False
    --------------------------------------------------
    

## This is the end of explanation
Thank you for putting effort into reading it 
