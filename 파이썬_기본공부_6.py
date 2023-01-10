# -*- coding: utf-8 -*-
"""파이썬 기본공부 6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RCBfAu4zYXTfG_ULxuN6I7Y9SQa2VQ5W
"""

#리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소 전부 출력

a = [2, 1, 5, 6, 7]

for i in a:

  print(i)

#리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소 전부 출력, len 사용

a = [2, 1, 5, 6, 7]

for i in range(len(a)):

  print(a[i])

#리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소들을 역순으로 출력, len 사용

a = [2, 1, 5, 6, 7]

for i in range(len(a)-1,-1,-1):
  #len(a)-1인 len(a)가 5이고 거꾸로 4부터 0까지 범위를 지정해여하므로
  #총 길이에서 -1을 해준다 -1까지 인 이유는 0번 인덱스를 포함해야 해기 때문이다  

  print(a[i])

#리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력

end_days = [31,28,31,30,31,30,31,31,30,31,30,31]

month = 1

for end_day in end_days:
  print("{}월은  {}일까지".format(month,end_day))
  month +=1

#리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력, len 사용

end_days = [31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(len(end_days)):
  print("{}월은  {}일까지".format(i+1,end_days[i]))

#리스트에 각 달의 끝 날짜들을 담고, '1월은 31일까지'와 같은 양식으로 출력, enumerate 사용

end_days = [31,28,31,30,31,30,31,31,30,31,30,31]
  
for i, end_day in enumerate(end_days):
  print("{}월은  {}일까지".format(i + 1, end_day))

print(list(enumerate(end_days)))

print("== 예제 1 ==")
s = "안녕하세요."

print("s의 길이 출력")
# 구현
print(len(s))
print("s를 이루는 문자 중에서 앞에꺼, 2개 출력")
# 구현
print(s[0:2])
print("s를 이루는 문자 중에서 앞에서 문자 하나 건너 뛰고 1개 출력")
# 구현
print(s[1:2])
print("s를 이루는 문자 중에서 앞에서 문자 4개 출력, 첫 인덱스 생략")
# 구현
print(s[:4])
print("s를 이루는 문자 중에서 앞에서 문자 3개 건너뛰고, 나머지 전부 출력, len")
# 구현
print(s[3:len(s)])
print("s를 이루는 문자 중에서 앞에서 문자 3개 건너뛰고, 나머지 전부 출력, 뒤 인덱스 생략, 방법 2")
# 구현
print(s[3:])
print("== 예제 2 ==")
s = "안녕하세요"

print("s를 이루는 문자를 하나씩 출력, while")
# 구현
i = 0
while i < len(s):
  print(s[i])
  i+=1
print("s를 이루는 문자를 역순으로 하나씩 출력, while")
# 구현
i = len(s)-1
while i > 0:
  print(s[i])
  i-=1
print("s를 이루는 문자를 하나씩 출력, for")
# 구현
for c in s:
  print(c)
print("== 예제 3 ==")
s = "a안b녕c하d세e요f"

print("s를 이루는 문자 중에서 한글만 출력")
# 구현
print(s[1]+s[3]+s[5]+s[7]+s[9])
print("s를 이루는 문자 중에서 한글만 출력, for, if or, continue")
# 구현
for c in s:
  if c == 'a' or c == 'b' or c == 'c' or c == 'd' or c =='e' or c == 'f':
    continue;
  print(c)
print("s를 이루는 문자 중에서 한글만 출력, for, if and, 방법 2")
# 구현
for c in s:
  if c != 'a' and c != 'b' and c != 'c' and c != 'd' and c !='e' and c != 'f':
    print(c)
    
print("s를 이루는 문자 중에서 한글만 출력, for, not in, 방법 3")
# 구현
for c in s:
  if c not in ['a','b','c','d','e','f']:
    print(c,end ='')

# 문제 : string1을 구성하는 문자 중에서 a,b,c,d,e 를 제외하고 출력해주세요.
# 조건 : 함수로 만들고 실행해주세요.
# 조건 : 함수 안에 `string1 = "안a녕b하c세d요e"` 이 부분을 새로 넣어야 합니다.(지역변수로 만들어야 합니다)
# 조건 : 2개 이상 만들어주세요.

def sol_v1():
  string1 = "안a녕b하c세d요e" 

  rs = ""
  rs += string1[0] + string1[2] + string1[4] + string1[6] + string1[8]

  print(rs)

def sol_v2():
  string1 = "안a녕b하c세d요e"

  rs = ""

  string1_len = len(string1)
  i = 0

  while ( i < string1_len ):
    c = string1[i]
    if ( c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e' ):
      rs += c
    i += 1

  print(rs)

def sol_v3():
  string1 = "안a녕b하c세d요e"

  rs = ""

  for c in string1:
    if ( c != 'a' and c != 'b' and c != 'c' and c != 'd' and c != 'e' ):
      rs += c

  print(rs)

def sol_v4():
  string1 = "안a녕b하c세d요e"

  rs = ""

  for c in string1:
    if c not in ['a', 'b', 'c', 'd', 'e']:
      rs += c

  print(rs)

sol_v1()
sol_v2()
sol_v3()
sol_v4()