<script>
    import {currentLatLng, searchResultsList, hasValidZip} from "../stores";

    let container;
    let map;
    let markers = [];
    let defaultZoom = 4;
    let defaultCenter = { lat: 39.8283, lng: -98.5795 };
    const mapOptions = { zoom: defaultZoom, center: defaultCenter };

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
                for (let i = 0; i < $searchResultsList.length; i++) {
                    const position = {
                        lat: Number($searchResultsList[i].latitude),
                        lng: Number($searchResultsList[i].longitude)
                    }
                    const pizzeriaMarker = new google.maps.Marker({
                        position,
                        map,
                        title: $searchResultsList[i].restaurant_name
                    });
                    markers.push(pizzeriaMarker);
                }
            }

            // set map to focus on current location
            map.setCenter({ lat: $currentLatLng[0], lng: $currentLatLng[1] });
            map.setZoom(12);
        }
    }
</script>

<div class="gmap" bind:this={container}></div>

<style>
    .gmap {
        height: 100%;
    }
</style>