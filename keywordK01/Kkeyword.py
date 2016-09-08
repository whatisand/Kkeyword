#-*- coding: utf-8 -*-

"""

스트링형이지만 주석으로도 활용된답니다.

Made by Kim, Dong-Woo

이 프로그램은 문서 키워드 추출과 관련된 연구를 위해 작성되었습니다.


"""




from matplotlib import font_manager, rc
font_fname = '/Library/Fonts/AppleGothic.ttf'     # A font of your choice
font_name = font_manager.FontProperties(fname=font_fname).get_name()
rc('font', family=font_name)
import nltk
from konlpy.tag import Twitter
import numpy
tw = Twitter()
# 트위터 형태소 분석기를 사용함
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 찾으려고 하는 상위 n개의 단어(명사)
_toFind_ = 30

# 문서 읽기
doc_ko = open('./k_tex2.txt').read()

# print(doc_ko)

# 명사만 추출
token_ko = tw.nouns(doc_ko)

# nltk 활용을 위한
res_ko = nltk.Text(token_ko, name=u'sutuk1')



print(len(res_ko.tokens))       # returns number of tokens (document length)
print(len(set(res_ko.tokens)))  # returns number of unique tokens
on_list = res_ko.vocab().most_common(_toFind_)

# on_list 는 리스트이다, most_common 이 리스트를 반환하는데 리스트는 튜플로 이루어져있다, 튜플은 첫번째인자로(0번쨰) 유니코드 스트링형을 갖고 두번째인자로(1번째) 몇번 빈출되었는지

# print(list(on_list[1])[0]) 테스트코드


to_list = list()


# 리스트안에 있는 튜플을 리스트로 바꾼 후 그것중 0번째 인자인 스트링형만 리스트에 다시 담는 작업을 하는 부분이다
for a in range(0, len(on_list)):
    to_list.append(list(on_list[a])[0])

# word_offset 는 딕셔너리로, 최빈단어 '스트링'을 키로, 단어 위치 '리스트'를 벨류로 가지고 있다.
word_offset = {}
# word_var 는 딕셔너리로, 최빈단어 '스트링'을 키로, 그것의 위치의 분산 '정수'를 벨류로 가지고 있다.
word_var = {}



for a in to_list:
    word_offset[a] = list()
    word_var[a] = 0


#이 아래 부분은 스래드로 만들어서 문서 몇개로 잘라서 처리해도 되는 그런 부분으로 볼 수 있겠다.
#이 아래 부분은 키워드 후보(상위n개빈출단어)의 오프셋을
for findword in to_list:
    offset = 0
    for docword in res_ko:
        if docword==word:
            word_offset[findword].append(offset)
        offset = offset + 1


print("최빈단어 상위k개 리스트 : ")
print(to_list)

print("최빈단어 위치 오프셋 리스트 딕셔너리 ")
print(word_offset)

wordtemp = 0

for a in to_list:
    word_var[a] = numpy.var(word_offset[a])
#분산 구하기
print("최빈단어 분산 딕셔너리 " )
print(word_var)

plot_list = list()

for a in to_list:
    if word_var[a] < 2000000: # 사실상 이 분산 기준의 최적값을 찾는게... 러닝을 통해 찾아 낼 수 있으려나
        plot_list.append(a)

# plot_list 는 분산이 21000 미만인 것들, 즉 키워드의 후보이다.

print("키워드 후보(사실상 키워드) " )
print(plot_list)

# plot_list = re.findall('u[\'].[\']',on_list)
# 정규식으로 문제를 해결해보려 했으나 더 편한 방법이 있었다. 역시 포문

fileout = open("./keywords.txt", 'w')

for a in plot_list:
    fileout.write(a)
    fileout.write(" ")


fileout.close()

# 아래 명령어는 문서 전체에서 명사로 분류된 단어중 활용 빈도기즌 상위 _toFind_ 개를 그래프로 나타낸 것이다.
res_ko.plot(_toFind_)


# res_ko.dispersion_plot([u'\uc774', '것', '화면', '수', '분할', '금리', '난방', '지방산', '진리', '권력', '오메가', '중앙은행', '시장', '이미지',
# '온도', '유사', '영상', '방식', '상사', '한학', '경서'])
# 이전에는 이렇게 일일히 찾아서 썼다, 보면 알겠지만 유니코드 넣어도 되는지 테스트하려고 실험해본걸 알 수 있음

res_ko.dispersion_plot(to_list)
res_ko.dispersion_plot(plot_list)

# plot list 는 키워드 리스트, to_ list 는 분산 필터링 하기 전 리스트