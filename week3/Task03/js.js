//選單的縮放，使用hide的方法
function hiden() {
    let hide = document.querySelector(".hide");
    let nav = document.querySelector(".menuIcon");
    if (hide.style.display == "none" || hide.style.display == "") { //加上或為空值，解決要按兩次才執行函式的問題
        hide.style.display = "block";
        nav.style.display = "none";
    } else {
        hide.style.display = "none";
        nav.style.display = "block";
    };
};

/*改善放大螢幕寬度時漢堡圖還存在的問題*/
window.onload = function () {//當載入網頁後執行函式
    function resize() {
        let nav = document.querySelector(".menuIcon");
        if (window.innerWidth > 600) {   //偵測到螢幕寬度大於600px後運行函式
            nav.style.display = "none";
        } else {
            nav.style.display = "block";  //小於600px記得要恢復block設定
        };
    };
    resize()
    window.addEventListener('resize', resize, false);	// 持續偵聽事件 resize
};


// ------------------------星星的函式-------------------------------

// let star = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
// function gray(number) {
//     let gray = document.querySelector(".gray-" + number);/*選取要操作的標籤，從0開始*/
//     if (star[number] == 0) {/*判定star的值是不是0*/
//         gray.style.filter = "grayscale(0)";//操作gray的classStyle
//         star[number] += 1;
//     } else {
//         gray.style.filter = "grayscale(1)";
//         star[number] = 0;
//     };
// };


fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function (response) {
    return response.json();
}).then(function (data) {
    // 前三個方框內容生成
    let subs;
    for (let j = 1; j < 4; j++) {
        let first = document.querySelector(".box" + j);
        // 創建fragment 虛擬DOM 不影響現有原生文件
        let fragment = document.createDocumentFragment();

        // 照片區塊、以及整理網址
        let httpConnect = String(data["result"]["results"][j]["file"]);
        subs = httpConnect.split(".jpg");  //分割網址
        let img = document.createElement("img");
        img.src = subs[0] + ".jpg";  //新增圖片網址
        img.classList.add("img");  //新增圖片class
        // 先將東西加到fragment階層，後面再一次把全部的fragment加到first階層中。
        fragment.appendChild(img);

        // 文字方塊生成
        let div = document.createElement("div");
        div.classList.add("photoTxt");
        div.appendChild(document.createTextNode(data["result"]["results"][j]["stitle"]));
        fragment.appendChild(div);
        first.appendChild(fragment);

    };
    for (let i = 4; i < 16; i++) {
        //選擇父層
        let second = document.querySelector(".box" + i);
        let fragmentSecond = document.createDocumentFragment();
        // 照片區塊、以及整理網址
        let httpConnect = String(data["result"]["results"][i]["file"]);
        // 因為有結尾是大寫JPG，因此使用判斷式進行篩選
        if (i == 12) {
            subs = httpConnect.split(".JPG");  //分割網址
            let img2 = document.createElement("img");
            img2.src = subs[0] + ".JPG";
            img2.classList.add("img2");  //新增圖片class
            // 先將東西加到fragmentSecond階層，後面再一次把全部的fragmentSecond加到second階層中。
            fragmentSecond.appendChild(img2);
            second.appendChild(fragmentSecond);
        } else {
            subs = httpConnect.split(".jpg");  //分割網址
            let img2 = document.createElement("img");
            img2.src = subs[0] + ".jpg";
            img2.classList.add("img2");  //新增圖片class
            // 先將東西加到fragmentSecond階層，後面再一次把全部的fragmentSecond加到second階層中。
            fragmentSecond.appendChild(img2);
            second.appendChild(fragmentSecond);
        };
        //------------------------------以下為欲新增的標籤---------------------------------
        //添加文字BOX
        let opacityDiv = document.createElement("div");
        opacityDiv.classList.add("opacity","num"+i);
        fragmentSecond.appendChild(opacityDiv);
        second.appendChild(fragmentSecond);

        //建立BOX內文字，以及添加class
        let secondText = document.querySelector(".num" + i);
        let div = document.createElement("div");
        div.classList.add("photoTxt2");
        div.appendChild(document.createTextNode(data["result"]["results"][i]["stitle"]));
        fragmentSecond.appendChild(div);
        secondText.appendChild(fragmentSecond);
    };
});

// 參考架構
    // <div class="secondPhoto" >
    //         <img src="image/food.jpg" class="img2">
    //         <div class="opacity">
    //             <div class="photoTxt2">Title 1</div>
    //         </div>
    //     </div>