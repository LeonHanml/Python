'''
import gensim
from gensim import corpora
corpus = ['This is a text mining book',
          'Is this  is a text mining book',
          'Text mining with python']

texts = [[word for word in document.lower().split()] for document in corpus]
print(texts)

dictionary = corpora.Dictionary(texts)

word_count = [dictionary.doc2bow(text) for text in texts]
print(word_count)

from gensim.matutils import corpus2dense
corpus_matrix = corpus2dense(word_count,len(dictionary))
print(corpus_matrix.T)


print("---")
print(dictionary.keys())
print([i for i in dictionary.values()])
print(dictionary.items())
print([i for i in dictionary.items()])

dictionary.filter_tokens(bad_ids=[0,4])
print([i for i in dictionary.items()])
dictionary.filter_n_most_frequent(1)
print([i for i in dictionary.items()])

dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=100000)

corpus2 = ['That is a text mining book',
          'Is that a text mining book',
          'Text mining with gensim']

texts2 = [[word for word in document.lower().split()] for document in corpus2]

dictionary2 = corpora.Dictionary(texts2)
print([i for i in dictionary2.values()])
print([i for i in dictionary2.items()])

dict1_2 = dictionary.merge_with(dictionary2)
print([dict1_2])
documents1 = ['This is a text mining book',
              'Is this a text mining book']
dict = corpora.Dictionary([[word for word in document.lower().split()] for document in documents1])
print(dict.values())
print(i for i in dict.items())

print([j for j in i ] for i in dict.items())

dict.add_documents([[word for word in document.lower().split()] for document in corpus2])

'''

'''
import gensim
from gensim import corpora ,models
docs = ['This is a text mining book',
        'Is this a text mining book',
        'Text mining with python']
texts = [[word for word in doc.lower().split() ] for doc in docs]
dict = corpora.Dictionary(texts)
corpus = [dict.doc2bow(text) for text in texts]
tfidf_model = models.TfidfModel(corpus)
corpus_tfidf = tfidf_model[corpus]
for i in corpus_tfidf:
    print( i)
print([ i for i in corpus_tfidf])

from gensim.matutils import corpus2dense
corpus_matirx = corpus2dense(corpus_tfidf,len(dict))
print(corpus_matirx.T)
print(dict.keys())
'''

'''
import nltk
import gensim
from nltk.corpus import brown
sentences = [[j for j in i] for i in brown.sents()]
model = gensim.models.Word2Vec(sentences,size=100,
                               window=5,#window：用于设置一个文档中目标词汇和预测词汇之间的最大距离
                               min_count=5 #min_count：在训练过程中忽略所有出现频数小于该值的词汇，默认值为“5”
                               )
# print(set(model.sort_vocab().keys()))
print(len(model['raining']))

doesnt_m = model.doesnt_match(['breakfast', 'cereal', 'raining','snowing''dinner', 'lunch'])
print(doesnt_m)

model.most_similar(positive=["wonderful","happy"],negative=["scared"],topn=5)
model.most_similar(positive=["wonderful","happy"],negative=["scared"],topn=False)
model.n_similarity(['old', 'lady'], ['young', 'boy'])
model.similar_by_word('nice',topn=5)
model.similarity('pleasure', 'happy')
model.similarity('pleasure', 'pleasure')
'''
''''''
import sklearn
from sklearn.datasets import fetch_20newsgroups

dataset = fetch_20newsgroups(shuffle=True, random_state=1,remove=('headers', 'footers', 'quotes'),categories=['rec.sport.baseball'])

len(dataset.data)

from sklearn.feature_extraction.text import CountVectorizer
dtm_vectorizer = CountVectorizer(stop_words="english")
dtm = dtm_vectorizer.fit_transform(dataset.data).toarray()

import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
english_stopwords = stopwords.words("english")
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '!', '@',
                        '#', '%', '$', '*'] # 自定义英文表单符号列表
words=[word_tokenize(t) for t in dataset.data]
words_lower=[[j.lower() for j in i] for i in words] # 小写处理
words_clear=[]
for i in words_lower:
    words_filter=[]
    for j in i:
        if j not in english_stopwords: # 过滤停用词
            if j not in english_punctuations: # 过滤标点符号
                words_filter.append(j)
    words_clear.append(words_filter)
words_clear
import gensim
model = gensim.models.Word2Vec(words_clear,size=100,window=5,min_count=5)























