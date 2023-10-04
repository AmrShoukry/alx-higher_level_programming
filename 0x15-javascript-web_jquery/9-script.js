let dataURL = 'https://fourtonfish.com/hellosalut/?lang=fr';
let div = $('DIV#hello');

$(document).ready(function () {
    $.get(dataURL, function (data, textStatus) {
        div.text(data['hello']);
    })    
}) 

