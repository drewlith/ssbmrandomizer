let disableTabs = false;
function highlight(item) {
    if (disableTabs == true) {
        return;
    }
    if (item.getAttribute("data") === "inactive") {
      item.style.backgroundColor = "#0000FFFF";
    }
  }
function removeHighlight(item) {
    if (disableTabs == true) {
        return;
    }
    if (item.getAttribute("data") === "inactive") {
        item.style.backgroundColor = "#0000FF88";
    }
}
function setActive(item) {
    if (disableTabs == true) {
        return;
    }
    const labels = [document.getElementById("attack-label"),
                    document.getElementById("throw-label"),
                    document.getElementById("attribute-label"),
                    document.getElementById("gecko-label"),
                    document.getElementById("secret-label")];
    for (let i = 0; i < labels.length; i++) {
        if (labels[i].getAttribute("id") === item.getAttribute("id")) {
            labels[i].setAttribute("data", "active");
            labels[i].style.backgroundColor = "#F0F0F0";
            labels[i].style.color = "#0000FFFF"
        } else {
            labels[i].setAttribute("data", "inactive");
            labels[i].style.backgroundColor = "#0000FF88";
            labels[i].style.color = "#FFCC00";
        }
    }
}
setActive(document.getElementById("attack-label"));