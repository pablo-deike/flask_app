function editEmail() {
  document.getElementById('userForm').removeAttribute('hidden');
  document.getElementById('row').hidden = true;
  document.getElementById('userForm').addEventListener('submit', changeEmail);
}

async function changeEmail(event) {
  event.preventDefault();
  let hasError = false;
  document.getElementById('emailError').textContent = '';
  const email = document.getElementById('email').value.trim();

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    document.getElementById('emailError').textContent =
        'Invalid email address.';
    hasError = true;
  }

  if (!hasError) {
    try {
      const response = await fetch('http://127.0.0.1:8000/change_user_attr', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({email})
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const result = await response.json();
      window.location.href = result.redirect_url;
      document.querySelector('.gfg').textContent = result.email;
      window.location.reload();
    } catch (err) {
      alert('Failed to submit: ' + err.message);
    }
  }
};
