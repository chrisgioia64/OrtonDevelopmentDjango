let map;

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 37.8, lng: -122.239 },
    zoom: 10,
  });

  $.getJSON('/developments/developments.json', function (j) {
    json = j['developments'];
    console.log('length: ' + json.length);
    const infoWindow = new google.maps.InfoWindow();

    for (let i = 0; i < json.length; i++) {
      let data = json[i];
      console.log(data);
      let lat = Number(data['lat']);
      let lng = Number(data['lng']);
      console.log(data['img']);
      const pos = {
        lat: lat,
        lng: lng,
      };
      const marker = new google.maps.Marker({
        position: pos,
        map: map,
      });

      marker.addListener('click', () => {
        boxText = document.createElement('html');
        boxText.innerHTML = '<head>';
        boxText.innerHTML += '</head><body>';
        boxText.innerHTML +=
          '<div id="thumbnail_text"><a href="' +
          data['id'] +
          '">' +
          data['name'] +
          '</a></div>';
        // boxText.innerHTML += data['address'] + '<br>';
        boxText.innerHTML +=
          '<img id="thumbnail_img" src="/media/' +
          data['img'] +
          "\" width='200px'>";
        boxText.innerHTML += '</body>';

        infoWindow.close();
        infoWindow.setContent(boxText);
        infoWindow.open(marker.getMap(), marker);
      });
    }
    // console.log(json); // this will show the info it in firebug console
  });
}
