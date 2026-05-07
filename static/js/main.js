const form = document.querySelector("form");

window.onload = () => {
    const savedData = JSON.parse(localStorage.getItem("auditForm"));

    if (savedData) {
        Object.keys(savedData).forEach(key => {
            const field = document.querySelector(`[name="${key}"]`);
            if (field) {
                field.value = savedData[key];
            }
        });
    }
};

form.addEventListener("input", () => {
    const formData = new FormData(form);
    const data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });

    localStorage.setItem("auditForm", JSON.stringify(data));
});