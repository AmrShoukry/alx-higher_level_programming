let dataURL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
let ul = $('UL#list_movies');

$.get(dataURL, function (data, textStatus) {
    $.each(data['results'], function (index, item) {
        ul.append(`<li>${item['title']}</li>`);
    })
})
