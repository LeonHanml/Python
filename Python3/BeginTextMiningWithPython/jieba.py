# encoding=utf8
import jieba
# jieba.cut("我爱自然语言处女")
import jieba.posseg as pseg
words = pseg.cut("我爱自然语言处女")
for word ,flag in words:
    print('%s %s' % (word,flag))