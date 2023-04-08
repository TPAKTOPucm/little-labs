function lockedProfile() {
  const showButtons = document.querySelectorAll('button');

  showButtons.forEach(button => {
    button.addEventListener('click', () => {
      const parentDiv = button.parentNode;
      const hiddenFields = parentDiv.nextElementSibling;

      if (parentDiv.querySelector('input[value="unlock"]').checked === false) {
        return;
      }

      if (getComputedStyle(hiddenFields).display === 'block') {
        return;
      }

      hiddenFields.style.display = 'block';

      hiddenFields.querySelector('button').addEventListener('click', () => {
        if (parentDiv.querySelector('input[value="unlock"]').checked === false) {
          return;
        }

        hiddenFields.style.display = 'none';
      });
    });
  });
}