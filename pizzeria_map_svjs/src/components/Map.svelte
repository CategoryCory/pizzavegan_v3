<script>
    import {currentLatLng, searchResultsList, hasValidZip} from "../stores";

    let container;
    let map;
    let markers = [];
    let defaultZoom = 4;
    let defaultCenter = { lat: 39.8283, lng: -98.5795 };
    const mapStyles = [
      {
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#f5f5f5"
          }
        ]
      },
      {
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#616161"
          }
        ]
      },
      {
        "elementType": "labels.text.stroke",
        "stylers": [
          {
            "color": "#f5f5f5"
          }
        ]
      },
      {
        "featureType": "administrative.land_parcel",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#bdbdbd"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#eeeeee"
          }
        ]
      },
      {
        "featureType": "poi",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#757575"
          }
        ]
      },
      {
        "featureType": "poi.business",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#e5e5e5"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "labels.text",
        "stylers": [
          {
            "visibility": "off"
          }
        ]
      },
      {
        "featureType": "poi.park",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#9e9e9e"
          }
        ]
      },
      {
        "featureType": "road",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#ffffff"
          }
        ]
      },
      {
        "featureType": "road.arterial",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#757575"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#dadada"
          }
        ]
      },
      {
        "featureType": "road.highway",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#616161"
          }
        ]
      },
      {
        "featureType": "road.local",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#9e9e9e"
          }
        ]
      },
      {
        "featureType": "transit.line",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#e5e5e5"
          }
        ]
      },
      {
        "featureType": "transit.station",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#eeeeee"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "geometry",
        "stylers": [
          {
            "color": "#bad9f8"
          }
        ]
      },
      {
        "featureType": "water",
        "elementType": "labels.text.fill",
        "stylers": [
          {
            "color": "#9e9e9e"
          }
        ]
      }
    ]
    const mapOptions = {
        zoom: defaultZoom,
        center: defaultCenter,
        styles: mapStyles
    };

    import { onMount } from 'svelte';

    onMount(async () => {
        map = new google.maps.Map(container, mapOptions);
    });

    $: {
        if ($hasValidZip) {
            // Clear all markers
            for (let i = 0; i < markers.length; i++) {
                markers[i].setMap(null);
            }

            if ($searchResultsList.length > 0) {
                const bounds = new google.maps.LatLngBounds();

                for (let i = 0; i < $searchResultsList.length; i++) {
                    const position = {
                        lat: Number($searchResultsList[i].latitude),
                        lng: Number($searchResultsList[i].longitude)
                    }
                    const pizzeriaMarker = new google.maps.Marker({
                        position,
                        map,
                        title: $searchResultsList[i].restaurant_name,
                        icon: "/static/images/pizzavegan-map-icon.png"
                    });
                    markers.push(pizzeriaMarker);
                    bounds.extend(pizzeriaMarker.getPosition());
                }

                map.setCenter(bounds.getCenter());
                map.fitBounds(bounds);

                if (map.getZoom() > 15) {
                    map.setZoom(15);
                } else {
                    map.setZoom(map.getZoom() - 1);
                }
            } else {
                // set map to focus on current location
                map.setCenter({ lat: $currentLatLng[0], lng: $currentLatLng[1] });
                map.setZoom(13);
            }
        }
    }
</script>

<div class="gmap" bind:this={container}></div>

<style>
    .gmap {
        height: 100%;
    }
</style>