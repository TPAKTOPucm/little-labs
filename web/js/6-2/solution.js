function solve() {
    let have = document.getElementsByTagName('input')
    let result = ''
    switch (have[1].value.toLowerCase()) {
        case "pascal case":
            have[0].value.split(" ").forEach(subStr => result += subStr[0].toUpperCase() + subStr.substring(1).toLowerCase())
            break
        case "camel case":
            have[0].value.split(" ").forEach(subStr => result += subStr[0].toUpperCase() + subStr.substring(1).toLowerCase())
            result = result.charAt(0).toLowerCase() + result.substring(1)
            break
        default:
            result = 'Error!'
    }
    document.getElementById('result').innerText += result
}