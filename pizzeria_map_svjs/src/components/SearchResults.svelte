<script>
    import PizzeriaListing from "./PizzeriaListing.svelte";
</script>

<div class="search-results-container">
    <PizzeriaListing message="First one"/>
    <PizzeriaListing message="Second one"/>
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
        padding: 0;
    }

    @media screen and (min-width: 1024px) {
        .search-results-container {
            max-height: 87%;
            overflow-y: auto;
        }
    }
</style>