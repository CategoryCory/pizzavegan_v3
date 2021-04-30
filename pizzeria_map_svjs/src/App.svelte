<script>
	import Map from './components/Map.svelte';
	import SearchBar from './components/SearchBar.svelte';
	export let ready;
</script>

<svelte:head>
	<script defer async
		src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBIIbGAPSDhXreX1zK_WoOXZSGR1ktxw6I&callback=initMap">
	</script>
	<script defer
		src="https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/markerclusterer.js">
	</script>
</svelte:head>

<div class="w-full h-screen lg:grid lg:grid-cols-2">
	<div class="h-1/3 lg:h-full">
		{#if ready}
			<Map />
		{:else}
			<div class="h-full grid place-content-center">
				<h2 class="text-2xl text-gray-400">Loading map...</h2>
			</div>
		{/if}
	</div>
	<div class="">
		<SearchBar />
		<div>This is the results area.</div>
	</div>
</div>
