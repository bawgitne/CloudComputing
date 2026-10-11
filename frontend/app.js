// Week 1: UI mock; API call will be implemented in week 3.
document.getElementById('form').addEventListener('submit', event => {
  event.preventDefault();
  document.getElementById('notice').textContent = 'Tuần 1: chưa kết nối API. Chức năng chat sẽ hoàn thiện sau.';
});
