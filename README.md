# Hospital Data Analysis Project

## Overview
This project involves analyzing a hospital dataset to derive key insights related to patient care, costs, vital signs, and discharge status. Various visualizations were created using Python libraries such as **Pandas**, **Matplotlib**, and **Seaborn** to uncover trends and patterns within the data. The project also includes saving the visualized data to CSV files and the plots as PNG images for further use.

## Prerequisites

- **Python 3.x**: Ensure Python is installed.
- **Libraries**:
  - Pandas
  - Matplotlib
  - Seaborn

You can install the required libraries using `pip`:

```bash
pip install pandas matplotlib seaborn


Dataset
The dataset used in this project is named hospital_data.csv, which contains various columns including patient demographics, diagnosis information, treatment costs, and vital signs. The main columns include:

Diagnosis_Description: The diagnosis given to the patient.
Length_of_Stay: The number of days the patient stayed in the hospital.
Payment_Method: Method of payment for treatment.
Total_Cost: Total cost incurred by the patient for treatment.
Age: Age of the patient.
Vital_Signs_Temperature: Body temperature of the patient.
Vital_Signs_Heart_Rate: Heart rate of the patient.
Vital_Signs_BP: Blood pressure of the patient.
Vital_Signs_Oxygen: Oxygen saturation level of the patient.
Discharge_Status: The status of the patient upon discharge (e.g., Discharged, Transferred, Deceased).


Key Analyses & Visualizations
1. Average Length of Stay by Diagnosis
This analysis calculates the average length of stay for each diagnosis. A bar plot visualizes the results.

CSV file: avg_stay_by_diagnosis.csv
PNG file: avg_stay_by_diagnosis.png
2. Distribution of Total Costs by Payment Method
This analysis visualizes the distribution of total costs across different payment methods using a boxplot.

PNG file: total_cost_by_payment_method.png
3. Relationship Between Age and Total Cost
A scatter plot is used to visualize the relationship between the age of the patient and the total treatment cost.

PNG file: age_vs_total_cost.png
4. Average Vital Signs by Diagnosis
This analysis computes the average of the vital signs for each diagnosis. The results are displayed in a bar plot.

CSV file: avg_vital_signs_by_diagnosis.csv
PNG file: avg_vital_signs_by_diagnosis.png
5. Percentage of Patients Discharged by Status
A pie chart is used to show the percentage of patients discharged, transferred, or deceased based on discharge status.

CSV file: discharge_status_percentage.csv
PNG file: patient_discharge_status_percentage.png
Code Details
The Python script performs the following steps:

Load Dataset: The dataset hospital_data.csv is loaded using Pandas.
Data Preprocessing: Missing or invalid values in the columns Length_of_Stay and vital signs are handled by converting them to numeric values, with errors coerced into NaN.


Analysis and Visualization:
The average length of stay by diagnosis is calculated and visualized as a bar chart.
The distribution of total costs by payment method is visualized using a boxplot.
A scatter plot shows the relationship between age and total cost.
The average vital signs by diagnosis are visualized in a bar chart.
The percentage of discharge statuses is visualized in a pie chart.
Save Results: After each analysis, results are saved as CSV files, and the corresponding visualizations are saved as PNG files for easy access.

Files
CSV Files:

avg_stay_by_diagnosis.csv: Average length of stay by diagnosis.
avg_vital_signs_by_diagnosis.csv: Average vital signs by diagnosis.
discharge_status_percentage.csv: Percentage of patients discharged by status.
PNG Files:

avg_stay_by_diagnosis.png: Bar chart showing the average length of stay by diagnosis.
total_cost_by_payment_method.png: Boxplot showing the distribution of total costs by payment method.
age_vs_total_cost.png: Scatter plot showing the relationship between age and total cost.
avg_vital_signs_by_diagnosis.png: Bar chart showing the average vital signs by diagnosis.
patient_discharge_status_percentage.png: Pie chart showing the percentage of patient discharge statuses.


How to Run
Clone the repository or download the script and the dataset.
Make sure that you have all the necessary dependencies installed.


Run the script:
python app.py


This will execute the analysis, generate visualizations, and save both the visualizations and processed data as CSV/PNG files in your project directory.

Conclusion
This project demonstrates the application of data analysis and visualization techniques to gain insights from hospital data. By using Pandas for data manipulation, Matplotlib and Seaborn for visualization, and exporting results as CSV and PNG files, the project provides an effective way to communicate important healthcare insights.
