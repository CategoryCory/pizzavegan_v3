<script>
    import PizzeriaListing from "./PizzeriaListing.svelte";
    import Pagination from "./Pagination.svelte";
</script>

<div class="search-results-container">
    <div class="search-results-listings">
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
<!--    <PizzeriaListing logo="/static/images/slices.png" />-->
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

    <Pagination />
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