var movieDetails = {
    "director": "",
    "runTime": ""
}

movieDetails["director"] = document.querySelector(".profile").children[0].innerText
movieDetails["runTime"] = document.querySelector(".runtime").innerText

return movieDetails;