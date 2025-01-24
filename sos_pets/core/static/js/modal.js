<script>
   function openModal(petId) {
       fetch(`/detalhes_pet/${petId}/`)
           .then(response => response.text())
           .then(data => {
               document.getElementById('modalContent').innerHTML = data;
               document.getElementById('petModal').style.display = 'block';

               // Espera 500ms para garantir que o modal foi carregado
               setTimeout(initializeMap, 500);  // Ajuste o tempo de espera aqui se necessário
           })
           .catch(error => console.error('Erro ao carregar detalhes do pet:', error));
   }

    function initializeMap() {
       // Pega os valores de latitude e longitude do input oculto
       let petLatitude = parseFloat(document.getElementById('pet-latitude').value);
       let petLongitude = parseFloat(document.getElementById('pet-longitude').value);

       console.log('Latitude:', petLatitude, 'Longitude:', petLongitude);  // Verifique no console se as coordenadas estão corretas

       // Verifica se as coordenadas são válidas, caso contrário, usa um valor padrão
       if (isNaN(petLatitude) || isNaN(petLongitude)) {
           petLatitude = -23.5505;  // Latitude padrão
           petLongitude = -46.6333; // Longitude padrão
       }

       // Cria o mapa com a localização do pet
       let mapModal = L.map('mapModal').setView([petLatitude, petLongitude], 14);  // Zoom 14 para ver claramente o marcador

       // Adiciona a camada de tiles do OpenStreetMap
       L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
           maxZoom: 19,
       }).addTo(mapModal);

       // Cria o marcador inicial nas coordenadas do pet
       let marker = L.marker([petLatitude, petLongitude], {draggable: false}).addTo(mapModal); // O marcador não pode ser arrastado

       // Adiciona o pop-up com a localização
       marker.bindPopup(`<b>${pet.nome}</b><br>Última localização conhecida: ${pet.address}`).openPopup();

       // Caso o marcador tenha que ser movido (mesmo que para localização padrão), pode-se permitir isso
       marker.on('dragend', function (e) {
           document.getElementById("id_latitude").value = e.target.getLatLng().lat;
           document.getElementById("id_longitude").value = e.target.getLatLng().lng;
       });
   }

   // Chama a função para inicializar o mapa
   initializeMap();

   // Função para fechar o modal
   function closeModal() {
       document.getElementById('petModal').style.display = 'none';
   }


    // Função que busca a lista de pets e chama a função de adicionar marcadores
    function carregarPets() {
        fetch('/api/pets/')
            .then(response => response.json())
            .then(pets => {
                if (pets.length === 0) {
                    console.log("Nenhum pet encontrado!");
                } else {
                    adicionarMarcadores(pets);
                }
            })
            .catch(error => {
                console.error('Erro ao carregar pets:', error);
            });
    }



       carregarPets();

</script>