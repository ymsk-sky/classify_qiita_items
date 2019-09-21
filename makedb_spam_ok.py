# すべてのテキストを巡回して単語データベースを作成する

import os, glob
import MeCab
import numpy as np
import pickle

savefile = "./ok-spam.pickle"
tagger = MeCab.Tagger()

word_dic = {"__id": 0}
files = []

def read_files(dir, label):
    files = glob.glob(dir + '/*txt')
    for f in files:
        read_file(f, label)

def read_file(filename, label):
    words = []
    with open(filename, "rt", encoding="utf-8") as f:
        text = f.read()
    files.append({
        "label": label,
        "words": text_to_ids(text)
    })

def text_to_ids(text):
    # 形態素解析
    word_s = tagger.parse(text)
    words = []
    for line in word_s.split("\n"):
        if line == 'EOS' or line == '': continue
        word = line.split("\t")[0]
        params = line.split("\t")[1].split(",")
        hinsi = params[0]
        hinsi2 = params[1]
        org = params[6]
        if not (hinsi in ['名詞', '動詞', '形容詞']): continue
        if hinsi == '名詞' and hinsi2 == '数': continue
        id = word_to_id(org)
        words.append(id)
    return words

def word_to_id(word):
    if not (word in word_dic):
        id = word_dic["__id"]
        word_dic["__id"] += 1
        word_dic[word] = id
    else:
        id = word_dic[word]
    return id

def make_freq_data_allfiles():
    y = []
    x = []
    for f in files:
        y.append(f['label'])
        x.append(make_freq_data(f['words']))
    return y, x

def make_freq_data(words):
    cnt = 0
    dat = np.zeros(word_dic["__id"], 'float')
    for w in words:
        dat[w] += 1
        cnt += 1
    dat = dat / cnt
    return dat

if __name__ == "__main__":
    read_files("ok", 0)
    read_files("spam", 1)
    y, x = make_freq_data_allfiles()
    pickle.dump([y, x, word_dic], open(savefile, 'wb'))
    print("finish")
