import pickle
import MeCab
import numpy as np
from aklearn.native_bayes import GaussianNB

test_text1 = """
テストするテキストをここに入力する
"""

test_text2 = """
テストするテキストをここに入力する
"""

data_file = "./ok-spam.pickle"
label_file = "./ok-spam-model.pickle"
label_names = ['OK', 'SPAM']

data = pickle.load(open(data_file), "rb")
word_dic = data[2]

# MeCab準備
tagger = MeCab.Tagger()
# 学習済みモデルを読み出す
model = pickle.load(open())

def check_spam(text):
    zw = np.zeros(word_dic['__id'])
    count = 0
    s = tagger.parse(text)
    for line in s.split("\n"):
        if line == "EOS": break
        params = line.split("\t")[1].split(",")
        org = params[6] # 単語の原形
        if org in word_dic:
            id = word_dic[org]
            zw[id] += 1
            count += 1
    zw = zw / count
    # 予測
    pre = model.predict([zw])[0]
    print("- 結果 = ", label_names[pre])

if __name__ == "__main__":
    check_spam(test_text1)
    check_spam(test_text2)
