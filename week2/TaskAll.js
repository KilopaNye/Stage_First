console.log("=================Task01==================")
function findAndPrint(messages) {
    // 根據自我介紹中出現的語句判斷，
    // 依照18 years old、college student、legal age、vote for Donald Trump等語句推理，
    // 可以得知Bob、Copper、Leslie、Vivian年紀已超過17歲。因此根據相關關鍵字作為判斷依據。
    // your code here, based on your own rules
    let obj = Object.keys(messages);
    for (let g = 0; g < obj.length; g++) {
        let key = obj[g];
        let value = messages[key];
        let arr = value.split(' ');           //將值轉換為分割字符串。
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

console.log("=================Task02==================")

function calculateSumOfBonus(data) {
    // 1.根據薪資保底計算都會給予5%獎金
    // 2.職位:Engineer+500，CEO+1000，Sales+300，工作表現獎金另計。
    // 3.工作表現高於平均值的話額外加800元獎勵金，工作表現維持在標準線上給予400元獎勵金
    // 獎金總計10000台幣。
    let m1 = [];
    let total = 0;


    for (let i = 0; i < data.employees.length; i++) {
        let name = data.employees[i].name;
        let salary = data.employees[i].salary;
        let role = data.employees[i].role;
        let performance = data.employees[i].performance;
        // 用正則表達式先把薪資資料做好篩選處理
        let salaryUSD_Pattern = /USD/;    //正則表達式規則建立
        let salaryTWD_Pattern = /,/;
        if (salaryUSD_Pattern.test(salary)) {
            m1[i] = parseInt(salary);
            m1[i] *= 30;
            m1[i] *= 0.05;
            total += m1[i];
        } else if (salaryTWD_Pattern.test(salary)) {
            m1[i] = parseInt(salary.replace(/,/, ''));
            m1[i] *= 0.05;
            total += m1[i];
        } else {
            m1[i] = salary;
            m1[i] *= 0.05;
            total += m1[i];
        };
        // 判別加成-職位
        if (role === "Engineer") {
            total += 500;
        } else if (role === "CEO") {
            total += 1000;
        } else if (role === "Sales") {
            total += 300;
        };
        //判別加成-工作表現
        if (performance === "above average") {
            total += 800;
        } else if (performance === "average") {
            total += 400;
        } else if (performance === "below average") {
            continue;
        };
    };
    console.log(total);
};
calculateSumOfBonus({
    "employees": [
        {
            "name": "John",
            "salary": "1000USD",
            "performance": "above average",
            "role": "Engineer"
        },
        {
            "name": "Bob",
            "salary": 60000,
            "performance": "average",
            "role": "CEO"
        },
        {
            "name": "Jenny",
            "salary": "50,000",
            "performance": "below average",
            "role": "Sales"
        }
    ]
}); // call calculateSumOfBonus function

console.log("=================Task03==================")

function func(...data) {
    let middle_names = []
    let name = ""
    let axix = 0    //判斷是否要打印"沒有" 假如有打印過資料，則+1，就不會觸發最後的判斷式。
    for (let i = 0; i < data.length; i++) {
        name = data[i][1]
        middle_names.push(name)
    };
    for (let i = 0; i < data.length; i++) {
        let freq = 0;
        name = data[i][1]
        for (let i = 0; i < middle_names.length; i++)
            if (name === middle_names[i]) {
                freq += 1
            };
        if (freq < 2) {
            console.log(data[i])
            axix += 1;            //axix+=1避免觸發""
        }
    };
    if (axix == 0) {
        console.log("沒有")
    }
}
func("彭⼤牆", "王明雅", "吳明"); // print 彭⼤牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有


console.log("=================Task04==================")

function getNumber(index) {
    //#0, 4, 3, 7, 6, 10, 9, 13, 12, 16, 15, …
    // #若index為偶數，則規則為除2加上自身的數值。
    // #若index為奇數，則規則為下一個數字加1，因此index參數先+1做跟偶數同等運算最後再加1即可。
    let answer = 0;
    let num = 0;
    let nums = 0;
    if (index % 2 == 0) {
        answer = index / 2;
        answer += index;
        console.log(answer);
    } else {
        nums = index + 1;
        num = nums / 2;
        nums += num;
        nums += 1;
        console.log(Number(nums))
    };
};
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15

console.log("=================Task05==================")

function findIndexOfCar(seats, status, number) {
    let serve_seats = [];
    for (let i = 0; i < seats.length; i++) {
        if (status[i] === 1 && seats[i] >= number) {
            serve_seats.push(seats[i]);
        }
    }
    // console.log(Math.min(serve_seats))
    let member = Math.min(...serve_seats); //找到提供服務的車廂最小值 使用展開運算符展開陣列
    console.log(seats.indexOf(member))     //#打印最小值車廂的位置，沒有的話會回傳-1
}
findIndexOfCar([3, 1, 5, 4, 2], [0, 1, 0, 1, 1], 2); // print 4
findIndexOfCar([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
findIndexOfCar([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2