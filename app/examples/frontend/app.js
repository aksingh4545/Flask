const apiBase = "http://127.0.0.1:5000/api/notes";

const loadBtn = document.getElementById("load");
const list = document.getElementById("notes");

loadBtn.addEventListener("click", async () => {
  list.innerHTML = "";
  const response = await fetch(apiBase);
  const notes = await response.json();

  notes.forEach((note) => {
    const li = document.createElement("li");
    li.textContent = `${note.id}. ${note.title}`;
    list.appendChild(li);
  });
});
