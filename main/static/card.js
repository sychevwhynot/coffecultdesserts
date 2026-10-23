document.addEventListener('DOMContentLoaded', () => {
    const btn = document.getElementById('show-more-btn');
    if (!btn) return;

    const section = document.getElementById('three');
    let expanded = false;

    btn.addEventListener('click', () => {
        expanded = !expanded;

        const hidden = document.querySelectorAll('.extra-category');

        if (expanded) {
            hidden.forEach(el => {
                el.classList.remove('is-hidden');
                el.classList.add('is-visible');
            });
        } else {
            hidden.forEach(el => {
                el.classList.remove('is-visible');
                el.classList.add('is-hidden');
            });
        }

        btn.textContent = expanded ? 'Скрыть' : 'Показать все';

        section?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});