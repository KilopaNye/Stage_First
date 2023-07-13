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

        # 判斷工作績效給予職位獎金
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
