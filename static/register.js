document.getElementById('userForm')
    .addEventListener('submit', async function(e) {
      e.preventDefault();

      document.getElementById('usernameError').textContent = '';
      document.getElementById('emailError').textContent = '';
      document.getElementById('passwordError').textContent = '';

      const username = document.getElementById('username').value.trim();
      const email = document.getElementById('email').value.trim();
      const password = document.getElementById('password').value;

      let hasError = false;

      if (username.length < 2) {
        document.getElementById('usernameError').textContent =
            'username must be at least 2 characters.';
        hasError = true;
      }

      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRegex.test(email)) {
        document.getElementById('emailError').textContent =
            'Invalid email address.';
        hasError = true;
      }

      if (password.length < 6) {
        document.getElementById('passwordError').textContent =
            'Password must be at least 6 characters.';
        hasError = true;
      }

      if (!hasError) {
        try {
          const response = await fetch('http://127.0.0.1:8000/register/save', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({username, email, password})
          });

          if (!response.ok) {
            throw new Error('Network response was not ok');
          }

          const result = await response.json();
          window.location.href = result.redirect_url;
        } catch (err) {
          alert('Failed to submit: ' + err.message);
        }
      }
    });
