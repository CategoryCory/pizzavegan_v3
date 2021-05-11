<script>
    let container;
    let map;
    let defaultZoom = 4;
    let defaultCenter = { lat: 39.8283, lng: -98.5795 };
    const mapOptions = { zoom: defaultZoom, center: defaultCenter };

    // const mapMarkerCenter = center;
    // const title = "This is a marker";

    import { onMount } from 'svelte';

    onMount(async () => {
        map = new google.maps.Map(container, mapOptions);
        //new google.maps.Marker({
        //    position: mapMarkerCenter,
        //    map,
        //    title
        //});
    });
</script>

<div class="gmap" bind:this={container}></div>

<style>
    .gmap {
        height: 100%;
    }
</style>