<script>
    import { currentZip, searchResultsList, hasValidZip, isLoading } from "../stores";
    import PizzeriaListing from "./PizzeriaListing.svelte";
    import Pagination from "./Pagination.svelte";
</script>

<div class="search-results-container">
    {#if $isLoading}
        <div class="no-results">
            <p>Loading...</p>
        </div>
    {:else}
        {#if $hasValidZip}
            <div class="search-results-listings">
                {#if $searchResultsList.length > 0}
                    {#each $searchResultsList as listing}
                        <PizzeriaListing restaurantData="{listing}" />
                    {/each}
                {:else}
                    <div class="no-results">
                        <p>No results found!</p>
                    </div>
                {/if}
    <!--            <Pagination />-->
            </div>
        {:else}
            <div class="no-results">
                {#if $currentZip.length > 0}
                    <p>Zip code {$currentZip} was not found.</p>
                {:else}
                    <p>Enter your ZIP code to find vegan pizza near you!</p>
                {/if}
            </div>
        {/if}
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
        display: grid;
        place-items: center;
    }

    .no-results p {
        padding: 2rem 0;
        font-family: "Jost", "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        font-size: 1.75rem;
        font-weight: 800;
        color: #D6D3D1;
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

        .no-results p {
            font-size: 3rem;
        }
    }
</style>