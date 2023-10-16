
var auth_button_submit = document.querySelector("#auth_submit");

var auth_userlogin = document.querySelector("#auth_userlogin");
var auth_pass1 = document.querySelector("#auth_pass1");

var auth_userlogin_status = document.querySelector("#auth_userlogin_status");
var auth_pass1_status = document.querySelector("#auth_userpass1_status");


var auth_userlogin_val = "";
var auth_pass1_val = "";



function auth_get_values() {

    auth_userlogin_val = auth_userlogin.value;
    auth_pass1_val = auth_pass1.value;


}


function val_to_json() {

    var val_json = {
        login: auth_userlogin_val,
        pass: auth_pass1_val
    };

      
    var json = JSON.stringify(val_json);
    return json;
}


function validate_userlogin(userlogi) {
    const regex = /^[a-zA-Z0-9_]{2,15}$/;
    return regex.test(userlogi);
  }
function validate_pass(pass) {
    const regex = /^.*(?=.{8,})(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*? ]).*$/;
    return regex.test(pass);
  }




function valid_data() {

    var error_data = [];
 
    if (validate_userlogin(auth_userlogin_val)) {
        auth_userlogin_status.textContent = "ok";
        auth_userlogin_status.style.color = "green";
    }else{
        error_data.push("login");
        auth_userlogin_status.textContent = "error";
        auth_userlogin_status.style.color = "red";
    }

    if (validate_pass(auth_pass1_val)) {
        auth_pass1_status.textContent = "ok";
        auth_pass1_status.style.color = "green";
    }else{
        error_data.push("pass1");
        auth_pass1_status.textContent = "error";
        auth_pass1_status.style.color = "red";
    }


    return error_data.length

}



function submit_auth(date){

    fetch('/adm/auth/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: date,
      })
        .then((response) => response.json())
        .then((data) => {
            var status = data["status"];
            console.log(data);

            if (status == 1) {
                alert("Вы успешно авторизовались \n переходим на страницу  админки");
                setCookie('access_token', data["access_token"], {'max-age': 1200, path: '/'});
                setCookie('refresh_token', data["refresh_token"], {'max-age': 86400, path: '/'});
                
                alert(getCookie('access_token'));
                alert(getCookie('refresh_token'));
                
                // window.location.href = '/adm/';
                
            }else if (status == 2){
                alert("неверный пароль");
            }else if (status == 3){
                alert("неверный логин");
            }else if (status == 4){
                alert("ошибка базы данных");
            }else if (status == 5){
                alert("не прошол валидацию на сервере");
            }else{
                alert("ошибка сервера");
            }

        })
        .catch((error) => {
            alert("error");
          console.log('Error:', error);
        });
}





auth_button_submit.addEventListener("click", function(e) {

    auth_get_values();
    console.log(val_to_json());
    var v_d = valid_data()
    if(v_d === 0){
        submit_auth(val_to_json());
    }else{
        alert(`у вас ${v_d} ошибок`)
    }




});

var test_btn_1 = document.querySelector("#test_btn_1");

test_btn_1.addEventListener("click", function(e) {
    
    var test_date = {'access_token': getCookie('access_token'), 'refresh_token': getCookie('refresh_token')}

    // const myHeaders = new Headers();

        // myHeaders.append('Content-Type', 'application/json');
        // myHeaders.append('Authorization', '1234abcd');
console.log(typeof getCookie("access_token"))
console.log( getCookie("access_token"))

    fetch('/adm/test_jwt/', {
        method: 'POST',
        headers: {
            // 'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + getCookie("access_token")
        },
        body: test_date,
      })
        .then((response) => response.json())
        .then((test_date) => {
            console.log(test_date)

        })
        .catch((error) => {
            alert("error");
          console.log('Error:', error);
        });


});
