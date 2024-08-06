from matplotlib import pyplot as plt

import rl_utils
my_list = []
# labels = ['PimaIndian','German Credit',"Ionosphere"]
# fig, (ax1, ax2) = plt.subplots(1, 2)
with open("list.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
    # 读取文件内容
    #     my_list.append(line.strip())
    # content = file.read()
    #
    # # 使用eval()函数将字符串转换为列表
        my_list = eval(line)
        first = my_list[0]
        test_list = []
        for num, i in enumerate(my_list):
            test_list.append((i))
            # test_list.append(i)
        # test_list = test_list[:800]

        print(max(test_list), min(test_list))
        print(test_list.index(max(test_list)))
        x = range(len(test_list))
        test_list = rl_utils.moving_average(test_list,25)
        plt.plot(x, test_list, label=f'Line {line_number}')  # 添加标签
        plt.xlabel('Episodes')
        plt.ylabel('Improve Level')
        # labels.append(f'Line {line_number}')
# plt.legend(labels=labels)
# plt.savefig('Convergence Analysis.pdf', dpi=600, format='pdf')
plt.show()

