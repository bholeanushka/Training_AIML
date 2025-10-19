const API_BASE = "http://localhost:8000";

const studentForm = document.getElementById("studentForm");
const studentList = document.getElementById("studentList");

// Handle Add or Update
studentForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const student = {
    StudentID: parseInt(document.getElementById("studentId").value),
    Name: document.getElementById("name").value,
    Age: parseInt(document.getElementById("age").value),
    Course: document.getElementById("course").value
  };

  // Try POST first, if fails, try PUT
  let res = await fetch(`${API_BASE}/students`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(student)
  });

  if (!res.ok) {
    // If student ID exists, update instead
    res = await fetch(`${API_BASE}/students/${student.StudentID}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(student)
    });
  }

  if (res.ok) {
    alert("Student added/updated successfully!");
    studentForm.reset();
    fetchStudents();
  } else {
    const err = await res.json();
    alert("Error: " + err.detail);
  }
});

// Fetch all students and display
async function fetchStudents() {
  const res = await fetch(`${API_BASE}/students`);
  const students = await res.json();

  studentList.innerHTML = "";

  students.forEach((s) => {
    const li = document.createElement("li");
    li.textContent = `${s.StudentID} - ${s.Name} (${s.Course}) `;

    // Update button pre-fills form
    const updateBtn = document.createElement("button");
    updateBtn.textContent = "Edit";
    updateBtn.onclick = () => {
      document.getElementById("studentId").value = s.StudentID;
      document.getElementById("name").value = s.Name;
      document.getElementById("age").value = s.Age;
      document.getElementById("course").value = s.Course;
    };

    // Delete button
    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.onclick = async () => {
      if (confirm(`Delete student ${s.StudentID}?`)) {
        const delRes = await fetch(`${API_BASE}/students/${s.StudentID}`, { method: "DELETE" });
        if (delRes.ok) fetchStudents();
        else alert("Error deleting student");
      }
    };

    li.appendChild(updateBtn);
    li.appendChild(deleteBtn);
    studentList.appendChild(li);
  });
}

window.runETL = async function () {
  try {
    const res = await fetch(`${API_BASE}/process-etl`, { method: "POST" });
    const data = await res.json();
    if (res.ok) {
      alert("student_result.csv has been generated!");
      console.log(data);
    } else {
      alert("ETL failed: " + (data.detail || "Unknown error"));
    }
  } catch (error) {
    console.error("ETL error:", error);
    alert("ETL request failed");
  }
};

window.generateInsights = async function () {
  try {
    const res = await fetch(`${API_BASE}/generate-analytics`, { method: "POST" });
    const data = await res.json();
    if (res.ok) {
      alert("student_insights.txt has been generated!");
      console.log(data);
    } else {
      alert("Generation failed: " + (data.detail || "Unknown error"));
    }
  } catch (error) {
    console.error("Generation error:", error);
    alert("Analytics generation request failed");
  }
};


// Load students on page load
fetchStudents();


