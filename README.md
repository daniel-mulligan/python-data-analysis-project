# python-data-analysis-project

# 🎓 Exam Data Analysis with Python

This project simulates, cleans, analyzes, and visualizes examination data for a tertiary institution. Using Python, it generates **two realistic datasets** and applies statistical analysis to uncover patterns in student performance, study habits, and demographics.

[Code Developement Process](docs/code-developement-process.md) 

---

## 📦 Project Overview

This project covers:

- Simulated exam data generation (2 datasets)  
- Data cleaning and augmentation  
- Frequency analysis using Pandas  
- Visualization with Matplotlib  
- Insightful interpretation of each dataset’s patterns  
- Final conclusions drawn from comparison of both datasets

for a more detailed overview please view: [Project Overview](docs/project-overview.md) 

---

## 🧰 Tools & Environment

- **IDE:** Spyder 5.5.1 (Anaconda)  
- **Python Version:** 3.12.7 (64-bit)  
- **Libraries Used:**  
  - `Pandas`  
  - `Matplotlib`  
  - `NumPy`  

- **Operating System:** Windows 11

---

## 📊 Features & Visuals

The project includes the following visualizations:

1. **Bar Chart** – Student age groups  
2. **Line Graph** – Time studied vs. mark achieved  
3. **Scatter Plot** – Mark achieved vs. exam duration  
4. **Scatter Plot** – Age vs. study time

Each visualization was produced for **both datasets**, allowing cross-comparison and deeper insight.

---

## 🚀 How to Run

1. 	open csv_gen.py and run it to generate the CSV file.

2. 	Open csv_clean.py and run it to clean the data in the previous csv file.
	(NB: make sure that the csv is in the same file as this .py file)

3. 	Open ft_graphs and run it to produce the frequency tables, graphs and charts
	(viewable on Spyder plot view)

Install dependencies if needed:

```bash
pip install pandas matplotlib
```

## 📌 Key Insights

* Students aged 25–35 are most common in both datasets.

* There's a positive correlation between study hours and exam marks.

* A slight negative correlation exists between time taken on the exam and the final score.

* Older students generally study more, suggesting experience or discipline.

* Dataset comparison helps verify consistency of trends across different student samples.

detailed anaylsis: [Data Analysis](docs/data-analysis.md) 

## 👤 Author
Daniel Mulligan
Python for Data Science – Exam Analysis Project
October 2024
