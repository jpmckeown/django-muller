document.addEventListener('DOMContentLoaded', function () {
    const titleField = document.getElementById('id_title');
    const slugField = document.getElementById('id_slug');
    let slugManuallyChanged = false;

    slugField.addEventListener('change', function () {
        slugManuallyChanged = true;
    });

    titleField.addEventListener('input', function () {
        if (!slugManuallyChanged) {
            const stripped = titleField.value.replace(/^the\s+/i, '');
            slugField.value = URLify(stripped, 255);
        }
    });
});
