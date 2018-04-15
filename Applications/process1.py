# -*- coding: utf-8 -*-

import redis
import jieba

connection_pool = redis.ConnectionPool(host='127.0.0.1', password='redis123', port=6379, db=0, decode_responses=True)
myRedis = redis.Redis(connection_pool=connection_pool)

# 取旧网页
pipe = myRedis.pipeline(transaction=True)
oldurls = myRedis.hkeys('__hash_url_templates')

# page_dict = {}
# for url in oldurls:
    # page_dict[url] = myRedis.hget('__hash_repository_html_body', url)
# pipe.execute()
page_dict = myRedis.hgetall('__hash_repository_html_body')

# 载入停用词
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords

# 分词
def segmentation(corpus, stopwords):
    list_dict = {}
    for url in corpus.keys():
        text = corpus[url]
        try:
            words = jieba.cut(text, HMM=True)
            cleanwords = []
            for w in words:
                w = w.strip()
                if w not in (stopwords, ' ', '', '|', '：', '，', '-', '[', ']', '！'):
                    cleanwords.append(w)
            list_dict[url] = ' '.join(cleanwords)
        except TypeError:
           print('TypeError')
    return list_dict

# pages_tags = segmentation(page_dict, stopwordslist('stop words.txt'))

# print(pages_tags.__len__())
# for key in pages_tags.keys():
#     print(key,'-->',' '.join(pages_tags[key]))

# myRedis.hmset('__hash_repository_body_terms_jieba_all', pages_tags)
#
idf = myRedis.hgetall('__hash_idf')
for i in idf.keys():
    if float(idf[i]) < 1:
        print(idf[i])
# print(idf)
# print(len(idf))