import numpy as np

# 骰娘程序demo_version1
# 控制台输出交互版

print("ciallo~，主人您好，请问有什么能为您服务的？")
print("简易投骰子请按1，循环投骰子请按2喵~")

num_input = float(input())
# 简易骰子，只投掷一次
if num_input == 1:
    print("现在进入简易骰子辣~ o(*￣▽￣*)o")
    print("主人请选择交互模式，默认投掷（0,100）还是自定义范围喵~，前者按1，后者按2喵喵喵~")
    mode_type = float(input())
    if mode_type == 1:
        print("主人请投掷，输入1停止喵~")
        this_rand = 0
        while 1:
            this_rand = np.random.randint(100)
            round_end = float(input())
            if round_end == 1:
                break
        print(str(this_rand)+'/'+str(100))
        if this_rand > 50:
            print("大成功喵！")
        else:
            print("大失败喵喵喵...")
    elif mode_type == 2:
        print("主人请输入想要的投掷范围喵~（默认从0开始，符合人的习惯认知）")
        ceil_num = int(input())
        print("主人请投掷，输入1停止喵~")
        this_rand = 0
        while 1:
            this_rand = np.random.randint(100)
            round_end = float(input())
            if round_end == 1:
                break
        print(str(this_rand) + '/' + str(100))
        if this_rand > 50:
            print("大成功喵！")
        else:
            print("大失败喵喵喵...")
# 循环骰子，用户自行决定投掷多少次
elif num_input == 2:
    print("现在主人不杀死本喵本喵就不会走了喵~")
    print("请主人赋予本喵生命吧！（输入整数，表示投掷轮次数）")
    try_num = int(input())
    all_rands = []
    all_results = []
    for i in range(try_num):
        print("现在是第"+str(i+1)+"次投掷喵喵喵~~~")
        print("主人请选择交互模式，默认投掷（0,100）还是自定义范围喵~，前者按1，后者按2喵喵喵~")
        mode_type = float(input())
        if mode_type == 1:
            print("主人请投掷，输入1停止喵~")
            this_rand = 0
            while 1:
                this_rand = np.random.randint(100)
                round_end = float(input())
                if round_end == 1:
                    break
            print(str(this_rand) + '/' + str(100))
            if this_rand > 50:
                print("大成功喵！")
                all_results.append("成功！")
            else:
                print("大失败喵喵喵...")
                all_results.append("失败...")
        elif mode_type == 2:
            print("主人请输入想要的投掷范围喵~（默认从0开始，符合人的习惯认知）")
            ceil_num = int(input())
            print("主人请投掷，输入1停止喵~")
            this_rand = 0
            while 1:
                this_rand = np.random.randint(100)
                round_end = float(input())
                if round_end == 1:
                    break
            print(str(this_rand) + '/' + str(100))
            if this_rand > 50:
                print("大成功喵！")
                all_results.append("成功！")
            else:
                print("大失败喵喵喵...")
                all_results.append("失败...")
        all_rands.append(this_rand)
    print("下面是主人所有的投掷结果喵~")
    for i in range(try_num):
        print("第"+str(i)+"次:"+str(all_rands[i])+" "+all_results[i])
# 错误输入处理
else:
    print("不是哥们，1和2还能输入别的啊...")
