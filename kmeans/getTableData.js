var data = [];
var tableRows = document.querySelector("tbody").querySelectorAll("tr");

const tableRowsList = Array.prototype.filter.call(tableRows, (item) => item.style.display !== "none");

for (let i = 1; i < 101; i++) {
    getDataFromRows(tableRowsList[i])
};

function getDataFromRows(row) {
    let rowDetails = {};
    if (row.style.display !== "none") {
        var rowCells = row.children;
        rowDetails["country"] = rowCells[1].innerText;
        rowDetails["totalDeaths"] = rowCells[4].innerText;
        rowDetails["population"] = rowCells[13].innerText;

    }

    data.push(rowDetails);
}


return JSON.stringify(data);