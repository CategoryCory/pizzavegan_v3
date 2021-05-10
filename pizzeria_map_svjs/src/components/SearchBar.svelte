<script>
    import { currentZip } from "../stores";

    let zipCode;
    let showError = false;

    function buttonClicked(e) {
        const zipRegex = /^[0-9]{5}(?:-[0-9]{4})?$/;
        if (zipRegex.test(zipCode)) {
            $currentZip = zipCode;
            showError = false;
        } else {
            $currentZip = "";
            showError = true;
        }
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
        <button type="submit" class="sb-form__button" on:click|preventDefault={buttonClicked}>
            <img src="/static/images/magnifying-glass.svg" alt="Search">
        </button>
    </form>
    {#if showError}
        <div class="sb-error">
            <p>Please enter a valid 5 or 9 digit ZIP code.</p>
        </div>
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
        /*width: 95%;*/
        /*margin: 0 auto;*/
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

    .sb-form__button {
        padding: 0.5em 0.75rem;
    }

    .sb-form__button img {
        height: 1.75rem;
        width: 1.75rem;
    }

    .sb-error {
        margin-top: 0.75em;
        padding: 0.75em 1em;
        border: 1px solid #D6D3D1;
        border-left: 4px solid #EF4444;
        border-radius: 0.25rem;
    }

    .sb-error p {
        color: #EF4444;
    }

    @media screen and (min-width: 640px) {
        .sb-container {
            width: 75%;
        }

        .sb-form {
            /*width: 75%;*/
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