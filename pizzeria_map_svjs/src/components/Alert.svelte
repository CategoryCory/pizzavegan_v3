<script>
    import { scale } from "svelte/transition";
    export let message;
</script>

<div class="sb-error" transition:scale="{{duration: 300}}">
    <p>{message}</p>
</div>

<style>
    .sb-error {
        width: 100%;
        margin-top: 0.75em;
        padding: 0.75em 1em;
        border: 1px solid #D6D3D1;
        border-left: 4px solid #EF4444;
        border-radius: 0.25rem;
    }

    .sb-error p {
        font-family: "Jost", "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
    }
</style>