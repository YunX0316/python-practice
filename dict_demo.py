dict_word = {
    "apple":"苹果",
    "banana":"香蕉",
    "cat":"猫",
}
word = input("查哪个单词？")
print(word, "的意思是：", dict_word.get(word, "词典里没有这个单词"))

scores = []
while True:
    s = input("输入一个成绩（直接回车结束）：")
    if s == "":
        break
    scores.append(int(s))

if scores:
    print("共", len(scores), "个成绩")
    print("平均分：", sum(scores) / len(scores))