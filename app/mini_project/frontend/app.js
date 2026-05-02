const apiBase = "http://127.0.0.1:5000";

const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const tokenBox = document.getElementById("token");
const taskTitle = document.getElementById("taskTitle");
const taskList = document.getElementById("taskList");

let token = "";

function authHeaders() {
  return token ? { Authorization: `Bearer ${token}` } : {};
}

async function login() {
  const response = await fetch(`${apiBase}/auth/token`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      email: emailInput.value,
      password: passwordInput.value,
    }),
  });

  const data = await response.json();
  token = data.token || "";
  tokenBox.textContent = token ? `Token: ${token}` : "Login failed";
}

async function loadTasks() {
  taskList.innerHTML = "";
  const response = await fetch(`${apiBase}/api/tasks`, {
    headers: { ...authHeaders() },
  });
  const tasks = await response.json();

  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.textContent = `${task.id}. ${task.title} (${task.completed ? "done" : "open"})`;
    taskList.appendChild(li);
  });
}

async function createTask() {
  const response = await fetch(`${apiBase}/api/tasks`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      ...authHeaders(),
    },
    body: JSON.stringify({ title: taskTitle.value }),
  });

  if (response.ok) {
    taskTitle.value = "";
    await loadTasks();
  }
}

document.getElementById("login").addEventListener("click", login);
document.getElementById("loadTasks").addEventListener("click", loadTasks);
document.getElementById("createTask").addEventListener("click", createTask);
