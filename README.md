
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
1. one-to-one mapping (Example 1) and many-to-one (Example 3) mapping are all valid<br>
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
    s1li, s2li = sorted(s1li, reverse=True), sorted(s2li, reverse=True)
    s1li, s2li = s1li[:s1li.index(0)], s2li[:s2li.index(0)]
    while s1li:
        if s1li[0] > s2li[0]: return False
        elif s1li[0] == s2li[0]: s1li, s2li = s1li[1:], s2li[1:]
        else: s2li[0], s2li, s1li = s2li[0]-s1li[0], sorted(s2li, reverse=True), s1li[1:]
    return True
```

## Explaination:

$s1$ is the first string, $s2$ is the second string.

- #### part1:<br>
Construct 2 lists with 26's 0 per each, which represent the number of each alphabet for two strings, $s1$ and $s2$.<br>
Then, keep the alphabet that has shown up in $s1$, $s2$.<br>

- #### part2:<br>
Since the length of $s1$, $s2$ might not be the same. If the length of $s1$ is larger, there must be an element which cannot be mapping to $s2$<br>

- #### part3:<br>
Check the first element for mapping.<br>
If the first element in $s1li$ (the maximum value in $s1li$) is larger than $s2li$ (the maximum value in $s2li$), return $False$. (many-to-many mapping)<br>
If the first element in $s1li$ and $s2li$ are the same, mapping succeed. Then, remove the first elements of $s1li$ and $s2li$.<br>
If the first element in $s1li$ is smaller than $s1li$, deduct the mapping succeeded value and re-sorted the $s2li$ for the next comparison.<br>
If $s1li$ is empty, it means that every element in $s1li$ has been mapped to the value in $s2li$ with the corrected mapping method, return $True$

## Basic Testing:


```python
# should pass
s1 = "abc"
s2 = "efg"
assert(oa(s1, s2) == True)
```


```python
# should pass
s1 = "foo"
s2 = "abc"
assert(oa(s1, s2) == False)
```


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

    the length of s1 23; the length of s2 23
    s1:  jorgzpxdpcetdwbjikwsanj
    s2:  fphlivomuufivrmmffxnkzy
    the sorted s1:  abcddegijjjknopprstwwxz
    the sorted s2:  ffffhiiklmmmnopruuvvxyz
    The result: True
    --------------------------------------------------
    the length of s1 19; the length of s2 19
    s1:  illwropgoxgzrqtwbpx
    s2:  nnsvxennxdhrhsdmjmf
    the sorted s1:  bggillooppqrrtwwxxz
    the sorted s2:  ddefhhjmmnnnnrssvxx
    The result: True
    --------------------------------------------------
    the length of s1 20; the length of s2 20
    s1:  qomyyzjqrpywkarvnqmb
    s2:  jumixohwuinvabsvqaiy
    the sorted s1:  abjkmmnopqqqrrvwyyyz
    the sorted s2:  aabhiiijmnoqsuuvvwxy
    The result: False
    --------------------------------------------------
    the length of s1 19; the length of s2 19
    s1:  pubwrodplupcshzabkk
    s2:  evmaszowvaptvwgtkuz
    the sorted s1:  abbcdhkkloppprsuuwz
    the sorted s2:  aaegkmopsttuvvvwwzz
    The result: True
    --------------------------------------------------
    the length of s1 26; the length of s2 26
    s1:  gqhvxjujsstbuyzaigicyzwmwu
    s2:  vhtddebnntttvdvcznwtanaxkw
    the sorted s1:  abcgghiijjmqsstuuuvwwxyyzz
    the sorted s2:  aabcdddehknnnntttttvvvwwxz
    The result: True
    --------------------------------------------------
    the length of s1 24; the length of s2 24
    s1:  pdihscnggqknhoecqtauxjth
    s2:  ytsmzroocdbdcrujhqgfppts
    the sorted s1:  accdegghhhijknnopqqsttux
    the sorted s2:  bccddfghjmooppqrrssttuyz
    The result: False
    --------------------------------------------------
    the length of s1 19; the length of s2 19
    s1:  jrurppvuieubupivdth
    s2:  wytqbnmoikhtgaswrxo
    the sorted s1:  bdehiijppprrtuuuuvv
    the sorted s2:  abghikmnooqrsttwwxy
    The result: False
    --------------------------------------------------
    the length of s1 12; the length of s2 12
    s1:  jtbiehzlocwi
    s2:  bklkpccqztgc
    the sorted s1:  bcehiijlotwz
    the sorted s2:  bcccgkklpqtz
    The result: True
    --------------------------------------------------
    the length of s1 20; the length of s2 20
    s1:  sxzfmstdsknkjswwiivy
    s2:  ubdjirmztoslowukdgxt
    the sorted s1:  dfiijkkmnsssstvwwxyz
    the sorted s2:  bddgijklmoorsttuuwxz
    The result: False
    --------------------------------------------------
    the length of s1 22; the length of s2 22
    s1:  aqrndsgrpwzskwxagsqpny
    s2:  wmehdmnbvvwfbwevamocwt
    the sorted s1:  aadggknnppqqrrssswwxyz
    the sorted s2:  abbcdeefhmmmnotvvvwwww
    The result: True
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

    the length of s1 14; the length of s2 12
    s1:  odzkvdbsregfra
    s2:  hkbqokqbbgef
    the sorted s1:  abddefgkorrsvz
    the sorted s2:  bbbefghkkoqq
    The result: False
    --------------------------------------------------
    the length of s1 18; the length of s2 14
    s1:  nxadghqoqwhsdxxcum
    s2:  fqtvjtnpqlunet
    the sorted s1:  acddghhmnoqqsuwxxx
    the sorted s2:  efjlnnpqqtttuv
    The result: False
    --------------------------------------------------
    the length of s1 22; the length of s2 21
    s1:  lvimhgwlidlraodwrhiyrp
    s2:  dubmscujvrmcldgudoiet
    the sorted s1:  addghhiiilllmoprrrvwwy
    the sorted s2:  bccdddegijlmmorstuuuv
    The result: False
    --------------------------------------------------
    the length of s1 21; the length of s2 26
    s1:  sujnguifefmksitbktkdk
    s2:  nlbtfjlsccgtdhjzokkggcstgv
    the sorted s1:  bdeffgiijkkkkmnssttuu
    the sorted s2:  bcccdfgggghjjkkllnosstttvz
    The result: True
    --------------------------------------------------
    the length of s1 26; the length of s2 21
    s1:  cnoootqzqmofzuwugzuifxmrkk
    s2:  hfsknoajdjpvgpsoolzwb
    the sorted s1:  cffgikkmmnooooqqrtuuuwxzzz
    the sorted s2:  abdfghjjklnoooppssvwz
    The result: False
    --------------------------------------------------
    the length of s1 18; the length of s2 17
    s1:  afmsmfbrzfztnqxjbr
    s2:  cnehozjhwpcqnlgtw
    the sorted s1:  abbfffjmmnqrrstxzz
    the sorted s2:  cceghhjlnnopqtwwz
    The result: False
    --------------------------------------------------
    the length of s1 13; the length of s2 16
    s1:  rmekxqjzdbfwl
    s2:  kqtqeumdlkoyhhnx
    the sorted s1:  bdefjklmqrwxz
    the sorted s2:  dehhkklmnoqqtuxy
    The result: True
    --------------------------------------------------
    the length of s1 19; the length of s2 15
    s1:  xbxvczpmovsvjmfayba
    s2:  ouzpwzoxkkwvumh
    the sorted s1:  aabbcfjmmopsvvvxxyz
    the sorted s2:  hkkmoopuuvwwxzz
    The result: False
    --------------------------------------------------
    the length of s1 21; the length of s2 15
    s1:  vhbvegnhievakzhpyadpu
    s2:  mmfxwmqdqzyczmc
    the sorted s1:  aabdeeghhhiknppuvvvyz
    the sorted s2:  ccdfmmmmqqwxyzz
    The result: False
    --------------------------------------------------
    the length of s1 28; the length of s2 23
    s1:  gmovguqpgxypyfqvypfauumfikes
    s2:  iihqzgfuwynaevrmqjicrqm
    the sorted s1:  aefffgggikmmopppqqsuuuvvxyyy
    the sorted s2:  acefghiiijmmnqqqrruvwyz
    The result: False
    --------------------------------------------------
    

## This is the end of explanation
Thank you for putting effort into reading it 
