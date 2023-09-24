
const data = { 
    name: 'anton', 
    age: '39'
  };
  
  fetch('http://localhost:3344/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
        var d = JSON.parse(data)
        console.log(typeof d);
        console.log(d);
    })
    .catch((error) => {
      console.log('Error:', error);
    });