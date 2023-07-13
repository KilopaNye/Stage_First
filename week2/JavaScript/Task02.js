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
        } else if(role === "Sales"){
            total += 300;
        };
        //判別加成-工作表現
        if (performance === "above average") {
            total += 800;
        } else if (performance === "average") {
            total += 400;
        } else if(performance === "below average"){
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