# 1.좋아하는 장소, 싫어하는, 가보고 싶은
 # 좋아하는 장소 찾아서 프린트
 # 가보고 싶은 장소를 '신촌'으로 변경
 # 전체 딕셔너리 키/값을 프린트
pl = {'fav':'유럽', 'hate':'중국', 'wish':'미국'}
print(pl['fav'])
pl['wish'] = '신촌'
for i in pl:
    print(i, pl[i])
print('------------------------------')
# 2.사전을 만들어보세요. 단어는 5개 이상
 # 사전에서 단어를 찾아보세요
 # 사전에 들어있는 전체목록을 프린트
dic = dict()
dic['1월'] = 'january'
dic['2월'] = 'february'
dic['3월'] = 'march'
dic['4월'] = 'april'
dic['5월'] = 'may'
print(dic)
print('------------------------------')
# 3.전체학기 성적 = {'1학기':100, '2학기': 50, '3학기':88, '4학기':99}
 # 2학기의 성적은?
 # 전체 성적 중 85점이 넘는 학기의 점수 프린트
score = {'1학기':100, '2학기': 50, '3학기':88, '4학기':99}
print(score['2학기'])
for i in score:
    if score[i] > 85:
        print(i, score[i])