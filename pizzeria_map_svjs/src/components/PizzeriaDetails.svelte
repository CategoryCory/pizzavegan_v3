<script>
    import { currentPizzeria } from "../stores";
    import Fa from "svelte-fa";
    import { faTimes, faExternalLinkAlt, faPizzaSlice } from "@fortawesome/free-solid-svg-icons";
    import { faFacebook, faTwitter, faInstagram, faTiktok, faYoutube } from "@fortawesome/free-brands-svg-icons";

    const diningOptions = [];

    $: {
        diningOptions.length = 0;
        if ($currentPizzeria.dine_in) diningOptions.push("Dine In");
        if ($currentPizzeria.carry_out) diningOptions.push("Carry Out");
        if ($currentPizzeria.delivery) diningOptions.push("Delivery");
    }

    const closeDetails = () => {
        for (let prop in $currentPizzeria) {
            delete $currentPizzeria[prop];
        }
        $currentPizzeria.isSet = false;
    };
</script>

<main class="{$currentPizzeria.isSet ? 'show-pizzeria-details' : ''}">
    <div class="close-button" on:click="{closeDetails}"><Fa icon={faTimes} fw color="#69625C" size="2x" /></div>
    {#if $currentPizzeria.isSet}
        <div class="title-row">
            {#if $currentPizzeria.profile.pizzeria_logo}
                <img src={$currentPizzeria.profile.pizzeria_logo} alt="Pizza Logo" class="pizzeria-logo">
            {:else}
                <div class="no-logo">
                    <p>No Logo Provided</p>
                </div>
            {/if}
            <div>
                <h2>{$currentPizzeria.profile.company_name}</h2>
                <p>
                    {$currentPizzeria.full_address}
                    {#if $currentPizzeria.phone}
                        &nbsp;|&nbsp;{$currentPizzeria.phone}
                    {/if}
                </p>
                {#if diningOptions.length > 0}
                    <p>{diningOptions.join(" | ")}</p>
                {/if}
                {#if $currentPizzeria.location_website}
                    <a href={$currentPizzeria.location_website} class="location-link">
                        <Fa icon={faExternalLinkAlt} fw color="#69625C" size="sm" style="display: inline-block; margin-right: 0.15rem;" />Visit Store Website
                    </a>
                {/if}
                <div class="online-links">
                    {#if $currentPizzeria.profile.online_ordering}
                        <a href={$currentPizzeria.profile.online_ordering} class="online-ordering" target="_blank">Order online</a>
                    {/if}
                    <div class="social-media">
                        {#if $currentPizzeria.profile.pizzeria_website}
                        <a href={$currentPizzeria.profile.pizzeria_website} target="_blank">
                            <Fa icon={faPizzaSlice} fw color="#69625C" size="lg" />
                        </a>
                        {/if}
                        {#if $currentPizzeria.profile.facebook}
                            <a href={$currentPizzeria.profile.facebook} target="_blank">
                                <Fa icon={faFacebook} fw color="#69625C" size="lg" />
                            </a>
                        {/if}
                        {#if $currentPizzeria.profile.twitter}
                            <a href={$currentPizzeria.profile.twitter} target="_blank">
                                <Fa icon={faTwitter} fw color="#69625C" size="lg" />
                            </a>
                        {/if}
                        {#if $currentPizzeria.profile.instagram}
                            <a href={$currentPizzeria.profile.instagram} target="_blank">
                                <Fa icon={faInstagram} fw color="#69625C" size="lg" />
                            </a>
                        {/if}
                        {#if $currentPizzeria.profile.tiktok}
                            <a href={$currentPizzeria.profile.tiktok} target="_blank">
                                <Fa icon={faTiktok} fw color="#69625C" size="lg" />
                            </a>
                        {/if}
                        {#if $currentPizzeria.profile.youtube}
                            <a href={$currentPizzeria.profile.youtube} target="_blank">
                                <Fa icon={faYoutube} fw color="#69625C" size="lg" />
                            </a>
                        {/if}
                    </div>
                </div>
            </div>
        </div>
        <div class="details-body">
            {#if $currentPizzeria.profile.description}
                <h3>About {$currentPizzeria.profile.company_name}</h3>
                <p>{$currentPizzeria.profile.description}</p>
            {/if}
            {#if $currentPizzeria.profile.promotions.length > 0}
                <div class="pizzeria-promotions">
                    <h3>Current Promotions</h3>
                    {#each $currentPizzeria.profile.promotions as promotion}
                        <div class="promotion-card">
                            <div class="promotion-title">
                                <h4>{promotion.title}</h4>
                                <span class="promotion-date-range">{promotion.date_range}</span>
                            </div>
                            <div>
                                <p>{promotion.description}</p>
                            </div>
                        </div>
                    {/each}
                </div>
            {/if}
            {#if $currentPizzeria.profile.menuitems.length > 0}
                <h3>Menu Items</h3>
                <div class="menu-items">
                    {#each $currentPizzeria.profile.menuitems as menuitem}
                        <div class="menu-item-card">
                            {#if menuitem.photo}
                                <img src={menuitem.photo} class="menu-item-photo" alt="Photo for {menuitem.title}">
                            {:else}
                                <div class="no-menu-photo">
                                    <p>No Photo Provided</p>
                                </div>
                            {/if}
                            <div class="menu-item-body">
                                <h4>{menuitem.title}</h4>
                                <p class="menu-item-price">${menuitem.price}</p>
                                <p class="menu-item-description">{menuitem.description}</p>
                            </div>
                        </div>
                    {/each}
                </div>
            {/if}
        </div>
    {/if}
</main>

<style>
    main {
        position: absolute;
        padding: 1rem;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 15;
        overflow-y: visible;
        transform: translateX(100%);
        transition: transform 250ms ease-in-out;
        background-color: rgba(255, 255, 255, 1);
        font-family: "Jost", "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }

    main * {
        font-family: inherit;
    }
    
    main h2 {
        font-size: 1.5rem;
        color: rgb(50, 45, 42);
    }

    main h3 {
        font-size: 1.25rem;
        color: rgb(50, 45, 42);
    }

    main h4 {
        font-size: 1.125rem;
        color: rgb(50, 45, 42);
    }

    main p {
        color: rgb(105, 98, 92);
    }

    .show-pizzeria-details {
        transform: translateX(0%);
    }

    .close-button {
        position: absolute;
        display: grid;
        place-items: center;
        top: 1.5rem;
        right: 1.5rem;
        width: 3.5rem;
        height: 3.5rem;
        cursor: pointer;
        background-color: rgba(255, 255, 255, 1);
        border-radius: 9999px;
        box-shadow: 0 2px 6px 1px rgba(0, 0, 0, 0.15);
    }

    .title-row {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .title-row p {
        font-size: 0.75rem;
    }

    .pizzeria-logo,
    .no-logo {
        margin-right: 2rem;
    }

    .pizzeria-logo {
        max-width: 10rem;
        max-height: 10rem;
    }

    .no-logo {
        width: 8rem;
        height: 8rem;
        display: grid;
        place-items: center;
        background-color: #E7E5E4;
    }

    .location-link {
        position: relative;
        display: inline-block;
        margin-top: 0.75rem;
        color: rgb(105, 98, 92);
    }

    .location-link::after {
        position: absolute;
        content: "";
        width: 100%;
        left: 0;
        bottom: 0;
        height: 1px;
        background-color: rgba(80, 73, 67, 0);
        transition: background-color 150ms ease-in-out;
    }

    .location-link:hover {
        color: rgb(80, 73, 67);
    }

    .location-link:hover::after {
        background-color: rgba(80, 73, 67, 1);
    }

    .online-links {
        margin-top: 1rem;
        display: flex;
        align-items: center;
    }

    .online-ordering {
        display: inline-block;
        margin-right: 1rem;
        padding: 0.1em 0.4em;
        border: 2px solid rgb(105, 98, 92);
        border-radius: 0.25em;
        color: rgb(105, 98, 92);
        transition: all 150ms ease-in-out;
    }

    .online-ordering:hover {
        background-color: rgb(105, 98, 92);
        color: rgb(255, 255, 255);
    }

    .social-media {
        display: flex;
        align-items: center;
        gap: 0.75em;
    }

    .details-body {
        padding: 1rem;
    }

    .pizzeria-promotions {
        margin: 0.5rem 0;
    }

    .promotion-card {
        margin-bottom: 0.75rem;
        padding: 0.5rem 1.5rem;
        border: 1px solid rgb(210, 202, 194);
        border-radius: 0.5rem;
    }

    .promotion-title {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }

    .promotion-date-range {
        display: inline-block;
        margin-bottom: 0.75rem;
        padding: 0 0.5rem;
        background-color: rgb(50, 45, 42);
        font-size: 0.875rem;
        color: white;
        border-radius: 0.25rem;
    }

    .menu-items {
        display: grid;
        grid-template-rows: auto;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
    }

    .menu-item-card {
        border-radius: 0.5rem;
        box-shadow: 0 3px 6px 2px rgba(50, 45, 42, 0.2);
    }

    .menu-item-photo {
        width: 100%;
        height: 12rem;
        object-fit: cover;
        object-position: center;
        border-top-left-radius: 0.5rem;
        border-top-right-radius: 0.5rem;
    }

    .no-menu-photo {
        width: 100%;
        height: 5rem;
        display: grid;
        place-items: center;
    }

    .menu-item-body {
        padding: 0.5rem 1rem;
    }

    .menu-item-body p {
        font-size: 0.875rem;
    }

    @media screen and (min-width: 1024px) {
        main {
            height: 100%;
        }

        main h2 {
            font-size: 2rem;
        }

        main h3 {
            font-size: 1.5rem;
        }

        main h4 {
            font-size: 1.125rem;
        }

        .title-row {
            flex-direction: row;
            align-items: center;
        }

        .title-row p {
            font-size: 1rem;
        }

        .promotion-title {
            flex-direction: row;
            align-items: center;
        }

        .promotion-date-range {
            margin-left: 0.75rem;
            margin-bottom: 0;
        }
    }
</style>