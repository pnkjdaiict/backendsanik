document.addEventListener("DOMContentLoaded", function() {
    const selectAllCheckbox = document.createElement("input");
    selectAllCheckbox.type = "checkbox";
    selectAllCheckbox.id = "select-all-states";
    const selectAllLabel = document.createElement("label");
    selectAllLabel.setAttribute("for", "select-all-states");
    selectAllLabel.innerText = "Select All States";

    // Insert the "Select All" checkbox above the states checkboxes
    const statesField = document.querySelector(".field-states"); // Adjust based on your template
    if (statesField) {
        statesField.insertBefore(selectAllLabel, statesField.firstChild);
        statesField.insertBefore(selectAllCheckbox, statesField.firstChild);

        // Handle the click event for "Select All"
        selectAllCheckbox.addEventListener("change", function() {
            const checkboxes = statesField.querySelectorAll("input[type='checkbox']");
            checkboxes.forEach(function(checkbox) {
                checkbox.checked = selectAllCheckbox.checked;
            });
        });
    }
});
