function toggle() {
    let button = document.getElementsByClassName('button')[0]
    console.log(button.innerText)
    if (button.innerText == 'MORE'){
        button.innerText = 'Less'
        document.getElementById('extra').style.display = 'block'
    } else {
        button.innerText = 'More'
        document.getElementById('extra').style.display = 'none'
    }
}