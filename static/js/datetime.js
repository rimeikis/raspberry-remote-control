function display_dateTime() {
    var refreshRate = 1000;
    mytime = setTimeout('getDateTime()', refreshRate)
}

function addZero(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

function getDateTime() {
    var d = new Date();

    var hr = addZero(d.getHours());
    var mi = addZero(d.getMinutes());
    var sec = addZero(d.getSeconds());
    var month = addZero(d.getMonth());
    var day = addZero(d.getDate());

    var n = `${hr}:${mi}:${sec} ${day}-${month}-${d.getFullYear()}`;
    document.getElementById('date').innerHTML = n;
    display_dateTime();
}
