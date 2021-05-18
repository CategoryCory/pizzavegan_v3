<script>
    import {currentLatLng, currentZip, hasValidZip, isLoading, searchResultsList} from "../stores";
    import Alert from "./Alert.svelte";
    import { beforeUpdate, afterUpdate } from "svelte";

    let zipCode;
    let zipFormatError = false;

    beforeUpdate(() => {
        // $searchResultsList.length = 0;
        // $isLoading = true;
    });

    // afterUpdate(() => {
    //     $isLoading = false;
    // })

    async function buttonClicked(e) {
        $isLoading = true;
        // $hasValidZip = false;
        $searchResultsList.length = 0;
        const zipRegex = /^[0-9]{5}(?:-[0-9]{4})?$/;
        if (zipRegex.test(zipCode)) {
            $currentZip = zipCode;
            zipFormatError = false;

            try {
                const response = await fetch(`/api/v1/signups/?zip=${$currentZip}`);
                const data = await response.json();

                if (data["origin_status"] === "NOT_FOUND")  {
                    $hasValidZip = false;
                    // $isLoading = false;
                    // return;
                } else {
                    $hasValidZip = true;
                    $searchResultsList = [...data.locations];
                    $currentLatLng = [...data.origin_latlng];
                }
            } catch (error) {
                console.log(error.message);
            } finally {
                // $isLoading = false;
            }
        } else {
            $currentZip = "";
            $hasValidZip = false;
            zipFormatError = true;
        }

        $isLoading = false;
    }
</script>

<div class="sb-container">
    <form class="sb-form">
        <input
            id="zipCode"
            type="text"
            class="sb-form__input"
            bind:value={zipCode}
            placeholder="Search by ZIP"
            aria-label="Search by ZIP"
        >
        {#if $isLoading}
            <div class="sb-form__wait-icon">
                <img src="/static/images/wait-icon.svg" alt="Wait...">
            </div>
        {:else}
            <button type="submit" class="sb-form__button" on:click|preventDefault={buttonClicked}>
                <img src="/static/images/magnifying-glass.svg" alt="Search">
            </button>
        {/if}
    </form>
    {#if zipFormatError}
        <Alert message="Please enter a valid 5 or 9 digit ZIP code." />
    {/if}
</div>

<style>
    .sb-container {
        width: 95%;
        margin: 0 auto;
        padding: 1rem 0.75rem;
        font-family: "Jost", "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }

    .sb-container * {
        font-family: inherit;
    }

    .sb-form {
        padding: 0.2rem 0.5rem;
        display: flex;
        justify-content: space-between;
        border: 1px solid rgb(168, 162, 158);
        border-radius: 0.5rem;
    }

    .sb-form__input {
        width: 100%;
        border: none;
        font-size: 1.125rem;
    }

    .sb-form__input:focus {
        box-shadow: none;
    }

    .sb-form__button,
    .sb-form__wait-icon {
        padding: 0.5em 0.75rem;
    }

    .sb-form__button img,
    .sb-form__wait-icon img {
        height: 1.75rem;
        width: 1.75rem;
    }

    .sb-form__wait-icon img {
        animation: wait-icon-spin 1s linear infinite;
    }

    @keyframes wait-icon-spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(359deg); }
    }

    @media screen and (min-width: 640px) {
        .sb-container {
            width: 75%;
        }

        .sb-form {
            padding: 0.5em 0.75em;
        }
    }

    @media screen and (min-width: 1024px) {
        .sb-container {
            padding: 0.75rem 0;
            min-height: 13%;
        }
    }
</style>