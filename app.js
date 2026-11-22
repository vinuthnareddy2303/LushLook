const form = document.querySelector("#booking-form");
const statusMessage = document.querySelector("#form-status");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  statusMessage.textContent = "Sending your request…";
  const payload = Object.fromEntries(new FormData(form).entries());

  try {
    const response = await fetch("http://127.0.0.1:5000/api/bookings", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error || "Could not save the request.");
    statusMessage.textContent = "Your appointment request was submitted successfully.";
    form.reset();
  } catch (error) {
    statusMessage.textContent = "Request not saved. Start the Flask backend and configure MySQL. (" + error.message + ")";
  }
});
