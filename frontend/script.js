// frontend/script.js
const API_URL = "http://127.0.0.1:5000/predict"; // change if your backend runs elsewhere

document.getElementById('heartForm').addEventListener('submit', async function(e){
    e.preventDefault();

    const data = {
        age: document.getElementById('age').value,
        sex: document.getElementById('sex').value,
        cp: document.getElementById('cp').value,
        trestbps: document.getElementById('trestbps').value,
        chol: document.getElementById('chol').value,
        fbs: document.getElementById('fbs').value,
        restecg: document.getElementById('restecg').value,
        thalach: document.getElementById('thalach').value,
        exang: document.getElementById('exang').value
    };

    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = "Predicting...";

    try {
        const resp = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data)
        });

        if (!resp.ok) {
            const err = await resp.json().catch(()=>({message:resp.statusText}));
            resultDiv.innerHTML = `<div class="error">Error: ${err.error || err.message || 'Server error'}</div>`;
            return;
        }

        const json = await resp.json();
        // Show interpreted result
        let html = `<h3>Result</h3>`;
        html += `<p><strong>Prediction:</strong> ${json.label} (class ${json.prediction})</p>`;
        if (json.probability !== null && json.probability !== undefined) {
            html += `<p><strong>Confidence:</strong> ${(json.probability*100).toFixed(1)}%</p>`;
        }
        resultDiv.innerHTML = html;
    } catch (err) {
        resultDiv.innerHTML = `<div class="error">Request failed: ${err.message}</div>`;
    }
});











// HOW TO RUN PROJECT

// cd backend
//.venv\Scripts\Activate.ps1
//python app.py




// input and output for this PromiseRejectionEvent
// Example 1
// {
//   "Age": 30,
//   "Sex": "Male",
//   "Chest Pain Type": 2,
//   "Resting Blood Pressure": 140,
//   "Cholesterol": 230,
//   "Fasting Blood Sugar > 120 mg/dl": "No",
//   "Resting ECG": 1,
//   "Max Heart Rate Achieved": 170,
//   "Exercise Induced Angina": "No"
// }


// Expected Output:
// Prediction: No Heart Disease (class 0)
// Confidence: ~75%

// Example 2
// {
//   "Age": 55,
//   "Sex": "Male",
//   "Chest Pain Type": 3,
//   "Resting Blood Pressure": 160,
//   "Cholesterol": 280,
//   "Fasting Blood Sugar > 120 mg/dl": "Yes",
//   "Resting ECG": 2,
//   "Max Heart Rate Achieved": 120,
//   "Exercise Induced Angina": "Yes"
// }


// Expected Output:
// Prediction: Heart Disease (class 1)
// Confidence: ~90%

// Example 3
// {
//   "Age": 45,
//   "Sex": "Female",
//   "Chest Pain Type": 1,
//   "Resting Blood Pressure": 150,
//   "Cholesterol": 200,
//   "Fasting Blood Sugar > 120 mg/dl": "No",
//   "Resting ECG": 0,
//   "Max Heart Rate Achieved": 160,
//   "Exercise Induced Angina": "No"
// }


// Expected Output:
// Prediction: No Heart Disease (class 0)
// Confidence: ~80%

// Example 4 (High Risk)
// {
//   "Age": 60,
//   "Sex": "Male",
//   "Chest Pain Type": 4,
//   "Resting Blood Pressure": 180,
//   "Cholesterol": 300,
//   "Fasting Blood Sugar > 120 mg/dl": "Yes",
//   "Resting ECG": 2,
//   "Max Heart Rate Achieved": 110,
//   "Exercise Induced Angina": "Yes"
// }


// Expected Output:
// Prediction: Heart Disease (class 1)
// Confidence: ~95%