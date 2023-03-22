#!/usr/bin/env python
# coding: utf-8

# In[ ]:
#建立字典
word_count = {}

#讀取文字檔
with open('hw2_data.txt', 'r') as f:
    for line in f:
        #將每行內容轉換成單字
        word = line.strip()
        #如果單字已經出現過就加一
        if word in word_count:
            word_count[word] += 1
        #如果單字沒出現過就算一    
        else:
            word_count[word] = 1

#輸出結果
print("總共有 {} 個不重複的英文字".format(len(word_count)))
for word, count in word_count.items():
    print("{} 出現了 {} 次".format(word, count))



