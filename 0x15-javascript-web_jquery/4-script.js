let button = $('DIV#toggle_header');
let header = $('header');

button.click(function () {
    if (header.hasClass('red')) {
        header.addClass('green');
        header.removeClass('red');
    }
    else {
        header.addClass('red');
        header.removeClass('green');
    }
});
