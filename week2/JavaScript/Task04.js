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
    }else{
        nums = index+1;
        num=nums/2;
        nums+=num;
        nums+=1;
        console.log(Number(nums))
    };
};
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15
