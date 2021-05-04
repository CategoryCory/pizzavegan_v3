<script></script>

<div class="sb-container">
    <form class="sb-form">
        <input
            id="zipCode"
            type="text"
            class="sb-form__input"
            placeholder="Search by ZIP"
            aria-label="Search by ZIP"
        >
        <button type="submit" class="sb-form__button">
            <img src="/static/images/magnifying-glass.svg" alt="Search">
        </button>
    </form>
</div>

<style>
    .sb-container {
        padding: 1rem 0.75rem;
    }

    .sb-form {
        width: 95%;
        margin: 0 auto;
        padding: 0.5em 0.75em;
        display: flex;
        justify-content: space-between;
        border: 1px solid rgb(168, 162, 158);
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

    @media screen and (min-width: 640px) {
        .sb-form {
            width: 75%;
        }
    }

    @media screen and (min-width: 1024px) {
        .sb-container {
            padding: 0.75rem 0;
            height: 13%;
        }
    }
</style>