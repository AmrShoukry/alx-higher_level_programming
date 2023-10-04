$(document).ready(function () {

    dataURL = 'https://www.fourtonfish.com/hellosalut/hello/';
    translateButton = $('INPUT#btn_translate');
    helloDiv = $('DIV#hello');

    translateButton.click(function() {
        lang = $('INPUT#language_code').val();
        $.get(dataURL, function (data, textStatus) {
            helloDiv.text(data[lang]);
        })    
    })
});