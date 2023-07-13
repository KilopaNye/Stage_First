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
