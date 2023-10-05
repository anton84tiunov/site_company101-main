
var reg_button_submit = document.querySelector("#reg_submit");

var reg_usersurname = document.querySelector("#reg_usersurname");
var reg_username = document.querySelector("#reg_username");
var reg_userpatronymic = document.querySelector("#reg_userpatronymic");
var reg_userphone = document.querySelector("#reg_userphone");
var reg_userdate_birth = document.querySelector("#reg_userdate_birth");
var reg_useremail = document.querySelector("#reg_useremail");
var reg_userlogin = document.querySelector("#reg_userlogin");
var reg_pass1 = document.querySelector("#reg_pass1");
var reg_pass2 = document.querySelector("#reg_pass2");

var reg_usersurname_status = document.querySelector("#reg_usersurname_status");
var reg_username_status = document.querySelector("#reg_username_status");
var reg_userpatronymic_status = document.querySelector("#reg_userpatronymic_status");
var reg_userphone_status = document.querySelector("#reg_userphone_status");
var reg_userdate_birth_status = document.querySelector("#reg_userdate_birth_status");
var reg_useremail_status = document.querySelector("#reg_useremail_status");
var reg_userlogin_status = document.querySelector("#reg_userlogin_status");
var reg_pass1_status = document.querySelector("#reg_userpass1_status");
var reg_pass2_status = document.querySelector("#reg_userpass2_status");




var reg_usersurname_val = "";
var reg_username_val = "";
var reg_userpatronymic_val = "";
var reg_userphone_val = "";
var reg_userdate_birth_val = "";
var reg_useremail_val = "";
var reg_userlogin_val = "";
var reg_pass1_val = "";
var reg_pass2_val = "";



function reg_get_values() {
    
    reg_usersurname_val = reg_usersurname.value;
    reg_username_val = reg_username.value;
    reg_userpatronymic_val = reg_userpatronymic.value;
    reg_userphone_val = reg_userphone.value;
    reg_userdate_birth_val = reg_userdate_birth.value;
    reg_useremail_val = reg_useremail.value;
    reg_userlogin_val = reg_userlogin.value;
    reg_pass1_val = reg_pass1.value;
    reg_pass2_val = reg_pass2.value;

}


function val_to_json() {

    var val_json = {
        usersurname: reg_usersurname_val,
        username: reg_username_val,
        userpatronymic: reg_userpatronymic_val,
        userphone: reg_userphone_val,
        userdate_birth: reg_userdate_birth_val,
        useremail: reg_useremail_val,
        userlogin: reg_userlogin_val,
        pass1: reg_pass1_val
    };

      
    var json = JSON.stringify(val_json);
    return json;
}


function validate_username(username) {
    const regex = /^[A-Za-z]{2,15}$/;
    return regex.test(username);
  }

function validate_userphone(userphone) {
    const regex = /^8[0-9]{10}$/;
    return regex.test(userphone);
  }
function validate_userdate_birth(userdate_birth) {
    const regex = /[0-9]{4}\-[0-9]{2}\-[0-9]{2}/;
    return regex.test(userdate_birth);
  }
function validate_useremail(email) {
    const regex = /^[a-z0-9.]{2,20}@[a-z0-9.]{2,20}$/;
    return regex.test(email);
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

    if (validate_username(reg_usersurname_val)) {
        reg_usersurname_status.textContent = "ok";
        reg_usersurname_status.style.color = "green";
    }else{
        error_data.push("surname");
        reg_usersurname_status.textContent = "error";
        reg_usersurname_status.style.color = "red";
    }

    if (validate_username(reg_username_val)) {
        reg_username_status.textContent = "ok";
        reg_username_status.style.color = "green";
    }else{
        error_data.push("name");
        reg_username_status.textContent = "error";
        reg_username_status.style.color = "red";
    }

    if (validate_username(reg_userpatronymic_val)) {
        reg_userpatronymic_status.textContent = "ok";
        reg_userpatronymic_status.style.color = "green";
    }else{
        error_data.push("patronymic");
        reg_userpatronymic_status.textContent = "error";
        reg_userpatronymic_status.style.color = "red";
    }
 
    if (validate_userphone(reg_userphone_val)) {
        reg_userphone_status.textContent = "ok";
        reg_userphone_status.style.color = "green";
    }else{
        error_data.push("phone");
        reg_userphone_status.textContent = "error";
        reg_userphone_status.style.color = "red";
    }

    if (validate_userdate_birth(reg_userdate_birth_val)) {
        reg_userdate_birth_status.textContent = "ok";
        reg_userdate_birth_status.style.color = "green";
    }else{
        error_data.push("date_birth");
        reg_userdate_birth_status.textContent = "error";
        reg_userdate_birth_status.style.color = "red";
    }

    if (validate_useremail(reg_useremail_val)) {
        reg_useremail_status.textContent = "ok";
        reg_useremail_status.style.color = "green";
    }else{
        error_data.push("emai");
        reg_useremail_status.textContent = "error";
        reg_useremail_status.style.color = "red";
    }
 
    if (validate_userlogin(reg_userlogin_val)) {
        reg_userlogin_status.textContent = "ok";
        reg_userlogin_status.style.color = "green";
    }else{
        error_data.push("login");
        reg_userlogin_status.textContent = "error";
        reg_userlogin_status.style.color = "red";
    }

    if (validate_pass(reg_pass1_val)) {
        reg_pass1_status.textContent = "ok";
        reg_pass1_status.style.color = "green";
    }else{
        error_data.push("pass1");
        reg_pass1_status.textContent = "error";
        reg_pass1_status.style.color = "red";
    }

    if (validate_pass(reg_pass2_val)) {
        reg_pass2_status.textContent = "ok";
        reg_pass2_status.style.color = "green";
    }else{
        error_data.push("pass2");
        reg_pass2_status.textContent = "error";
        reg_pass2_status.style.color = "red";
    }

    return error_data.length

}



function submit_reg(date){

    fetch('/adm/reg/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: date,
      })
        .then((response) => response.json())
        .then((data) => {
            var status = data["status"];
            if (status == 1) {
                alert("Вы успешно зарегистрировались \n переходим на страницу авторизации");
                window.location.href = '/adm/auth/';
            }else if (status == 2){
                alert("почта используется");
            }else if (status == 3){
                alert("логие используется");
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





reg_button_submit.addEventListener("click", function(e) {

    reg_get_values();
    console.log(val_to_json());
    var v_d = valid_data()
    if(v_d === 0){
        submit_reg(val_to_json());
    }else{
        alert(`у вас ${v_d} ошибок`)
    }




});




