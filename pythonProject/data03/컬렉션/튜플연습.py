target = ('영어999', '코딩마스터', 'ceo')
print(target[0])
print(target[0:2])

# tuple = 읽기전용
# target[0] = '일본어만점'
# print(target)

target2 = list(target)
print(target2)
print(type(target2))
print('마지막값>> ', target2[-1])
target2[0] = '일본어만점'
print(target2)
target = tuple(target2)
print(target)

next = ('여행', '또여행')
print(next + target)

# next0 = '여행', next1 = '또여행' 으로 들어감.(tuple만 가지는 특성)
next0, next1 = next
print(next0)
print(next1)