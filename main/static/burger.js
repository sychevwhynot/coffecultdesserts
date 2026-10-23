document.addEventListener('DOMContentLoaded', function () {
    const burger = document.getElementById('burger');
    const nav = document.getElementById('mobile-nav');
    if (!burger || !nav) return;

    function toggleMenu(open) {
        const isOpen = open ?? !nav.classList.contains('is-open');
        nav.hidden = false;                     // всегда снимаем hidden перед анимацией
        nav.classList.toggle('is-open', isOpen);
        burger.classList.toggle('is-open', isOpen);
        burger.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
    }

    burger.addEventListener('click', () => toggleMenu());

    nav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => toggleMenu(false));
    });

    // При переходе на lg и выше — закрыть меню
    const mq = window.matchMedia('(min-width: 992px)');
    mq.addEventListener('change', e => {
        if (e.matches) toggleMenu(false);
    });
});
