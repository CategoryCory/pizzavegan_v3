import { writable } from "svelte/store";

export const currentZip = writable("");
export const currentLatLng = writable([]);
export const currentPizzeria = writable({});
export const hasValidZip = writable(false);
export const isLoading = writable(false);
export const searchResultsList = writable([]);