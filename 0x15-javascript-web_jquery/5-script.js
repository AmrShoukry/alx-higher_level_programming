let button = $('DIV#add_item');
let ul = $('UL.my_list');
let item = '<li>Item</li>';

button.click(function () {
    ul.append(item)
});
