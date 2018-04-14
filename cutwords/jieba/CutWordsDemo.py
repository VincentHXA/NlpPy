#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    test jieba demo
'''

import jieba

input = ["这是一个伸手不见五指的黑夜。我叫孙悟空，我爱北京，我爱Python和C++。", "我不喜欢日本和服。", "雷猴回归人间。",
                "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作", "结果婚的和尚未结过婚的"]


# for sentence in input:
#     set_list = jieba.cut(sentence, cut_all=True)  # 全模式
#     print('Full Mode:', ','.join(set_list))

for sentence in input:
    set_list = jieba.cut(sentence)  # 精确模式
    print('Default(Accurate) Mode:', ','.join(set_list))

# for sentence in input:
#     set_list = jieba.cut_for_search(sentence)  # 搜索引擎模式
#     print('Search Mode:', ','.join(set_list))

# for sentence in input:
#     set_list = jieba.cut(sentence, cut_all=True, HMM=True)  # 全模式
#     print('HMM Full Mode:', ','.join(set_list))

for sentence in input:
    set_list = jieba.cut(sentence, HMM=True)  # 精确模式
    print('HMM Default(Accurate) Mode:', ','.join(set_list))
#
# for sentence in input:
#     set_list = jieba.cut_for_search(sentence, HMM=True)  # 搜索引擎模式
#     print('HMM Search Mode:', ','.join(set_list))