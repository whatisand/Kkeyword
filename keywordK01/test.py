#-*- coding: utf-8 -*-
from matplotlib import font_manager, rc
font_fname = '/Library/Fonts/AppleGothic.ttf'     # A font of your choice
font_name = font_manager.FontProperties(fname=font_fname).get_name()
rc('font', family=font_name)
import nltk
from konlpy.tag import Twitter
tw = Twitter()
# 트위터 형태소 분석기를 사용함
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 찾으려고 하는 상위 n개의 단어(명사)
_toFind_ = 40

doc_ko = open('./k_tex1.txt').read()

# print(doc_ko)

token_ko = tw.nouns(doc_ko)


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


word_offset = {}

a = to_list[3]


word_offset[a] = list()





c = 0

for b in res_ko:
    if b==a:
        word_offset[a].append(c)
    c = c + 1


print(a)
print(word_offset[a])