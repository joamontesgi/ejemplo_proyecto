document.getElementById('file').addEventListener('submit', function(event){
    event.preventDefault();
    let formData = new FormData();
    let fileInput = document.getElementById('fileInput');

    if(fileInput.files.length>0){
        formData.append('file', fileInput.files[0]);
        fetch('http://127.0.0.1:5000/predict',{
            method: 'POST',
            body: formData
        })
        .then(response=>response.json())
        .then(data=>{
            alert('Se recibió existosamente la respuesta')
        })
        
    }else{
        alert('No se cargó un archivo');
    }
});

// fetch js = API DE JS
// AXIOS