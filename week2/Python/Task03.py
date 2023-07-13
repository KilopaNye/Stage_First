def func(*data):
    middle_names = []
    middle_name = ""
    length = len(middle_names) + 1
    axix = 0  # 判斷是否要打印"沒有" 假如有打印過資料，則+1，就不會觸發最後的判斷式。
    for datas in data:
        middle_name = datas[1]
        middle_names.append(middle_name)
    for datas in data:
        middle_name = datas[1]
        freq = middle_names.count(middle_name)
        if freq >= 2:
            continue
        elif freq == 2 and length > 4:
            print("沒有")
        else:
            axix += 1
            print(datas)
    if axix == 0:
        print("沒有")


func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
