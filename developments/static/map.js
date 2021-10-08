let map;
// import { MarkerClusterer } from '@googlemaps/markerclusterer';

// $(function () {
//   $.when(
//     $.getScript('/script1'),
//     $.getScript('/scirpt2'),
//     $.getScript('/script3')
//   );
// }).done(function () {
//   // do stuff with the contents of my new script files
// });

function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 39, lng: -100.239 },
    zoom: 5,
  });

  $.getJSON('/developments/developments.json', function (j) {
    json = j['developments'];
    console.log('length: ' + json.length);
    const infoWindow = new google.maps.InfoWindow();

    // create an array of all your markers
    const markers = [];

    // Path for cluster icons to be appended (1.png, 2.png, etc.)
    const imagePath =
      'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m';

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
      markers.push(marker);

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

    // Enable marker clustering for this map and these markers
    // const cluster = new markerClusterer.MarkerClusterer(map, markers, {
    //   imagePath: imagePath,
    // });

    const cluster = new MarkerClusterer(map, markers, {
      imagePath: imagePath,
    });

    // console.log(json); // this will show the info it in firebug console
  });
}

// setTimeout(initMap, 10000);
