$.get('https://swapi-api.hbtn.io/api/films/?format=json',
  function (data) {
    for (const i of data.results) {
      $('UL#list_movies').append('<li>' + i.title + '</li>');
    }
  }
);
/* JSON.stringify() keep this if you want to know
what its inside of data */
