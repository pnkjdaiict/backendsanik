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
