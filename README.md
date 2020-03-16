
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

## Assumption:

All the elements in strings are all lowercase alphabet<br>

## Solution:


```python
def oa(s1, s2):
    # part1
    if len(s1)>len(s2): return False
    # part2
    s1li, s2li = [0]*26, [0]*26
    for i in s1: s1li[ord(i)-97]+=1
    for i in s2: s2li[ord(i)-97]+=1
    s1li.sort(reverse=True)
    s2li.sort(reverse=True)
    s1li, s2li = s1li[:s1li.index(0)], s2li[:s2li.index(0)]
    # part3
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
```

## Explaination:

s1 is the first string, s2 is the second string.

- #### part1:<br>
Since the length of s1, s2 might not be the same. If the length of s1 is larger, there must exist an element that cannot be mapped to s2.<br>

- #### part2:<br>
Construct 2 lists with 26's 0 per each, which represent the number of each alphabet for s1 and s2.<br>
Then, sort with descending order and keep the existing alphabets.<br>

- #### part3:<br>
If the first element in s1li (the maximum value in s1li) is larger than s2li (the maximum value in s2li), return False. (many-to-many mapping)<br>
If both the first element in s1li and s2li are the same, mapping succeed. Then, remove the first elements of s1li and s2li.<br>
If the first element in $s1li$ is smaller than $s1li$, deduct the mapping succeeded value and re-sort the s2li for the next comparison.<br>
If s1li is empty, it means that every element in s1li has been mapped to the value in s2li with the corrected mapping method, return True

- #### Consequence:<br>
> Memory: O(1)<br>
> For any s1 (with length n) and s2 (with length m), the length of s1li and s2li are always 26, which represents a~z (assume k=26)<br>
> <br>
> Runtime: O(n)<br>
> In part 3, although we need the sort in the while loop, since it only sorted with the length of 26, the runtime is k*log(k)*(n+m), which is O(n+m) <br>

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

    the length of s1 22; the length of s2 22
    s1:  lnkpnawkcoxepnvmwlwayr
    s2:  bztmvjdluzjshlpvtpwhug
    the sorted s1:  aacekkllmnnnopprvwwwxy
    the sorted s2:  bdghhjjllmppsttuuvvwzz
    The result: False
    --------------------------------------------------
    the length of s1 26; the length of s2 26
    s1:  vclkshxorqoxuvjbsdnhssjxrp
    s2:  srmwfeepnftaqoxmnzwehvfzti
    the sorted s1:  bcdhhjjklnoopqrrssssuvvxxx
    the sorted s2:  aeeefffhimmnnopqrsttvwwxzz
    The result: False
    --------------------------------------------------
    the length of s1 19; the length of s2 19
    s1:  yskirawujhfkuniyuhj
    s2:  wewttcxrwoiwkxhpjqp
    the sorted s1:  afhhiijjkknrsuuuwyy
    the sorted s2:  cehijkoppqrttwwwwxx
    The result: False
    --------------------------------------------------
    the length of s1 10; the length of s2 10
    s1:  suoqeqhmpd
    s2:  vbzrcrrewn
    the sorted s1:  dehmopqqsu
    the sorted s2:  bcenrrrvwz
    The result: True
    --------------------------------------------------
    the length of s1 22; the length of s2 22
    s1:  gdamssuabvccpcfkstzllu
    s2:  wogbzgjljbhokwlukcvcqy
    the sorted s1:  aabcccdfgkllmpssstuuvz
    the sorted s2:  bbccgghjjkkllooquvwwyz
    The result: False
    --------------------------------------------------
    the length of s1 26; the length of s2 26
    s1:  stjjlzvmelzuwbnfrekoloudxy
    s2:  zinfdcjbmipopjuoypybomjcvl
    the sorted s1:  bdeefjjklllmnoorstuuvwxyzz
    the sorted s2:  bbccdfiijjjlmmnooopppuvyyz
    The result: True
    --------------------------------------------------
    the length of s1 16; the length of s2 16
    s1:  kahdmdrekwxpqobd
    s2:  ravfgyamqfbrzcrr
    the sorted s1:  abdddehkkmopqrwx
    the sorted s2:  aabcffgmqrrrrvyz
    The result: True
    --------------------------------------------------
    the length of s1 26; the length of s2 26
    s1:  mmnpkulavycvixoearhbqavvvv
    s2:  qvdepycvkxxykezyrdlaghcayo
    the sorted s1:  aaabcehiklmmnopqruvvvvvvxy
    the sorted s2:  aaccddeeghkklopqrvvxxyyyyz
    The result: False
    --------------------------------------------------
    the length of s1 27; the length of s2 27
    s1:  tlochhklcwynwqiviywvlllkxpe
    s2:  ozzjszeczkfdhliupfzcvhxsael
    the sorted s1:  ccehhiikklllllnopqtvvwwwxyy
    the sorted s2:  accdeeffhhijkllopssuvxzzzzz
    The result: False
    --------------------------------------------------
    the length of s1 17; the length of s2 17
    s1:  pzhroyuoawgavrhzr
    s2:  yngqewgoshciwkyni
    the sorted s1:  aaghhooprrruvwyzz
    the sorted s2:  cegghiiknnoqswwyy
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

    the length of s1 21; the length of s2 26
    s1:  vrabrdxjgujvptmarasnz
    s2:  ddjqknavjgtphqsmvsmpcnhqjn
    the sorted s1:  aaabdgjjmnprrrstuvvxz
    the sorted s2:  acddghhjjjkmmnnnppqqqsstvv
    The result: True
    --------------------------------------------------
    the length of s1 11; the length of s2 22
    s1:  qpapnmmluho
    s2:  qemkokwzqtlcarixfpgwah
    the sorted s1:  ahlmmnoppqu
    the sorted s2:  aacefghikklmopqqrtwwxz
    The result: True
    --------------------------------------------------
    the length of s1 13; the length of s2 12
    s1:  ghacyoftarepc
    s2:  eppaybibmigc
    the sorted s1:  aaccefghoprty
    the sorted s2:  abbcegiimppy
    The result: False
    --------------------------------------------------
    the length of s1 11; the length of s2 15
    s1:  mbinrrovgap
    s2:  qrnzxucunktrxlw
    the sorted s1:  abgimnoprrv
    the sorted s2:  cklnnqrrtuuwxxz
    The result: True
    --------------------------------------------------
    the length of s1 11; the length of s2 26
    s1:  hoiruxrwpgv
    s2:  zwotgznjjaachfsrgeihynbbjb
    the sorted s1:  ghioprruvwx
    the sorted s2:  aabbbcefgghhijjjnnorstwyzz
    The result: True
    --------------------------------------------------
    the length of s1 29; the length of s2 10
    s1:  yaccpmgmosbygavozkyoeiziqcacn
    s2:  vojmcahnbl
    the sorted s1:  aaabcccceggiikmmnooopqsvyyyzz
    the sorted s2:  abchjlmnov
    The result: False
    --------------------------------------------------
    the length of s1 28; the length of s2 22
    s1:  rfnhnuoeljghudwsngfoymjhjcem
    s2:  dmkhqjxuqufbftmhbrzrnn
    the sorted s1:  cdeeffgghhhjjjlmmnnnoorsuuwy
    the sorted s2:  bbdffhhjkmmnnqqrrtuuxz
    The result: False
    --------------------------------------------------
    the length of s1 10; the length of s2 28
    s1:  erwcjnyukd
    s2:  zfjzwcfyydorwgvcdtuojyxkcupj
    the sorted s1:  cdejknruwy
    the sorted s2:  cccddffgjjjkooprtuuvwwxyyyzz
    The result: True
    --------------------------------------------------
    the length of s1 21; the length of s2 15
    s1:  pyswjsbtxycbwmbbyrlpz
    s2:  umiihzyghlrmmsu
    the sorted s1:  bbbbcjlmpprsstwwxyyyz
    the sorted s2:  ghhiilmmmrsuuyz
    The result: False
    --------------------------------------------------
    the length of s1 25; the length of s2 19
    s1:  nwxgaehtqegbelzrasqzslztb
    s2:  fsamghtikkfntabojjo
    the sorted s1:  aabbeeegghllnqqrssttwxzzz
    the sorted s2:  aabffghijjkkmnoostt
    The result: False
    --------------------------------------------------
    

## This is the end of explanation
Thank you for putting effort into reading it 
