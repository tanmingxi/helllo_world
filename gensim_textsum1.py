# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 09:27:37 2017

@author: Mingxi TAN
"""

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim.summarization import summarize
from textrank4zh import TextRank4Keyword, TextRank4Sentence

text = "Thomas A. Anderson is a man living two lives. By day he is an " + \
    "average computer programmer and by night a hacker known as " + \
    "Neo. Neo has always questioned his reality, but the truth is " + \
    "far beyond his imagination. Neo finds himself targeted by the " + \
    "police when he is contacted by Morpheus, a legendary computer " + \
    "hacker branded a terrorist by the government. Morpheus awakens " + \
    "Neo to the real world, a ravaged wasteland where most of " + \
    "humanity have been captured by a race of machines that live " + \
    "off of the humans' body heat and electrochemical energy and " + \
    "who imprison their minds within an artificial reality known as " + \
    "the Matrix. As a rebel against the machines, Neo must return to " + \
    "the Matrix and confront the agents: super-powerful computer " + \
    "programs devoted to snuffing out Neo and the entire human " + \
    "rebellion. "

text="习近平（1953年6月15日－），中华人民共和国最高领导人。"+\
    "祖籍河南邓州[a]，籍贯陕西富平，生于北京，中国共产党第五代领导人，第十八届中央委员会总书记。"+\
    "1969年1月参加工作，清华大学化工系毕业，在职研究生学历，法学博士学位[7]，1974年1月加入中国共产党。"+\
    "1979年至1982年，担任国务院办公厅和中央军委办公厅秘书，属现役军人。"+\
    "1982年离开北京，担任中共正定县委副书记、书记，其后先后在厦门市、宁德市、福州市、福建省、浙江省党委和政府担任领导职务。"+\
    "2007年3月，被任命为中共上海市委书记，接替先前因贪腐问题被调查、免职的陈良宇的位置。"+\
    "2007年中共十七届一中全会当选为中共中央政治局常委，被任命为中共中央书记处书记，进入核心领导层，随后接任中共中央党校校长一职。"+\
    "2008年第十一届全国人大一次会议上，习近平成为中华人民共和国副主席[8]。"+\
    "2010年中共十七届五中全会决定增补习近平为中共中央军委副主席。"+\
    "[9]2010年10月28日，全国人大常委会表决，决定习近平为国家军委副主席。" 

text1=u"到了16世纪，算术、 初等代数以及三角学等初等数学已大体完备。17世纪变量概念的"+\
    "产生使人们开始研究变化中的量与量的互相关系和图形间的互相变换。微积分的概念也在此时形成"+\
    "随着数学转向形式化,为研究数学基础而产生的集合论和数理逻辑等也开始发展。"
text2=u"演化心理学从现代演化观点来研究心理的特质理论。例如记忆、知觉、语言等。 它试图去探究是"+\
    "何种人类心理特征在适应进化。即作为自然选择和性选择的功能产品。演化心理学家认为在人类先祖生活"+\
    "的环境下，心理适应的演化解决了呈周期性出现的问题。"
text3=u"结构主义认为世界上存在著不同的结构影响著政治现象。结构的因素包括地缘因素、经济力量、社会规范、"+\
    "价值观等等。环境因素催生、局限著不同的政治现象，甚至使个体无法作出自主的决定。环境可以随人们的影响而变更。"
s = SnowNLP(text)
s.keywords(3)
s.summary(3)
s.sentences
s.words
    
print ('Input text:')
print (text)

print ('Summary:')
print (summarize(text))

###############################################################################

tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)
print( '关键词：' )
for item in tr4w.get_keywords(3, word_min_len=1):
    print(item.word, item.weight)
    
tr4s = TextRank4Sentence()
tr4s.analyze(text=text3, lower=True, source = 'all_filters')    
print()
print( '摘要：' )
for item in tr4s.get_key_sentences(num=1):
    print(item.index, item.weight, item.sentence)

result=tr4s.get_key_sentences(num=3)    


