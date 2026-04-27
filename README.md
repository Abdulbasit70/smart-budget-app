💰 Smart Budgeting Web App
A simple and interactive web application to track income, expenses and savings in real-time. Built using Python and Streamlit, this app helps users understand their financial habits through clean dashboards and visual insights.
________________________________________
🚀 Features
•	➕ Add income and expense transactions
•	📂 Categorize spending
•	📊 Interactive dashboard with financial metrics
•	📈 Visualizations for spending analysis
•	🗑️ Delete transactions easily
•	💾 Persistent storage using SQLite
________________________________________
🧰 Tech Stack
•	Python – Core programming language
•	Streamlit – For building the web UI
•	Pandas – Data manipulation and analysis
•	SQLite – Lightweight database for storage
________________________________________
📸 Screenshots
 
 

 
________________________________________
⚙️ Installation & Setup
1️ Clone the repository
git clone https://github.com/Abdulbasit70/smart-budget-app.git
cd smart-budget-app
________________________________________
2️ Create virtual environment (optional but recommended)
python -m venv venv
Activate:
Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate
________________________________________
3️ Install dependencies
pip install -r requirements.txt
If you don’t have requirements.txt, run:
pip install streamlit pandas
________________________________________
4️ Run the app
streamlit run app.py
The app will open in your browser.
________________________________________
🗄️ Project Structure
smart_budget_app/
│
├── app.py            # Main Streamlit app
├── database.py       # Database operations
├── budget.db         # SQLite database (auto-created)
├── requirements.txt
└── venv/
________________________________________
💡 How It Works
•	User inputs transactions through the UI
•	Data is stored in SQLite database
•	Pandas processes the data for analysis
•	Streamlit displays insights and charts
________________________________________
📈 Future Improvements
•	Budget alerts & notifications
•	Monthly reports
•	Export data (CSV/Excel)
•	User authentication system
•	Deploy app online
________________________________________
🌐 Deployment
You can deploy this app using Streamlit Cloud or similar platforms.
________________________________________
🙌 Acknowledgements
This project was built as part of learning full-stack data applications using Python.
________________________________________
📬 Contact
Feel free to connect with me on LinkedIn or reach out for feedback!
