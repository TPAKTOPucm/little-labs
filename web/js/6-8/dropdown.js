function addItem() {
    document.getElementById('menu').innerHTML += '<option value="' + document.getElementById('newItemValue').value + '">' + document.getElementById('newItemText').value + '</option>'
}