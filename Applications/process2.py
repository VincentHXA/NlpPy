# -*- coding: utf-8 -*-

from synonyms import synonyms
import redis
import random

conn_pool = redis.ConnectionPool(host='127.0.0.1', password='redis123', port=6379, db=0, decode_responses=True)
myredis = redis.Redis(connection_pool=conn_pool)

page_term_dict = myredis.hgetall('__hash_repository_body_terms_jieba')

def getSynonyms(page_term_dict, percentage, num):
    resdict = {}
    for url in page_term_dict.keys():
        terms = str(page_term_dict[url]).split(' ')
        size = len(terms)
        res = []
        print('current: ', url)
        for i in range(num):
            term_synonyms = []
            count = 0
            done = set()
            # while count <= size*percentage or len(done)==size:
            # target_size = int(size*percentage)
            # choose_terms = random.sample(terms, target_size)

            for term in terms:
                syn, scores = synonyms.nearby(term)
                if len(syn)>0:
                    term_synonyms.append(random.sample(syn, 1)[0])
                    count = count + 1
                else:
                    term_synonyms.append(term)
            res.append(term_synonyms)
            myredis.hset('__synonyms_' + url, i, ' '.join(term_synonyms))
            # print(count,'/',size,'/',len(done),'-->',term_synonyms)
        resdict[url] = res

# synonyms_dict = getSynonyms(page_term_dict, 1.0, 200)

idf = myredis.hkeys('__hash_idf')
print(len(idf))

# print(len(synonyms_dict))
# for key in synonyms_dict.keys():
#     print(key)
#     list = synonyms_dict[key]
#     for i in range(len(list)):
#         input = ' '.join(list[i])
#         myredis.hset('__synonyms_'+key, i, )
        # print(len(l), '-->', l)