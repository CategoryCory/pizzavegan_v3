<script>
	import Map from './components/Map.svelte';
	import SearchBar from './components/SearchBar.svelte';
	import SearchResults from './components/SearchResults.svelte';
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

<main class="map-container">
	<div class="map">
		{#if ready}
			<Map />
		{:else}
			<div class="map__loading-container">
				<h2 class="map__loading-message">Loading map...</h2>
			</div>
		{/if}
	</div>
	<div class="search-container">
		<SearchBar />
		<SearchResults />
	</div>
</main>

<style>
	.map-container {
		width: 100%;
	}

	.map {
		height: 250px;
	}

	.map__loading-container {
		height: 100%;
		display: grid;
		place-items: center;
	}

	.map__loading-message {
		font-size: 2rem;
		color: rgb(168, 162, 158);
	}

	.search-container {
		height: inherit;
		padding-top: 0.75em;
	}

	@media screen and (min-width: 640px) {
		.map {
			height: 350px;
		}
	}

	@media screen and (min-width: 1024px) {
		.map-container {
			height: 750px;
			display: grid;
			grid-template-columns: repeat(2, minmax(0, 1fr));
		}

		.map {
			height: 100%;
		}

		.search-container {
			max-height: 100%;
		}
	}
</style>
