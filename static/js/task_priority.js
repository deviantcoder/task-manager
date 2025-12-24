document.querySelectorAll('.dropdown-item').forEach(item => {
    item.addEventListener('click', function (e) {
        e.preventDefault();

        const value = this.dataset.value;
        const label = this.textContent.trim();

        document.getElementById('priority-input').value = value;

        const button = document.getElementById('priority-button');
        button.textContent = label;

        button.classList.remove(
            'btn-outline-secondary',
            'btn-success',
            'btn-warning',
            'btn-danger'
        );

        if (value === 'low') button.classList.add('btn-success');
        if (value === 'medium') button.classList.add('btn-warning');
        if (value === 'high') button.classList.add('btn-danger');
    });
});