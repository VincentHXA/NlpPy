# -*- coding: utf-8 -*-

from synonyms import synonyms

# tokens, natures = synonyms._segment_words('中文近义词工具包')
#
# print(tokens)
# print(natures)

# print("人脸: %s" % (synonyms.nearby("人脸")))
# print("识别: %s" % (synonyms.nearby("识别")))
# print("NOT_EXIST: %s" % (synonyms.nearby("NOT_EXIST")))

sen1 = "旗帜引领方向"
# sen1 = "发生历史性变革"
# sen1 = "发生历史性变革"

sen2 = "旗帜指引道路"
# sen2 = "发生历史性变革"
# sen2 = "发生历史性变革"
r = synonyms.compare(sen1, sen2, seg=True)

print(r)

print(synonyms.display('国家'))