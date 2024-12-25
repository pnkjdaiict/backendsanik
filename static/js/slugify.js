(function($) {
    $(document).ready(function() {
        $('#id_title').on('keyup change', function() {
            var title = $(this).val();
            var slug = title.toLowerCase()
                            .replace(/[^a-z0-9]+/g, '-')  // Replace non-alphanumeric characters with hyphens
                            .replace(/^-+|-+$/g, '');    // Remove leading/trailing hyphens
            $('#id_slug_field').val(slug);
        });
    });
})(django.jQuery);

document.addEventListener('DOMContentLoaded', function () {
    const selectAllCheckbox = document.createElement('input');
    selectAllCheckbox.type = 'checkbox';
    selectAllCheckbox.id = 'select-all-states';
    selectAllCheckbox.style.marginRight = '10px';

    const selectAllLabel = document.createElement('label');
    selectAllLabel.setAttribute('for', 'select-all-states');
    selectAllLabel.textContent = 'Select All States';
    
    const statesContainer = document.querySelector('fieldset'); // Ensure this is the correct container for your states field
    statesContainer.insertBefore(selectAllCheckbox, statesContainer.firstChild);
    statesContainer.insertBefore(selectAllLabel, selectAllCheckbox.nextSibling);

    selectAllCheckbox.addEventListener('change', function () {
        const checkboxes = document.querySelectorAll('input[type="checkbox"][name="states"]');
        checkboxes.forEach(checkbox => checkbox.checked = selectAllCheckbox.checked);
    });
});
