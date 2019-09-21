import pickle
from sklearn.native_bayes import GaussionNB
from sklearn.model_selction import train_test_split
from sklearn.metrics import accuracy_score

data_file = "./ok-spam.pickle"
save_file = "./ok-spam-model.pickle"
data = pickle.load(open(data_file, "rb"))
y = data[0]
x = data[1]

count = 100
rate = 0
for i in range(count):
    x_train. x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2)
    model = GaussionNB()
    model.fit(x_train, y_train)
    # 評価
    y_pred = model.predict(x_test)
    acc = accuracy_score(y_test, y_pred)
    # 評価結果が良ければモデルを保存
    if acc > 0.94: pickle.dump(model, open(save_file, "wb"))
    print(acc)
    rate += acc

# 平均値を表示
print("----")
print("average = ", rate / count)
