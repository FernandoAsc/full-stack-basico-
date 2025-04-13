const API_URL = 'http://localhost:5000/pets';

document.addEventListener("DOMContentLoaded", carregarPets);
document.getElementById("pet-form").addEventListener("submit", cadastrarPet);

function carregarPets() {
  fetch(API_URL)
    .then(res => res.json())
    .then(pets => {
      const container = document.getElementById("lista-pets");
      container.innerHTML = "";
      pets.forEach(pet => {
        const card = document.createElement("div");
        card.className = "col-md-4";
        card.innerHTML = `
          <div class="card">
            <div class="card-body">
              <h5 class="card-title">${pet.nome}</h5>
              <p class="card-text">Tipo: ${pet.tipo}<br>Idade: ${pet.idade} ano(s)</p>
              <button class="btn btn-danger btn-sm" onclick="deletarPet(${pet.id})">Excluir</button>
            </div>
          </div>
        `;
        container.appendChild(card);
      });
    });
}

function cadastrarPet(e) {
  e.preventDefault();
  const nome = document.getElementById("nome").value;
  const tipo = document.getElementById("tipo").value;
  const idade = document.getElementById("idade").value;

  fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nome, tipo, idade }),
  })
    .then(() => {
      document.getElementById("pet-form").reset();
      carregarPets();
    });
}

function deletarPet(id) {
  fetch(`${API_URL}/${id}`, { method: "DELETE" })
    .then(() => carregarPets());
}
