function GoForm() {
    document.querySelector(".signup-form").onsubmit = function (event) {
        let count_name = document.querySelector("#count_name").value;
        let user_count = document.querySelector("#user_count").value;
        let password = document.querySelector("#password").value;
        console.log(count_name)
        if (count_name.length < 1 || user_count.length < 1 || password.length < 1) {
            alert("不得為空，請正確填寫表單");
            event.preventDefault(); // 阻止表單提交
        };
    };
};

function signin() {
    document.querySelector(".login-form").onsubmit = function (event) {
        let user_count = document.querySelector("#login-count").value;
        let password = document.querySelector("#login-password").value;
        console.log(count_name)
        if (user_count < 1 || password < 1) {
            alert("不得為空，請正確填寫表單");
            event.preventDefault(); // 阻止表單提交
        };
    };
};


