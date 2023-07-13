print("=======================Task01==========================")
def find_and_print(messages):
# 當文字串中有[18,college,legal,vote]這些字詞的時候print當前的Key. 沒有的話就跳過進到下一輪。
    for i in messages:
        if ("18" in messages[i]):
            print(i)
        elif("college" in messages[i]):
            print(i)
        elif("legal" in messages[i]):
            print(i)
        elif("vote" in messages[i]):
            print(i)
        else:
            continue


find_and_print({
"Bob":"My name is Bob. I'm 18 years old.",
"Mary":"Hello, glad to meet you.",
"Copper":"I'm a college student. Nice to meet you.",
"Leslie":"I am of legal age in Taiwan.",
"Vivian":"I will vote for Donald Trump next week",
"Jenny":"Good morning."
})

print("=======================Task02==========================")
def calculate_sum_of_bonus(data):
    # 1.根據薪資保底計算都會給予5%獎金
    # 2.職位:Sales+300，CEO+1000，Engineer+500，工作表現獎金另計。
    # 3.工作表現高於平均值的話額外加800元獎勵金，工作表現維持在標準線上給予400元獎勵金
    # 獎金總計10000台幣。
    bonus1 = 0
    bonus2 = 0
    total_bonus = 0
    # 先判斷薪資，並轉換為int(TWD)
    for i in data["employees"]:
        if type(i["salary"]) is str:
            i["salary"] = i["salary"].replace(",", "")
            if "USD" in i["salary"]:
                i["salary"] = int(i["salary"][:-3]) * 30
        else:
            i["salary"] = int(i["salary"])
        i["salary"] = int(i["salary"])

        # 判斷職位給予職位獎金
        if i["role"] == "Engineer":
            bonus2 += 500
        elif i["role"] == "CEO":
            bonus2 += 1000
        elif i["role"] == "Sales":
            bonus2 += 300

        # 判斷工作績效給予獎金
        if i["performance"] == "above average":
            bonus2 += 800
        elif i["performance"] == "average":
            bonus2 += 400
        # 將每一迴圈的薪資加總
        bonus1 += i["salary"]
    # 在外圈沒有Loop的位置全部一起乘以0.05取得總體基本薪資保底的5%獎金
    bonus1 *= 0.05
    # 將獎金1、2相加並轉為INT打印
    total_bonus = bonus1 + bonus2
    total_bonus = int(total_bonus)
    print(total_bonus)


calculate_sum_of_bonus(
    {
        "employees": [
            {
                "name": "John",
                "salary": "1000USD",  # 1500 500 800
                "performance": "above average",
                "role": "Engineer",
            },
            {
                "name": "Bob",
                "salary": 60000,  # 3000 1000 400
                "performance": "average",
                "role": "CEO",
            },
            {
                "name": "Jenny",
                "salary": "50,000",  # 2500 300
                "performance": "below average",
                "role": "Sales",
            },
        ]
    }
)  # call calculate_sum_of_bonus function

print("=======================Task03==========================")
def func(*data):
    middle_names=[]
    middle_name=""
    length = len(middle_names) + 1
    axix=0    #判斷是否要打印"沒有" 假如有打印過資料，則+1，就不會觸發最後的判斷式。
    for datas in data:
        middle_name = datas[1] 
        middle_names.append(middle_name)
    for datas in data:
        middle_name = datas[1] 
        freq= middle_names.count(middle_name)
        if freq>=2:
            continue
        elif freq==2 and length>4:
            print("沒有")
        else:
            axix+=1
            print(datas)
    if axix == 0:
        print("沒有")
            
func("彭⼤牆", "王明雅", "吳明")  # print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有


print("=======================Task04==========================")
def get_number(index):
#0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, …
#若index為偶數，則規則為除2加上自身的數值。
#若index為奇數，則規則為下一個數字加1，因此index參數先+1做跟偶數同等運算最後再加1即可。
    if index%2 == 0:
        answer=index/2
        answer+=index
        print(int(answer))
    else:
        nums = index+1
        num=nums/2
        nums+=num
        nums+=1
        print(int(nums))

get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15

print("=======================Task05==========================")


def find_index_of_car(seats, status, number):
    serve_seats = []
    for i in range(len(seats)):
        # 檢查車廂是否提供服務，並且大於成員數。 條件成立就將車廂位置數append進max_fitted_seats空LIST中
        if status[i] == 1 and seats[i] >= number:
            serve_seats.append(seats[i])

    # 判斷陣列是否有提供服務的車位
    if len(serve_seats) > 0:
        member = min(serve_seats)  # 找到提供服務的車廂最小值
        print(seats.index(member))  # 打印最小值車廂的位置
    else:
        print("-1")


find_index_of_car([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2)  # print 4
find_index_of_car([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4)  # print -1
find_index_of_car([4, 6, 5, 8], [0, 1, 1, 1], 4)  # print 2
