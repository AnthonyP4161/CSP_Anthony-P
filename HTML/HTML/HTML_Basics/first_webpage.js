function reveal(){
    var x = document.getElementById("invisible")
    var y = document.getElementById("hidden").innerHTML = "Hi";
    if (x.style.display === "none") {
        x.style.display = "block";
      } else {
        x.style.display = "none";
      }
    
    
}


function hover(){
    document.getElementById("img").src = "https://www.pngplay.com/wp-content/uploads/13/Pug-PNG-Images-HD.png"
}

function leave(){
    document.getElementById("img").src = "https://images.vexels.com/media/users/3/300494/isolated/preview/e94c110b68f40df08116e06f9f5e22f2-cute-pug-dog-sitting-down.png"
}