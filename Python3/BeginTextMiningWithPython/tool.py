class tool():
    @staticmethod
    def _dic(filename):
        return "D:/www/data/nlp/weibo/" + filename + ".txt"

    __han_stopwords = "stopwords"

    @staticmethod
    def readfile(self, filepath):
        f = open(self._dic(filepath), 'r', encoding="utf-8")
        return f

    @staticmethod
    def writefile(self, filepath):
        f = open(self._dic(filepath), 'w', encoding="utf-8")
        return f

    def readwrite(self, readfilepath, writefilepath):
        f = open(self._dic(readfilepath), 'r')
        g = open(self._dic(writefilepath), 'w')
        return f, g

    @staticmethod
    def get_punctuation_list(*flag):
        english_punctuations = [',', '.', ':', ';', '?', '!', '(', ')', '[', ']', '@', '&', '#', '%', '$', '*', '{',
                                '}', '--', '-']
        chinese_punctuations = ['，', '。.', '：', '；', '？', '（', '）', '【', '】', '！', '@',
                                '#', '%', '￥', '*']
        tag = chinese_punctuations + english_punctuations
        if flag == 'e':
            return english_punctuations
        elif flag == "c":
            return chinese_punctuations
        else:
            return tag

    @staticmethod
    def get_hanNLP_stop_words(self):
        f = self.readfile(self, self.__han_stopwords)
        list = [l.replace("\n", "") for l in f.readlines()]
        f.close()
        return list

    @staticmethod
    def filter_chinese(self, textfilename, outfilename):
        import re
        list = []
        f = self.readfile(self._dic(textfilename))
        g = tool.writefile(self._dic(outfilename))

        for line in f.read().splitlines():
            chstr_list = re.findall(u'[\u4e00-\u9fff]+', line)
            list.append(chstr_list)
        for s in list:
            g.write((" ".join(s) + "\r\n"))
        g.flush()
        g.close()
        f.close()

    @staticmethod
    def get_chinese_stopwords(self):
        import re
        all_stop_list = self.get_hanNLP_stop_words(self)
        print(all_stop_list)
        tmp = ["".join(re.findall(u'[\u4e00-\u9fff]+', s)) for s in all_stop_list]
        return [s for s in tmp if s != ""]

    @staticmethod
    def remove_stopwords_participle(self, textfilename, outfilename, *stopwords):
        if stopwords == "zh":
            stopwordslist = self.get_chinese_stopwords(self)
        elif stopwords == "all":
            stopwordslist = self.get_hanNLP_stop_words(self)
        else:
            stopwordslist = self.get_hanNLP_stop_words(self)
        list = []
        f = self.readfile(self,textfilename)
        for line in f.readlines():
            l = [word.lower() for word in line.split(" ") if word not in stopwordslist]
            list.append(" ".join(l))

        g = tool.writefile(self,outfilename)
        for s in list:
            g.write(s)
        g.flush()
        g.close()
        f.close()


def flat(l):
    for k in l:
        if not isinstance(k, (list, tuple)):
            yield k
        else:
            yield from flat(k)
class text_cut():




    @staticmethod
    def get_FredDict(self,textfilename,outfilename):
        from nltk.probability import FreqDist ,ConditionalFreqDist

        f = tool.readfile(tool,textfilename)
        g = tool.writefile(tool,outfilename)
        result = ([line.replace("\n","").split(" ") for line in  f.readlines()])
        list2 = list(flat(result))
        # for i in result:
        #     list=list +i
        # r= sum(result,[])
        # print(list2)
        fd = FreqDist(list2)

        print(sorted([ i for i in fd.items() if i[1] >50],key=lambda x :x[1],reverse=True))
        print(len(fd))
        # import matplotlib.pyplot as plt
        # fig  = plt.figure()
        #
        # fd.plot()
        # plt.show()



    @staticmethod
    def jieba_cut(self, textfilename, outfilename):
        import jieba
        list = []
        f = tool.readfile(textfilename)
        g = tool.writefile(outfilename)
        for line in f.readlines():
            lcut = jieba.lcut(line, HMM=True)
            tmp = [s for s in lcut if s != " " and s != "\r\n"]
            g.write(" ".join(tmp) + "\n")

        g.flush()
        g.close()
        f.close()

    @staticmethod
    def stanford_cut(self, textfilename, outfilename):
        from nltk.tokenize.stanford_segmenter import StanfordSegmenter
        path = "D:/www/data/nlpsoftware/stanford-segmenter"
        segmenter = StanfordSegmenter(
            path_to_jar=path + "/stanford-segmenter.jar",
            path_to_sihan_corpora_dict=path + "/data",
            path_to_model=path + "/data/pku.gz",
            path_to_dict=path + "/data/dict-chris6.ser.gz",
            java_class='edu.stanford.nlp.ie.crf.CRFClassifier'

        )
        # _, g = tool.readwrite(textfilename, outfilename)
        g = tool.writefile(tool,outfilename)
        # #
        #     sentence = u"这是斯坦福中文分词器测试"
        #     sentence = u"工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作"
        # g = tool.writefile()

        # result = segmenter.segment(sentence)
        filepath = tool._dic(textfilename)
        result = segmenter.segment_file(filepath)

        g.write(result)

        g.flush()
        g.close()
class wordvector():
    @staticmethod
    def get_tfidf(textfilename):
        from gensim import corpora
        from gensim import  models
        from gensim.matutils import corpus2dense

        f = tool.readfile(tool,"jieba_remove_stopwords_result")
        g = tool.writefile(tool,"00")
        result = ([line.replace("\n","").split(" ") for line in  f.readlines()])
        dict = corpora.Dictionary(result)

        corpus = [dict.doc2bow(r) for r in result ]
        tfidf_model = models.TfidfModel(corpus)
        corpus_tfidf = tfidf_model[corpus]

        corpus_matrix = corpus2dense(corpus_tfidf,len(dict))
        return corpus_tfidf
    @staticmethod
    def get_word2vector(self):
        from gensim import models
        f = tool.readfile(tool,"jieba_remove_stopwords_result")
        g = tool.writefile(tool,"00")
        result = ([line.replace("\n","").split(" ") for line in  f.readlines()])
        model = models.Word2Vec(result ,size=100,window =5,min_count=5)
        model.most_similar(positive=["会"],negative=["不会"],topn=8)
        model.similar_by_word("会",topn=8)

    @staticmethod
    def LDA(self,textfilename):
        from gensim.models.ldamodel import LdaModel
        lad = LdaModel(corpus=wordvector.get_tfidf(textfilename),id2word=dict,num_topics=2)






# print(list(flat([[1,3],[3,5]])))
# text_cut.get_FredDict(text_cut,"jieba_remove_stopwords_result","00")

'''
#Test Function : stanford_cut
# text_cut.stanford_cut(text_cut,"aa","stanford_out1")

#Test Function : get_punctuation_list
print(tool.get_punctuation_list('c'))
l = tool.get_hanNLP_stop_words(tool)
print(l)

#Test Function : readfile/writefile

f = tool.readfile(tool, "clean_content")
print(f.readline())
g = tool.writefile(tool, "aa")
g.write(str(f.readline()))
g.close()
f.close()

#Test Function : remove_stopwords_participle

# tool.filter_chinese(tool,"clean_content","tmp_tool_clean_content")
# tool.remove_stopwords_participle(tool,"stanford_result","stanford_remove_stopwords_result","zh")
# tool.remove_stopwords_participle(tool,"jieba_cut_result8","jieba_remove_stopwords_result","zh")

#Test Function : jieba_cut
# tool.jieba_cut(tool,"clean_content_without_other_flag","jieba_cut_result")
# print(ll)

#Test Function :

'''