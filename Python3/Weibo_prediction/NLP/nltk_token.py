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
# sentence = u"这是斯坦福中文分词器测试

# result = segmenter.segment(sentence)
# result2 = segmenter.segment_file("D:/www/data/nlpdata/icwb2-data/testing/pku_test.utf8")
clean_content="D:\\www\\data\\Weibo Data\\Weibo Data\\nlp/clean_content.txt"
clean_content_out="D:\\www\\data\\Weibo Data\\Weibo Data\\nlp/clean_content_out.txt"
result3 = segmenter.segment_file(clean_content)
print(result3)

with open(clean_content_out,'wb+') as f:
    f.write(result3.encode('utf8'))
