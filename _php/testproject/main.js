if (!String.prototype.toFString) {
    String.prototype.toFString = function () {
        var args = arguments;
        return this.replace(/{(\d+)}/g, function (match, number) {
            return typeof args[number] != 'undefined'
                ? args[number]
                : match;
        })
    }
}

function sayHi(elem) {
    let name = elem.id;
    alert("Hello, Boddy! I'm {0}".toFString(name));
}

document.querySelectorAll('.row').forEach(row => {
    row.onclick = ev => sayHi(ev.target);
})
