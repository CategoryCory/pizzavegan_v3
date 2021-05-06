<script>
    let pizzeriaName = "Bob's Pizza";
    let streetAddress = "123 Main Street";
    let city = "Oxford";
    let state = "MS";
    let zip = "38655";
    let phone = "662-555-1234";

    export let logo;
    
</script>

<div class="listing-container">
    <div class="listing-image-container">
        <img src={logo} alt="Pizza Logo" class="listing-image">
    </div>
    <div class="listing-info-container">
        <h2>{pizzeriaName}</h2>
        <p>{streetAddress}</p>
        <p>{city}, {state} {zip}</p>
        <p>{phone}</p>
        <p>Dine In | Pickup | Delivery</p>
    </div>
</div>

<style>
    .listing-container {
        display: flex;
        justify-content: flex-start;
        align-items: center;
        /*border: 1px solid rgb(230, 226, 222);*/
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
        font-size: 1.2rem;
        line-height: 1.5;
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