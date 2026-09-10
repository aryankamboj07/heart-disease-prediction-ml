## Heart Disease Prediction — Local setup

1. Create virtualenv and install backend deps:
   cd backend
   python -m venv .venv
   source .venv/bin/activate    # (Linux/macOS)
   .venv\Scripts\Activate.ps1   # (Windows PowerShell)
   pip install -r requirements.txt

2. Put your trained model `model.pkl` inside backend/.
   - If you trained the model in `End-to-End-HeartDisease.ipynb`, run:
       import joblib
       joblib.dump(trained_model, "model.pkl")
     and copy that file to backend/.

   - Or use train_model.py (modify dataset path) to create model.pkl.

3. Start backend:
   python app.py
   (server runs on http://127.0.0.1:5000)

4. Serve frontend:
   - Simplest: open frontend/index.html in browser (CORS allowed because backend uses flask-cors).
   - Or run a simple static server:
       cd frontend
       python -m http.server 8000
     then open http://127.0.0.1:8000

5. Fill the form and click Predict.
