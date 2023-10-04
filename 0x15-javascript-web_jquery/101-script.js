$(document).ready(function () {
    let ul = $('UL.my_list');
    
    let item = '<li>Item</li>';

    let addButton = $('DIV#add_item');
    let removeButton = $('DIV#remove_item');
    let clearButton = $('DIV#clear_list');

    addButton.click(function () {
        ul.append(item);
    })

    removeButton.click(function() {
        $('UL.my_list li:last').remove();
    })

    clearButton.click(function() {
        $.each(ul, function(index, element) {
            element.remove();
        })
    })
})

