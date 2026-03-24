async function cargar() {
  const res = await fetch("/productos");
  const data = await res.json();

  const lista = document.getElementById("lista");
  lista.innerHTML = "";

  data.forEach(p => {
    const li = document.createElement("li");
    li.textContent = `${p.nombre} - $${p.precio}`;
    lista.appendChild(li);
  });
}

async function agregar() {
  const nombre = document.getElementById("nombre").value;
  const precio = document.getElementById("precio").value;

  if (!nombre || !precio) {
    alert("Completa los campos");
    return;
  }

  await fetch("/productos", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ nombre, precio })
  });

  document.getElementById("nombre").value = "";
  document.getElementById("precio").value = "";

  cargar();
}

cargar();