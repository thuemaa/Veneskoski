
$(document).ready(function() {

    /*Map var*/
    var soikkamap;

    loadMap();
});

/*Loads the map into variable*/
function loadMap() {
    soikkamap = L.map('kartta_div').setView([21.505, -15.19], 13);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
        '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
        'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1IjoidGh1ZW1hcyIsImEiOiJjanFsZWRoaGwwbHN0M3hxbnY2aTRqeGVtIn0.9UJgz8O3n3f_ftfMiCpuvg'
    }).addTo(soikkamap);
}

