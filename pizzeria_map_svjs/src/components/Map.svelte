<script>
    let container;
    let map;
    let zoom = 8;
    let center = { lat: 34.3668, lng: -89.5186 };
    const mapOptions = { zoom, center };

    const mapMarkerCenter = center;
    const title = "This is a marker";

    import { onMount } from 'svelte';

    onMount(async () => {
        map = new google.maps.Map(container, mapOptions);
        new google.maps.Marker({
            position: mapMarkerCenter,
            map,
            title
        });
    });
</script>

<div class="gmap" bind:this={container}></div>

<style>
    .gmap {
        height: 100%;
    }
</style>