# 🎓 University Student Analytics Dashboard

**Data Mining – Activity I: Data Visualization and Dashboard Deployment**  
Universidad de la Costa · Department of Computer Science and Electronics  
Professor: José Escorcia-Gutierrez, Ph.D.

---

## 👥 Team Members
- Team Member 1
- Team Member 2
- Team Member 3
- Team Member 4

---

## 📋 Purpose

This dashboard provides interactive visualizations of university student data covering admissions, enrollment, retention rates, and satisfaction scores across academic years (2015–2024) and departments (Engineering, Business, Arts, Science).

It was built as part of **Activity I** of the Data Mining course and demonstrates the complete workflow: data exploration in Google Colab → interactive dashboard in Streamlit → deployment via Streamlit Cloud.

---

## 📊 Features

- **KPI Cards** – Average retention rate, satisfaction, total enrolled, and admission rate.
- **Line charts** – Retention rate and satisfaction trends over time.
- **Bar chart** – Spring vs Fall term comparison.
- **Donut chart** – Department enrollment distribution.
- **Stacked bar chart** – Enrollment by department per year.
- **Multi-line chart** – Applications → Admitted → Enrolled funnel.
- **Interactive filters** – Year, Term, Department (sidebar).

---

## 🗂️ Repository Structure

```
├── app.py                  # Streamlit dashboard
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── university_student_data.csv   # Dataset
```

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## ☁️ Streamlit Cloud Deployment

1. Push this repository to GitHub.
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud) and sign in.
3. Click **"New app"** → select your repository → set **Main file path** to `app.py`.
4. Click **Deploy**.

---

## 📁 Dataset

The dataset `university_student_data.csv` contains 20 records (2015–2024, Spring & Fall) with the following columns:

| Column | Description |
|---|---|
| Year | Academic year |
| Term | Semester (Spring / Fall) |
| Applications | Total applications received |
| Admitted | Number of students admitted |
| Enrolled | Number of students enrolled |
| Retention Rate (%) | Percentage of students retained year-over-year |
| Student Satisfaction (%) | Average satisfaction score |
| Engineering Enrolled | Enrolled students in Engineering |
| Business Enrolled | Enrolled students in Business |
| Arts Enrolled | Enrolled students in Arts |
| Science Enrolled | Enrolled students in Science |

---

## 🔍 Key Findings

- Retention rates show a positive upward trend from 85% (2015) to 90% (2024).
- Student satisfaction improved consistently from 78% to 88%.
- Engineering is the department with the highest enrollment across all years.
- A dip in applications and retention occurred in 2020, likely related to the COVID-19 pandemic.
- **Actionable insight:** The university should investigate the factors driving the satisfaction increase in Engineering and replicate those strategies in Arts and Science, where enrollment growth has slowed.
