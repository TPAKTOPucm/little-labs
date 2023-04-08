function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick)
   let data = document.getElementsByTagName('tbody')[0]
   let result = document.getElementById('result')
   result.style.textAlign = 'center'
   function onClick() {
      let text = document.getElementById('searchField').value
      let num = 0
      for(let tr of data.getElementsByTagName('tr')){
         if (tr.innerText.includes(text)) {
            num++
            tr.className = 'select'
         } else {
            tr.className = ''
         }
      }
      result.innerText = num + " matches found"
   }
}