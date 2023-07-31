function GoForm(){
    document.querySelector(".login-form").onsubmit = function(event){
        let checkbox = document.querySelector(".agree-check")
        if(!checkbox.checked){
            alert('請先閱讀同意條款並打勾確認');
            event.preventDefault(); // 阻止表單提交
        }
    }
}
function GoCal() {
    let calText = document.querySelector(".cal-text");
    let calTextValue = calText.value;
    let num = Number(calTextValue);
    if (Number.isInteger(num) != true || num < 1) {
        alert('請輸入一個正整數');
    } else {
        window.location.href = '/square/' + num;
    };
};