document.addEventListener("DOMContentLoaded", () => {
    // Show the first tab by default
    document.querySelector(".tab-button").click();
});

function openTab(evt, tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll(".tab-content");
    tabContents.forEach(content => content.classList.remove("active"));

    // Remove active class from all tab buttons
    const tabButtons = document.querySelectorAll(".tab-button");
    tabButtons.forEach(button => button.classList.remove("active"));

    // Show the current tab content and add active class to the button
    document.getElementById(tabName).classList.add("active");
    evt.currentTarget.classList.add("active");
}

function searchTable() {
    let input, filter;
    input = document.getElementById("searchInput");
    filter = input.value.toLowerCase();

    const xhr = new XMLHttpRequest();
    xhr.open("GET", "search.php?query=" + filter, true);
    xhr.onload = function () {
        if(xhr.status === 200) {
            document.getElementById("tableData").innerHTML = xhr.responseText;
        }
    };
    xhr.send();
}
