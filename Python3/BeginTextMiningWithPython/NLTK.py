from nltk.tokenize.stanford_segmenter import StanfordSegmenter
from nltk.tokenize.stanford import CoreNLPTokenizer
# from nltk.tokenize.stanford import

path = "D:/www/data/nlpsoftware/stanford-segmenter"
segmenter = StanfordSegmenter(
    path_to_jar=path + "/stanford-segmenter.jar",
    path_to_sihan_corpora_dict=path + "/data",
    path_to_model=path + "/data/pku.gz",
    path_to_dict=path + "/data/dict-chris6.ser.gz",
    java_class='edu.stanford.nlp.ie.crf.CRFClassifier'

)
#
sentence = u"这是斯坦福中文分词器测试"
sentence = u"工信处女干事每月经过   下属   科室都要亲口交代24口交换机等技术性器件的安装工作"

segmenter.tokenize_sents(u"工信处")
result = segmenter.segment(sentence)
result2 = segmenter.segment_file("D:/www/data/nlpdata/icwb2-data/testing/pku_test.utf8")
clean_content="D:\\www\\data\\Weibo Data\\Weibo Data\\nlp/clean_content.txt"
# clean_content_out="D:\\www\\data\\Weibo Data\\Weibo Data\\nlp/clean_content_out.txt"
# result3 = segmenter.segment_file(clean_content)
print(type(result2))


# with open(clean_content_out,'wb+') as f:
#     f.writelines([(s+"\r\n").encode('utf8') for s in  clean_content_out])
print(result2)
# outfile = open("D:/www/data/nlpsoftware/outfile.txt",'w')
# outfile.write(result)
# outfile.close()
#
# stanford_postagger="D:\\www\\data/nlpsoftware/stanford-postagger-full-2017-06-09\\stanford-postagger.jar"
# stanford_ner="D:\\www\\data/nlpsoftware/stanford-ner-2017-06-09\\stanford-ner.jar"
# classifiers="D:\\www\\data\\nlpsoftware\\stanford-ner\\classifiers\\"
# word_tokenize() implicitly calls sent_tokenize()
# ToktokTokenizer() is fastest
# MosesTokenizer() is able to detokenize text
# ReppTokenizer() is able to provide token offsets
# from nltk.tokenize.stanford import StanfordTokenizer
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.tokenize.moses import MosesTokenizer
from nltk.tokenize.repp import ReppTokenizer
from nltk.tokenize import word_tokenize

# tokenizer = StanfordTokenizer(path_to_jar=stanford_postagger)
# tokenizer = StanfordTokenizer()
# sent = "Good muffins cost $3.88\nin New York.  Please buy me\ntwo of them.\nThanks."
# print (tokenizer.tokenize(sent))

# from nltk.tag import StanfordNERTagger
#
# eng_tagger = StanfordNERTagger(classifiers+'english.all.3class.distsim.crf.ser.gz')
# print (eng_tagger.tag('Rami Eid is studying at Stony Brook University in NY'.split()))



