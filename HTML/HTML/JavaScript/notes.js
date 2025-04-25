function hello(){
    document.getElementById("title").style.color = "green"
}
function hi(){
    let name = window.prompt("What the sigma is yo name?", "Sensei Sigma")
    document.getElementById("title").innerHTML = "Hi " + name + "!"
}
function restart(){
    document.getElementById("title").innerHTML = "JS Notes"
    document.getElementById("title").style.color = "black"
}
function hidden(){
    document.getElementById("meme").style.display = "block"
}
function pop(){
    window.alert("Bro, just don't click dat!")
}
function show(){
    document.getElementById("lost").style.display="block"
}
function reveal(){
    document.getElementById("hidden").style.display="block"
}