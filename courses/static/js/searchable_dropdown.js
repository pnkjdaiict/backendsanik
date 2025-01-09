document.addEventListener('DOMContentLoaded', function () {
    const searchInputs = document.querySelectorAll('.searchable-field');
    searchInputs.forEach((searchInput) => {
        const parent = searchInput.closest('.form-group');
        const checkboxes = parent.querySelectorAll('input[type="checkbox"]');
        
        searchInput.addEventListener('input', function () {
            const filter = searchInput.value.toLowerCase();
            checkboxes.forEach((checkbox) => {
                const label = checkbox.nextElementSibling;
                if (label && label.textContent.toLowerCase().includes(filter)) {
                    checkbox.closest('label').style.display = '';
                } else {
                    checkbox.closest('label').style.display = 'none';
                }
            });
        });
    });
});
