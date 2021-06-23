<script>
    import { scale } from "svelte/transition";
    import { currentPizzeria } from "../stores";
    import Fa from "svelte-fa";
    import { faFacebook, faTwitter, faInstagram, faTiktok, faYoutube } from "@fortawesome/free-brands-svg-icons";
    export let restaurantData;

    const diningOptions = [];
    if (restaurantData.dine_in) diningOptions.push("Dine In");
    if (restaurantData.carry_out) diningOptions.push("Carry Out");
    if (restaurantData.delivery) diningOptions.push("Delivery");

    const handleClick = () => {
        $currentPizzeria["latitude"] = restaurantData.latitude;
        $currentPizzeria["longitude"] = restaurantData.longitude;
        // alert($currentPizzeria.latitude);
    }
</script>

<div class="listing-container" transition:scale="{{duration: 300}}">
    <div class="listing-image-container" on:click={handleClick}>
        {#if restaurantData.profile.pizzeria_logo}
            <img src={restaurantData.profile.pizzeria_logo} alt="Pizza Logo" class="listing-image">
        {:else}
            <div class="no-logo">
                <p>No Logo Provided</p>
            </div>
        {/if}
    </div>
    <div class="listing-info-container">
        <h2 class="listing-pizzeria-name" on:click={handleClick}>{restaurantData.profile.company_name}</h2>
        <p>{restaurantData.street_address1}</p>
        <p>{restaurantData.city}, {restaurantData.state} {restaurantData.zip_code}</p>
        {#if restaurantData.phone}
            <p>{restaurantData.phone}</p>
        {/if}
        {#if diningOptions.length > 0}
            <p>{diningOptions.join(" | ")}</p>
        {/if}
        {#if restaurantData.profile.online_ordering }
            <a href={restaurantData.profile.online_ordering} class="listing-online-ordering">Order online!</a>
        {/if}
        <div class="listing-social-media">
            {#if restaurantData.profile.facebook}
                <a href={restaurantData.profile.facebook}>
                    <Fa icon={faFacebook} fw color="#69625C" size="lg" />
                </a>
            {/if}
            {#if restaurantData.profile.twitter}
                <a href={restaurantData.profile.twitter}>
                    <Fa icon={faTwitter} fw color="#69625C" size="lg" />
                </a>
            {/if}
            {#if restaurantData.profile.instagram}
                <a href={restaurantData.profile.instagram}>
                    <Fa icon={faInstagram} fw color="#69625C" size="lg" />
                </a>
            {/if}
            {#if restaurantData.profile.tiktok}
                <a href={restaurantData.profile.tiktok}>
                    <Fa icon={faTiktok} fw color="#69625C" size="lg" />
                </a>
            {/if}
            {#if restaurantData.profile.youtube}
                <a href={restaurantData.profile.youtube}>
                    <Fa icon={faYoutube} fw color="#69625C" size="lg" />
                </a>
            {/if}
        </div>
    </div>
</div>

<style>
    .listing-container {
        padding: 0.5rem 0 1rem;
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
        padding: 0;
    }

    .listing-info-container h2 {
        margin-bottom: 0;
        font-size: 1.2rem;
        line-height: 1.2;
    }

    .listing-info-container p {
        font-size: 0.875rem;
        line-height: 1.375;
        color: rgb(105, 98, 92);
    }

    .listing-social-media {
        margin-top: 0.75em;
        display: flex;
        justify-content: start;
        align-items: center;
        gap: 0.5em;
    }

    .listing-online-ordering {
        display: inline-block;
        margin-top: 0.75em;
        padding: 0.1em 0.4em;
        border: 2px solid rgb(105, 98, 92);
        border-radius: 0.25em;
        color: rgb(105, 98, 92);
        transition: all 150ms ease-in-out;
    }

    .listing-online-ordering:hover {
        background-color: rgb(105, 98, 92);
        color: rgb(255, 255, 255);
    }

    .no-logo {
        height: 100%;
        width: 100%;
        display: grid;
        place-items: center;
        background-color: #E7E5E4;
    }

    .no-logo p {
        color: #57534E;
        font-weight: bold;
        text-align: center;
    }

    .listing-image-container,
    .listing-pizzeria-name {
        cursor: pointer;
    }

    @media screen and (min-width: 1024px) {
        .listing-image-container {
            width: 10rem;
            padding: 0.75rem;
        }

        .listing-image {
            max-height: 8.5rem;
            max-width: 8.5rem;
        }

        .listing-info-container h2 {
            font-size: 1.5rem;
        }

        .listing-info-container p {
            font-size: 1rem;
        }
    }
</style>