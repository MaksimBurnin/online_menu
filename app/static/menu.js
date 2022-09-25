window.addEventListener('DOMContentLoaded', () => {
  menu();
});

function menu(){
  const csrfToken = document.querySelector('meta[name=csrftoken]').getAttribute('value');
  const items = document.querySelectorAll('.dish');

  for(item of items){
    const id = item.dataset.id;
    const addButton = item.querySelector('.dish__add');
    const removeButton = item.querySelector('.dish__remove');

    addButton.addEventListener('click', () => {
      cartRequest(id, true);
    });
    removeButton.addEventListener('click', () => {
      cartRequest(id, false);
    });
  }

  function cartRequest(id, add){
    const formData = new FormData();

    formData.append('action', add ? 'add' : 'remove');
    formData.append('id', id);

    return fetch('/cart', {
      method: 'POST',
      body: formData,
      headers: {
        'X-CSRFToken': csrfToken,
      }
    })
      .then((response) => response.json())
      .then((data) => {
      console.log('data', data);
      updateCart(data);
    });
  }

  function updateCart(data){
    for(item of items){
      const id = item.dataset.id;
      const qty = data[id] || 0;

      item.querySelector('.dish__qty').innerHTML = qty;

      item.classList.toggle('added', qty > 0);
    }
  }
}
