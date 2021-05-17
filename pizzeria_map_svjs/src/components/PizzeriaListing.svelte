<script>
    import { scale } from "svelte/transition";

    let logo = "";

    export let restaurantData;
    
</script>

<div class="listing-container" transition:scale="{{duration: 300}}">
    <div class="listing-image-container">
        <img src={logo} alt="Pizza Logo" class="listing-image">
    </div>
    <div class="listing-info-container">
        <h2>{restaurantData.restaurant_name}</h2>
        <p>{restaurantData.street_address1}</p>
        <p>{restaurantData.city}, {restaurantData.state} {restaurantData.zip_code}</p>
        <!-- p>{phone}</p -->
        <p>Dine In | Pickup | Delivery</p>
    </div>
</div>

<style>
    .listing-container {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        border-radius: 0.5rem;
        box-shadow: 0 0.125rem 0.5rem 0 rgba(0, 0, 0, 0.15);
        font-family: "Jost", "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }

    .listing-container * {
        font-family: inherit;
    }

    .listing-image-container {
        height: 100%;
        width: 7rem;
        padding: 0.5rem;
        display: grid;
        place-items: center;
    }

    .listing-image {
        max-height: 6rem;
        max-width: 6rem;
        object-fit: scale-down;
        object-position: center;
    }

    .listing-info-container {
        height: 100%;
        padding: 0.75rem 1rem;
    }

    .listing-info-container h2 {
        margin-bottom: 0.75rem;
        font-size: 1.2rem;
        line-height: 1.2;
    }

    .listing-info-container p {
        font-size: 0.875rem;
        line-height: 1.375;
        color: rgb(105, 98, 92);
    }

    @media screen and (min-width: 640px) {

    }

    @media screen and (min-width: 1024px) {
        .listing-image-container {
            width: 10rem;
            padding: 0.75rem;
        }

        .listing-image {
            max-height: 10rem;
            max-width: 10rem;
        }

        .listing-info-container h2 {
            font-size: 1.5rem;
        }

        .listing-info-container p {
            font-size: 1rem;
        }
    }
</style>