window.onload = function(){
    document.querySelector(".login-form").onsubmit = function(){
        let checkbox = document.querySelector(".agree-check")
        if(!checkbox.checked){
            alert('請先閱讀同意條款並打勾確認');
            return false; // 阻止表單提交
        }
    }
}