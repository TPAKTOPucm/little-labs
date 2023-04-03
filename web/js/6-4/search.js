function search() {
   let num = 0
   let text = document.getElementById('searchText').value
   for (let el of document.getElementsByTagName('li')){
      if (el.innerText.includes(text)) {
         num++
         el.style.fontWeight = 'bold'
      } else {
         el.style.fontWeight = 'normal'
      }
   }
   document.getElementById('result').innerText = num + " matches found"
}