document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('order-form');
    const submitBtn = document.getElementById('order-submit');
    const messageBox = document.getElementById('form-message');

    if (!form) return;

    function clearState() {
        form.querySelectorAll('.invalid-feedback').forEach(el => el.textContent = '');
        form.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));
        messageBox.textContent = '';
        messageBox.className = 'form-message mt-3';
    }

    function showErrors(errors) {
        for (const [field, messages] of Object.entries(errors)) {
            const input = form.querySelector(`[name="${field}"]`);
            const errorEl = form.querySelector(`[data-error="${field}"]`);
            if (input) input.classList.add('is-invalid');
            if (errorEl) errorEl.textContent = messages.join(' ');
        }
    }

    function showMessage(text, type) {
        messageBox.textContent = text;
        messageBox.classList.remove('text-success', 'text-danger');
        messageBox.classList.add(type === 'success' ? 'text-success' : 'text-danger');
    }

    form.addEventListener('submit', async function (e) {
        e.preventDefault();
        clearState();

        submitBtn.disabled = true;
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Отправка...';

        const formData = new FormData(form);

        try {
            const response = await fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                },
                body: formData,
            });

            const data = await response.json();

            if (response.ok && data.success) {
                showMessage(data.message || 'Заявка отправлена! Скоро мы с вами свяжемся', 'success');
                form.reset();
            } else {
                if (data.errors) {
                    showErrors(data.errors);
                }
            }
        } catch (err) {
            console.error('AJAX error:', err);
        } finally {
            submitBtn.disabled = false;
            submitBtn.textContent = originalText;
        }
    });
});
