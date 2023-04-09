function lockedProfile() {
  let showButtons = document.getElementsByTagName('button')
  for (let button of showButtons){
    button.addEventListener('click', () => {
      let parentDiv = button.parentNode
      let hiddenFields = parentDiv.getElementsByTagName('div')[0]
      if (parentDiv.querySelector('input[value="unlock"]').checked == false) {
        return
      }
      if (button.innerText == "Show more"){
        button.innerText = "Hide it"
        hiddenFields.style.display = 'block'
      } else {
        button.innerText = "Show more"
        hiddenFields.style.display = 'none'
      }
    })
  }
}