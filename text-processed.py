import jieba

jieba.set_dictionary('dict.txt.big')
jieba.load_userdict("userdict.txt")

content = open('result.txt', 'rb').read()
words = jieba.cut(content, cut_all=False)

print "Output 精確模式 Full Mode："

import jieba.analyse
wordstop = jieba.analyse.extract_tags(content, topK=50)

print "Output top 50："
for word in wordstop:
    print word


tags = jieba.analyse.extract_tags(content, 10)

print "Output tfidf："
print ",".join(tags)


import json
hash = {}
for item in words: 
  if item in hash:
    hash[item] += 1
  else:
    hash[item] = 1
json.dump(hash,open("count.json","w"))

fd = open("count.csv","w")
fd.write("word,count\n")
for k in hash:
  fd.write("%s,%d\n"%(k.encode("utf8"),hash[k]))
