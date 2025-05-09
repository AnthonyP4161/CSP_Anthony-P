function reveal(){
    if (document.getElementById("hidden").src === "https://www.nps.gov/cany/planyourvisit/images/_DSC4737.jpg?maxwidth=1300&maxheight=1300&autorotate=false") {
      document.getElementById("hidden").src= "https://www.ulumresorts.com/app/uploads/2023/04/shutterstock_1801854883.jpg";
      document.getElementById("credits").innerHTML = "Image by ulumresorts.com"
    } else {
      document.getElementById("hidden").src = "https://www.nps.gov/cany/planyourvisit/images/_DSC4737.jpg?maxwidth=1300&maxheight=1300&autorotate=false";
      document.getElementById("credits").innerHTML = "Image by Neal Herbert on nps.gov"
    }
}


function hover(){
  document.getElementById("image1").src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWJSdHQWu2lMHKPqI2S2wLK3MvBiqRc6JO8Q&s"
  document.getElementById("credits1").innerHTML = "Image by offthebeatenpath.com"
}

function leave(){
  document.getElementById("image1").src = "https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Green_River_Overlook_Ekker_Butte.jpg/1920px-Green_River_Overlook_Ekker_Butte.jpg"
  document.getElementById("credits1").innerHTML = "Image by au-ears on wikipedia.org"
}
