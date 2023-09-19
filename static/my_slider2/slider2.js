
var slider_cont = document.querySelector('#slider_container');

var slider_card = document.querySelector('.slider_card_img');

var slider_card_left = document.querySelector('#slider_card_left_img');
var slider_card_focus = document.querySelector('#slider_card_focus_img');
var slider_card_right = document.querySelector('#slider_card_right_img');

var slider_cont_down = false;
var slider_cont_move = 0;
var slider_cont_up = false;
var start_move = 0;
var end_move = 0;

var left_card = 0;
var current_card = 1;
var right_card = 2;

const slider_images = [
    'static/img/img1.jpg',
    'static/img/img2.jpg',
    'static/img/img3.jpg',
    'static/img/img4.jpg',
    'static/img/img5.jpg'
];


    slider_card_left.style.backgroundImage =  "url(" + slider_images[left_card] + ")";
    slider_card_focus.style.backgroundImage = "url(" + slider_images[current_card] + ")";
    slider_card_right.style.backgroundImage = "url(" + slider_images[right_card] + ")";


function slider_image_install(direction) {
    if(direction == 'left'){
        left_card -= 1;
        current_card -= 1;
        right_card -= 1;
    }
    if(direction == 'right'){
        left_card += 1;
        current_card += 1;
        right_card += 1;
    }
    console.log(left_card);
    slider_card.style.opacity = "0.5";

    slider_card_left.style.backgroundImage =  "url(" + slider_images[left_card] + ")";
    slider_card_focus.style.backgroundImage = "url(" + slider_images[current_card] + ")";
    slider_card_right.style.backgroundImage = "url(" + slider_images[right_card] + ")";

    slider_card.style.opacity = "1";
}
slider_card_left.addEventListener('click', (event) => {
    slider_image_install('left');
});
slider_card_right.addEventListener('click', (event) => {
    slider_image_install('right');
});


slider_cont.addEventListener('touchstart', (event) => {
    slider_cont_down = true;
    start_move = event.changedTouches[0].pageX;
});
slider_cont.addEventListener('mousedown', (event) => {
    slider_cont_down = true;
    start_move = event.clientX;
});


slider_cont.addEventListener('touchmove', (event) => {
});
slider_cont.addEventListener('mousemove', (event) => {
});


slider_cont.addEventListener('touchend', (event) => {
    if(slider_cont_down){
        end_move = event.changedTouches[0].pageX;
        if(start_move - end_move < -100){
            slider_image_install('left');
        }
        if(start_move - end_move > 100){
            slider_image_install('right');
        }
        slider_cont_down = false;
    }
    
});
slider_cont.addEventListener('mouseup', (event) => {
    if(slider_cont_down){
        end_move = event.clientX;
        if(start_move - end_move < -100){
            slider_image_install('left');
        }
        if(start_move - end_move > 100){
            slider_image_install('right');
        }
        slider_cont_down = false;
    }
});