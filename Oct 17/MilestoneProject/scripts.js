const API_BASE = "http://localhost:8000"; // Update if hosted elsewhere

document.getElementById("studentForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const student = {
    StudentID: parseInt(document.getElementById("studentId").value),
    Name: document.getElementById("name").value,
    Age: parseInt(document.getElementById("age").value),
    Course: document.getElementById("course").value
  };

  const res = await fetch(`${API_BASE}/students`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(student)
  });

  if (res.ok) {
    alert("Student added!");
    fetchStudents();
  } else {
    alert("Error adding student.");
  }
});

async function fetchStudents() {
  const res = await fetch(`${API_BASE}/students`);
  const students = await res.json();

  const list = document.getElementById("studentList");
  list.innerHTML = "";

  students.forEach((s) => {
    const li = document.createElement("li");
    li.textContent = `${s.StudentID} - ${s.Name} (${s.Course})`;
    list.appendChild(li);
  });
}
