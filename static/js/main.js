document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    if (!form) return;

    // Load saved values
    document.querySelectorAll("input, select").forEach((field) => {

        const savedValue = localStorage.getItem(field.name);

        if (savedValue !== null) {
            field.value = savedValue;
        }

        // Save on change
        field.addEventListener("input", () => {
            localStorage.setItem(field.name, field.value);
        });

    });

});