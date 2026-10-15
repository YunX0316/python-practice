name = input("你叫什么名字？")
print("你好，" + name + "!")

age = int(input("你今年多大了？"))
if age >= 18 :
    print(name + "你已经是大人了，可以学 Agentic AI 了！")
else :
    print(name + "小小年纪就在学编程，前途无量！")

mood = input("今天心情怎么样？（好/不好）")
if mood == "好" :
    print("保持住，学习效率翻倍！")
elif mood == "不好" :
    print("没关系，敲两行代码就好了~")
else :
    print("看不懂你的回答，但祝你今天顺利！")