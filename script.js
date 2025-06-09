document.getElementById('translateBtn').addEventListener('click', async () => {
  const text = document.getElementById('inputText').value.trim();
  const source = document.getElementById('source').value;
  const target = document.getElementById('target').value;
  if (!text) return alert('Veuillez saisir un texte.');

  const res = await fetch('https://ton-backend-url/translate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer 123456789-SECRET'
    },
    body: JSON.stringify({ text, source_language: source, target_language: target })
  });
  const json = await res.json();
  document.getElementById('result').innerText = json.translated_text
    || json.detail || 'Erreur lors de la traduction.';
});
