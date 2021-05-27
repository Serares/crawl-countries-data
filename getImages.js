var imagesElements = document.querySelectorAll("a[class=image]")
var returnedElements = [];
for (var i = 0; i < 10; i++) {
    returnedElements.push(imagesElements[i].href)
}
return returnedElements;
