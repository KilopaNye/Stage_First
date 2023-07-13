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

let star = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
function gray(number) {
    let gray = document.querySelector(".gray-" + number);/*選取要操作的標籤，從0開始*/
    if (star[number] == 0) {/*判定star的值是不是0*/
        gray.style.filter = "grayscale(0)";//操作gray的classStyle
        star[number] += 1;
    } else {
        gray.style.filter = "grayscale(1)";
        star[number] = 0;
    };
};