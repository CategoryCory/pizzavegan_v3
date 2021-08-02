<script>
    import { scale } from "svelte/transition";
    import { currentPizzeria } from "../stores";
    import Fa from "svelte-fa";
    import { faFacebook, faTwitter, faInstagram, faTiktok, faYoutube } from "@fortawesome/free-brands-svg-icons";
    import { faExternalLinkAlt, faPizzaSlice } from "@fortawesome/free-solid-svg-icons";
    export let restaurantData;

    const diningOptions = [];
    if (restaurantData.dine_in) diningOptions.push("Dine In");
    if (restaurantData.carry_out) diningOptions.push("Carry Out");
    if (restaurantData.delivery) diningOptions.push("Delivery");

    const handleClick = () => {
        $currentPizzeria = Object.assign({}, restaurantData);
        $currentPizzeria.isSet = true;
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
        <div class="listing-link-container">
            {#if restaurantData.profile.online_ordering }
                <a href={restaurantData.profile.online_ordering} class="listing-link" target="_blank">
                    <Fa icon={faExternalLinkAlt} fw color="#69625C" size="sm" style="display: inline-block; margin-right: 0.15rem;" />Order online
                </a>
            {/if}
            {#if restaurantData.location_website}
                <a href={restaurantData.location_website} class="listing-link" target="_blank">
                    <Fa icon={faExternalLinkAlt} fw color="#69625C" size="sm" style="display: inline-block; margin-right: 0.15rem;" />Visit Store Website
                </a>
            {/if}
        </div>
        <div class="listing-social-media">
            {#if restaurantData.location_website}
                <a href={restaurantData.location_website} target="_blank">
                    <Fa icon={faPizzaSlice} fw color="#69625C" size="lg" />
                </a>
            {/if}
            {#if restaurantData.profile.facebook}
                <a href={restaurantData.profile.facebook} target="_blank">
                    <Fa icon={faFacebook} fw color="#69625C" size="lg" />
                </a>
            {/if}
            {#if restaurantData.profile.twitter}
                <a href={restaurantData.profile.twitter} target="_blank">
                    <Fa icon={faTwitter} fw color="#69625C" size="lg" />
                </a>
            {/if}
            {#if restaurantData.profile.instagram}
                <a href={restaurantData.profile.instagram} target="_blank">
                    <Fa icon={faInstagram} fw color="#69625C" size="lg" />
                </a>
            {/if}
            {#if restaurantData.profile.tiktok}
                <a href={restaurantData.profile.tiktok} target="_blank">
                    <Fa icon={faTiktok} fw color="#69625C" size="lg" />
                </a>
            {/if}
            {#if restaurantData.profile.youtube}
                <a href={restaurantData.profile.youtube} target="_blank">
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
        width: 95%;
        padding: 0;
    }

    .listing-info-container h2 {
        margin-bottom: 0;
        font-size: 1.2rem;
        line-height: 1.2;
    }

    .listing-info-container p,
    .listing-info-container a {
        font-size: 0.875rem;
    }

    .listing-info-container p {
        /* font-size: 0.875rem; */
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

    .listing-link-container {
        width: 100%;
        display: flex;
        flex-wrap: wrap;
        align-items: center;
        gap: 0.75rem;
    }

    .listing-link {
        position: relative;
        display: block;
        margin-top: 0.25rem;
        color: rgb(105, 98, 92);
        transition: color 150ms ease-in-out;
    }

    .listing-link::after {
        position: absolute;
        content: "";
        width: 100%;
        left: 0;
        bottom: 0;
        height: 1px;
        background-color: rgba(80, 73, 67, 0);
        transition: background-color 150ms ease-in-out;
    }

    .listing-link:hover {
        color: rgb(80, 73, 67);
    }

    .listing-link:hover::after {
        background-color: rgba(80, 72, 67, 1);
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

        /* .listing-info-container p {
            font-size: 1rem;
        } */
    }
</style>