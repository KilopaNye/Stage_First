function findAndPrint(messages) {
    // 根據自我介紹中出現的語句判斷，
    // 依照18 years old、college student、legal age、vote for Donald Trump等語句推理，
    // 可以得知Bob、Copper、Leslie、Vivian年紀已超過17歲。因此根據相關關鍵字作為判斷依據。
    // your code here, based on your own rules
    let obj = Object.keys(messages);
    for (let g = 0; g < obj.length; g++) {
        let key = obj[g];
        let value = messages[key];
        let arr = value.split(' ');           //將值轉換為分割字符串
        for (let i = 0; i < arr.length; i++) {      //用if for迴圈判斷字符始有有相符，沒有的話就跳下一個。
            if ("18" == arr[i]) {
                console.log(key);
            } else if ("college" == arr[i]) {
                console.log(key);
            } else if ("legal" == arr[i]) {
                console.log(key);
            } else if ("vote" == arr[i]) {
                console.log(key);
            } else {
                continue;
            };
        };
    }
};

findAndPrint({
    "Bob": "My name is Bob. I'm 18 years old.",
    "Mary": "Hello, glad to meet you.",
    "Copper": "I'm a college student. Nice to meet you.",
    "Leslie": "I am of legal age in Taiwan.",
    "Vivian": "I will vote for Donald Trump next week",
    "Jenny": "Good morning."
});