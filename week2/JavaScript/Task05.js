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