var database = firebase.database();
var dbRef = database.ref('data');
var statusRef = dbRef.child('status')

var array = [];

dbRef.on('value', function(snapshot) {
    snapshot.forEach(function(child) {
        array += (child.key, child.val())
        if (child.key == "temp") {
            document.getElementById("temp").innerHTML = child.val() + "&deg;C";
        } else if (child.key == "humi") {
            document.getElementById("humi").innerHTML = child.val() + "%";
        } else if (child.key == "status") {
            if (child.val() == 1) {
                document.getElementById("status").innerHTML = "Boiler is ON"
            } else {
                document.getElementById("status").innerHTML = "Boiler is OFF"
            }
        }
    });
});


function turnOn() {
    dbRef.update({
        status: 1
    });
    database.child("data").update(status)
}

function turnOff() {
    dbRef.update({
        status: 0
    });
    database.child("data").update(status)
}
