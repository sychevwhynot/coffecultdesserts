(function () {
    const KEY = 'cookie-accepted';
    const banner = document.getElementById('cookie-banner');
    const btn = document.getElementById('cookie-accept');

    if (!banner || !btn) return;

    let accepted = null;
    try {
        accepted = localStorage.getItem(KEY);
    } catch (e) {
    }
    if (accepted === '1') return;

    banner.hidden = false;
    requestAnimationFrame(() => {
        banner.classList.add('is-visible');
    });

    btn.addEventListener('click', function () {
        banner.classList.remove('is-visible');
        try {
            localStorage.setItem(KEY, '1');
        } catch (e) {}
        setTimeout(() => banner.remove(), 400);
    });
})();
