
var menu = document.querySelector(".menu");
var menu_checkbox = document.querySelector("#menu-checkbox");

menu_checkbox.addEventListener('change', function(e) {
  document.body.style.overflow = e.target.checked === true ? 'hidden' : '';
});

menu.addEventListener("mousemove", function(event) {
  document.body.style.overflow = 'hidden';
});

menu.addEventListener("mouseout", function(event) {
  document.body.style.overflow = 'scroll';
});


document.getElementById("menu-header")
  .addEventListener('wheel', function(event) {
    if (event.deltaMode == event.DOM_DELTA_PIXEL) {
      var modifier = 1;
      // иные режимы возможны в Firefox
    } else if (event.deltaMode == event.DOM_DELTA_LINE) {
      var modifier = parseInt(getComputedStyle(this).lineHeight);
    } else if (event.deltaMode == event.DOM_DELTA_PAGE) {
      var modifier = this.clientHeight;
    }
    if (event.deltaY != 0) {
      // замена вертикальной прокрутки горизонтальной
      this.scrollLeft += modifier * event.deltaY;
      event.preventDefault();
    }
  });
