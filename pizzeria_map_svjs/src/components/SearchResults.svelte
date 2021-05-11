<script>
    import { currentZip, searchResultsList } from "../stores";
    import PizzeriaListing from "./PizzeriaListing.svelte";
    import Pagination from "./Pagination.svelte";
</script>

<div class="search-results-container">
    {#if $searchResultsList.length > 0}
        <div class="search-results-listings">
            {#each $searchResultsList as listing}
                <PizzeriaListing logo="{listing.logo}" />
            {/each}
        </div>
<!--        <Pagination />-->
    {:else}
        <div class="no-results">
            {#if $currentZip.length === 0}
                <p>Enter your ZIP code to search for vegan pizza near you!</p>
            {:else}
                <p>No results found.</p>
            {/if}
        </div>
    {/if}
</div>

<style>
    .search-results-container {
        padding: 0.5rem 1rem;
    }

    .search-results-listings {
        display: grid;
        grid-auto-rows: 1fr;
        grid-template-columns: repeat(auto-fit, minmax(325px, 1fr));
        gap: 0.75rem;
    }

    .no-results {
        background-color: bisque;
        display: grid;
        place-items: center;
    }

    @media screen and (min-width: 1024px) {
        .search-results-container {
            padding: 1.5rem;
            max-height: 87%;
            overflow-y: auto;
        }

        .search-results-listings {
            gap: 1.5rem;
        }
    }
</style>