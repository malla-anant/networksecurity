# 📡 Network Security Prediction App

> Detect malicious or suspicious URLs using machine learning — upload a CSV of URL features, and get predictions instantly.

---

## 🌐 Live Demo / Web App

You can try the deployed app here:  
**[🛡️ Network Security Prediction App – Streamlit Cloud]([(https://malla-anant-networksecurity-streamlit-app-ri7wmo.streamlit.app/)])**

---

## 🧠 Project Overview

This project is designed to classify URLs as benign or malicious using machine learning. It includes:

- A **data pipeline**: ingestion → validation → transformation  
- **Model training** module for ML model development  
- **Backend API** using FastAPI for serving predictions  
- **Frontend UI** using Streamlit for easy CSV upload and prediction display  
- Optional **MongoDB integration** for storing data and artifacts  
- Produces output CSV and HTML-table view of predictions  

---

## 🔧 Setup & Run Locally

1. Clone the repository

git clone https://github.com/malla-anant/networksecurity.git
cd networksecurity

2. Create a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run backend (FastAPI)

# Start the backend using Uvicorn with auto-reload
uvicorn app:app --reload

5. Run frontend (Streamlit)

streamlit run streamlit_app.py
Visit: http://localhost:8501

Upload a CSV of URL features → Click Predict → See results in table + download option

🧪 Input / Output Format

Input: CSV file where each row has feature columns like:
having_IP_Address, URL_Length, Shortining_Service, having_At_Symbol, ...

Output: Same data plus a new column predicted_column (e.g., 1.0 for malicious, 0.0 for benign).
Output is shown in table in UI; also saved in prediction_output/output.csv.

🛠 Technologies & Libraries

Python 3.x
FastAPI — backend API
Streamlit — frontend UI
Pandas, NumPy, scikit-learn — data & ML
MongoDB — optional for data storage
Jinja2 — HTML templating for backend
Includes custom modules for logging, exception handling, and ML pipelines.

🚀 Deployment — Streamlit Community Cloud

Make sure your repo has streamlit_app.py, requirements.txt, and all required files.
Push changes to GitHub main branch.
Go to Streamlit Cloud → New app → pick your repo, branch & file → Deploy.
Once deployed, copy the public URL and update the Live Demo link above.

📝 Notes & Tips

Ensure your trained model and preprocessor files are present under final_model/.
Input CSV must match the feature schema expected by the model.
Dependencies are managed via requirements.txt.

👤 Author
Malla Anant
