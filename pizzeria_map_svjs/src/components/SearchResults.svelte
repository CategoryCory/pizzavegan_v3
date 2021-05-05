<script>
    import PizzeriaListing from "./PizzeriaListing.svelte";
</script>

<div class="search-results-container">
    <PizzeriaListing logo="/static/images/pizza-slice.png" />
    <PizzeriaListing logo="/static/images/Pizza-Hut-Logo.png" />
    <PizzeriaListing logo="/static/images/slices.png" />
    <PizzeriaListing logo="/static/images/pizza-slice.png" />
    <PizzeriaListing logo="/static/images/Pizza-Hut-Logo.png" />
    <PizzeriaListing logo="/static/images/slices.png" />
    <PizzeriaListing logo="/static/images/pizza-slice.png" />
    <PizzeriaListing logo="/static/images/Pizza-Hut-Logo.png" />
    <PizzeriaListing logo="/static/images/slices.png" />
    <PizzeriaListing logo="/static/images/pizza-slice.png" />
    <PizzeriaListing logo="/static/images/Pizza-Hut-Logo.png" />
    <PizzeriaListing logo="/static/images/slices.png" />
    <PizzeriaListing logo="/static/images/pizza-slice.png" />
    <PizzeriaListing logo="/static/images/Pizza-Hut-Logo.png" />
    <PizzeriaListing logo="/static/images/slices.png" />
    <PizzeriaListing logo="/static/images/pizza-slice.png" />
    <PizzeriaListing logo="/static/images/Pizza-Hut-Logo.png" />
    <PizzeriaListing logo="/static/images/slices.png" />
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
<!--    <PizzeriaListing />-->
</div>

<style>
    .search-results-container {
        padding: 0.5rem 1rem 1rem;
        display: grid;
        grid-auto-rows: 1fr;
        gap: 0.75rem;
    }

    @media screen and (min-width: 640px) {
        .search-results-container {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }

    @media screen and (min-width: 1024px) {
        .search-results-container {
            padding: 1.5rem;
            max-height: 87%;
            overflow-y: auto;
            gap: 1.5rem;
            grid-template-columns: repeat(1, minmax(0, 1fr));
        }
    }

    @media screen and (min-width: 1536px) {
        .search-results-container {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }
</style>