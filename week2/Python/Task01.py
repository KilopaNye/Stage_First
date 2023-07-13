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