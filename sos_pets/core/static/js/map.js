function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: { lat: -23.9541, lng: -46.3333 }, // Exemplo Praia Grande
    });

    map.addListener('click', function (e) {
        placeMarker(e.latLng, map);
        document.getElementById('localizacao').value = e.latLng.lat() + ", " + e.latLng.lng();
    });

    function placeMarker(location, map) {
        new google.maps.Marker({
            position: location,
            map: map,
        });
    }
}
