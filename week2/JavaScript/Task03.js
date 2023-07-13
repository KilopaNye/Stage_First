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
