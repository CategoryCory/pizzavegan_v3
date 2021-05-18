<script>
    import { currentZip, searchResultsList, hasValidZip, isLoading } from "../stores";
    import PizzeriaListing from "./PizzeriaListing.svelte";

    let resultsPluralized;
    $: {
        if ($searchResultsList.length === 1)
            resultsPluralized = "result";
        else
            resultsPluralized = "results";
    }
</script>

<div class="search-results-container">
    {#if !$isLoading}
        {#if $hasValidZip}
            <p class="search-results-message">{$searchResultsList.length} {resultsPluralized} found</p>
            <div class="search-results-listings">
                {#if $searchResultsList.length > 0}
                    {#each $searchResultsList as listing}
                        <PizzeriaListing restaurantData="{listing}" />
                    {/each}
                {/if}
            </div>
        {:else}
            {#if $currentZip.length > 0}
                <p class="search-results-message">Zip code {$currentZip} not found.</p>
            {/if}
        {/if}
    {/if}
</div>

<style>
    .search-results-container {
        padding: 0.5rem 1rem;
    }

    .search-results-message {
        padding: 0.5rem 1.25rem;
        margin-bottom: 1.5rem;
        background-color: #D6D3D1;
        border-radius: 0.5rem;
        font-family: "Jost", "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
        color: #57534E;
        text-align: right;
    }

    .search-results-listings {
        display: grid;
        grid-auto-rows: 1fr;
        grid-template-columns: repeat(auto-fit, minmax(325px, 1fr));
        gap: 0.75rem;
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