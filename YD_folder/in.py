import numpy as np
import random
print("欢迎来到反虚构区，在进行游戏之前，请进行最基本的角色设置")
a=int(input("请输入您的力量点数"))
none=True
number=0
end_flag = 0
while 1:
    random_int=(random.randint(1,99))
    print (random_int)
    if random_int ==99:
        print ("你有一个大失败的投掷检定进入反区,恭喜你呀恭喜你，乖乖等待上帝的惩罚吧！" )
    if random_int == 1:
        print("你有一个大成功的投掷检定进入反区，唔……你作弊了吧？你一定作弊了吧！")
    if random_int >1 and a/random_int>=5:
        print("去买彩票吧，记得分我一半！")
    if a/random_int<5 and a/random_int>3:
        print("哇……好高的成功度，不愧是你")
    if a/random_int<3 and random_int<a:
        print("普普通通，算你成功了吧")
    if (random_int>a and random_int<99):
        print("指望我会安慰你吗？哈哈，失败！")
    end_flag = int(input("如果继续投掷请按1"))
    if end_flag != 1:   #2025.5.24:end == 1 逻辑错误，不满足继续投掷需要 ---> end != 1
        break
        




