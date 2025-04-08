document.getElementById('userForm')
    .addEventListener('submit', async function(e) {
      e.preventDefault();

      document.getElementById('usernameError').textContent = '';
      document.getElementById('passwordError').textContent = '';

      const username = document.getElementById('username').value.trim();
      const password = document.getElementById('password').value;

      try {
        const response = await fetch('http://127.0.0.1:8000/auth', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({username, password})
        });

        if (response.status === 401) {
          throw new Error('Incorrect username or password');
        }

        const result = await response.json();
        window.location.href = result.redirect_url;
      } catch (err) {
        alert(err.message);
      }
    });
