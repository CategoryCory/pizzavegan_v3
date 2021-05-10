<script></script>

<div class="pagination-container">
    <a href="/" class="previous">&larr;</a>
    <a href="/" class="active">1</a>
    <a href="/">2</a>
    <a href="/">3</a>
    <a href="/">4</a>
    <a href="/">5</a>
    <a href="/" class="next">&rarr;</a>
</div>

<style>
    .pagination-container {
        padding: 1.5rem 0;
        display: flex;
        justify-content: flex-end;
        gap: 0.5rem;
    }

    .pagination-container a {
        display: inline-block;
        width: 2.5rem;
        height: 2.5rem;
        line-height: 2.5rem;
        border-radius: 9999px;
        text-align: center;
    }

    .pagination-container a:hover {
        background-color: #E7E5E4;
    }

    .pagination-container a.previous,
    .pagination-container a.next {
        background-color: #E7E5E4;
    }

    .pagination-container a.previous:hover,
    .pagination-container a.next:hover {
        background-color: #D6D3D1;
    }

    .pagination-container a.active {
        background-color: #B45A7E;
        color: white;
    }

    @media screen and (min-width: 640px) {
        .pagination-container {
            padding: 2.25rem 0;
        }

        .pagination-container a {
            width: 3rem;
            height: 3rem;
            line-height: 3rem;
        }
    }
</style>