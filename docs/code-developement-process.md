# 🛠️ Code Development Process

## 📋 Initial Process and Planning

The development process began by drafting a basic script to generate realistic student exam data within defined parameter ranges.

### Step 1: Data Generation
- A script was written to create data points such as age, study hours, exam duration, and exam marks.
- The aim was to simulate realistic student behavior across 150 entries.

### Step 2: Data Cleaning
- A cleaning function was implemented to ensure the `.csv` file maintained 150 valid rows.
- Any duplicate, zero, or out-of-range values were replaced using logic that regenerated those values within the expected statistical boundaries.

### Step 3: Frequency Tables and Charts
- A dictionary-based approach was used to group data into frequency tables using `for` loops and defined bins.
- These tables became the basis for visual representations of the data.

### Step 4: Graph and Chart Creation
- **Bar Chart**: Created from age group frequency table.
- **Line Graph**: Correlated study hours with exam marks. This was the most challenging, as it required direct grouping from the `.csv` rather than pre-made frequency bins.
- **Scatter Plots**: Two scatter plots were created—one correlating exam duration with marks, and another comparing study time with student age.

---

## 🧪 Issues Discovered During Initial Runs

Several problems with the original random generation model were identified:

- **No Visual Frequency Table**: Added `matplotlib` to visualize frequency data.
- **Unbalanced Age Distribution**: The range (0–100) skewed too many students above 45. To fix this, a model inspired by Canadian tertiary statistics was implemented.
- **Inaccurate Correlations**:
  - Study time vs. marks showed a non-linear, unrealistic trend.
  - Exam duration vs. marks lacked the expected **negative correlation** (i.e., lower-performing students taking longer).
  - Age vs. study time showed randomness, despite research indicating older students tend to study more.

---

## 🔄 Final Code Adjustments

### ✅ CSV Generation
- Revised to produce more statistically accurate data using:
  - **Age-weighted study time**
  - **Study-time-weighted marks**
  - **Mark-weighted exam durations**

> These adjustments introduced realistic correlation patterns while still allowing natural variability and outliers.

### ✅ Cleaning Logic
- Updated to align with the new generation logic, ensuring replacements remained consistent with the statistical model.

### ✅ Frequency Table and Binning
- Minor binning corrections for study time (e.g., inclusion of students studying <1 hour).
- Created additional binning for percentage marks to improve readability and interpretation.

---

This structured process ensured that the final dataset:
- Mimicked real academic performance trends,
- Maintained data quality after cleaning,
- And provided meaningful insights through visualization.
