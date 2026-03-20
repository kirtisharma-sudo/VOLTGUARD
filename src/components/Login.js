const handleSubmit = async (e) => {
  e.preventDefault();
  const response = await fetch('/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password: pass }),
  });

  const data = await response.json();
  if (data.status === 'success') {
    onLogin(data.role); // Logged in!
  } else {
    alert("Unauthorized Access Attempt Detected.");
  }
};
