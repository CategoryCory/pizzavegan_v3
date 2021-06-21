<script>
    import { scale } from "svelte/transition";
    import Fa from "svelte-fa";
    import { faFacebook, faTwitter, faInstagram, faTiktok, faYoutube } from "@fortawesome/free-brands-svg-icons";
    export let restaurantData;
</script>

<div class="listing-container" transition:scale="{{duration: 300}}">
    <div class="listing-image-container">
        <img src={restaurantData.profile.pizzeria_logo} alt="Pizza Logo" class="listing-image">
    </div>
    <div class="listing-info-container">
        <h2>{restaurantData.profile.company_name}</h2>
        <p>{restaurantData.street_address1}</p>
        <p>{restaurantData.city}, {restaurantData.state} {restaurantData.zip_code}</p>
        <!-- p>{phone}</p -->
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
        {#if restaurantData.profile.online_ordering }
            <a href={restaurantData.profile.online_ordering} class="listing-online-ordering">Order online!</a>
        {/if}
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
        padding: 0.75rem 1rem 1.25rem;
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

    .listing-social-media {
        margin: 0.75em 0 1.5em;
        display: flex;
        justify-content: start;
        align-items: center;
        gap: 0.5em;
    }

    .listing-online-ordering {
        padding: 0.2em 0.6em;
        border: 2px solid rgb(105, 98, 92);
        border-radius: 0.4em;
        color: rgb(105, 98, 92);
        transition: all 150ms ease-in-out;
    }

    .listing-online-ordering:hover {
        background-color: rgb(105, 98, 92);
        color: rgb(255, 255, 255);
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