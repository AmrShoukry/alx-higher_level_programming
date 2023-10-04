let dataURL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
let nameDiv = $('DIV#character');

$.get(dataURL, function (data, textStatus) {
    nameDiv.text(data['name']);
})
