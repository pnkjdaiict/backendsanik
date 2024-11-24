document.addEventListener("DOMContentLoaded", function () {
    // Apply Select2 to the states field
    const statesField = document.getElementById("id_states");
    if (statesField) {
        $(statesField).select2({
            width: "100%", // Full width
            placeholder: "Search and select states", // Placeholder text
        });
    }
});
