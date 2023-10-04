$(document).ready(function () {

    translateButton = $('INPUT#btn_translate');
    helloDiv = $('DIV#hello');

    translateButton.click(function() {
        lang = $('INPUT#language_code').val();
        dataURL = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;

        $.get(dataURL, function (data, textStatus) {
            helloDiv.text(data['hello']);
        })    
    })

    $('#language_code').keypress(function(event) {
        if (event.which === 13) {
            lang = $('INPUT#language_code').val();
            dataURL = `https://hellosalut.stefanbohacek.dev/?lang=${lang}`;
            $.get(dataURL, function (data, textStatus) {
                helloDiv.text(data['hello']);
            })    
        }
    });
});
