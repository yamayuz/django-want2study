function radio_click() {
  document.getElementById("ch_servings_submit").click();
}

$('form').on('submit', e => {
  
  if (e.target.id == 'list_add' || e.target.id == 'sort-form') {
      return null
  } 

  e.preventDefault();  
  let id = '#' + e.target.id
  let url = $(id).prop("action");

  $.ajax({
  'url': url,
  'type': 'GET',
  'data': {
      'testdata': 'test',
  },
  'dataType': 'json'
  }).done(response => {

  let result_status = response.result['status']
  let add_star = response.result['add_star']
  let current_id = 'star-' + response.result['pk']

  if (result_status == 0 && add_star == true) {
      document.getElementById(current_id).classList.add('favorite');
  } else if (result_status == 0 && add_star == false) {
      document.getElementById(current_id).classList.remove('favorite');
  }
  });
});