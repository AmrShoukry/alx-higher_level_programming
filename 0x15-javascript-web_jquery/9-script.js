$(document).ready(function () {
    let dataURL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    let div = $('DIV#hello');

    $.get(dataURL, function (data, textStatus) {
        div.text(data['hello']);
    })    
}) 

