#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
    test jieba extract tags using TextRank Algorithm demo
'''

import jieba.analyse

content = '孙中山生于广东省香山县（今中山市）翠亨村的农民家庭。 [2]  青少年时代受到广东人民斗争传统的影响，向往太平天国反清事业，自诩“洪秀全第二”。1905年（光绪三十一年）成立中国同盟会。1911年10月10日（宣统三年）新军中的革命党人暗中联络，决定当天晚上起义。辛亥革命后被推举为中华民国临时大总统（任期1912年1月1日——1912年4月1日）。1925年3月12日孙中山在北京逝世，1929年6月1日，根据其生前遗愿，葬于南京紫金山中山陵。 [3]  1940年，国民政府通令全国，尊称其为中华民国国父。'

tags = jieba.analyse.textrank(content, 30, withWeight=True)

for tag in tags:
    print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))