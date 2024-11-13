import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the dataset
data = pd.read_csv('hospital_data.csv')

# Check data types and inspect the 'Length_of_Stay' column
print(data.dtypes)
print(data['Length_of_Stay'].unique())  # Check unique values in Length_of_Stay

# Convert 'Length_of_Stay' to numeric, invalid values will become NaN
data['Length_of_Stay'] = pd.to_numeric(data['Length_of_Stay'], errors='coerce')

# Check if there are any NaN values after conversion
print(data['Length_of_Stay'].isna().sum())

# 1. Average length of stay by diagnosis
avg_stay_by_diagnosis = data.groupby('Diagnosis_Description')['Length_of_Stay'].mean()
avg_stay_by_diagnosis.plot(kind='bar', color='skyblue')
plt.title('Average Length of Stay by Diagnosis')
plt.xlabel('Diagnosis')
plt.ylabel('Average Length of Stay (days)')
plt.show()

# 2. Distribution of total costs by payment method
sns.boxplot(x='Payment_Method', y='Total_Cost', data=data)
plt.title('Total Cost Distribution by Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Total Cost ($)')
plt.show()

# 3. Relationship between age and total cost
plt.scatter(data['Age'], data['Total_Cost'], alpha=0.6)
plt.title('Age vs Total Cost of Treatment')
plt.xlabel('Age')
plt.ylabel('Total Cost ($)')
plt.show()

# 4. Average vital signs across diagnoses
# Ensure that vital signs are numeric
data[['Vital_Signs_Temperature', 'Vital_Signs_Heart_Rate', 'Vital_Signs_BP', 'Vital_Signs_Oxygen']] = \
    data[['Vital_Signs_Temperature', 'Vital_Signs_Heart_Rate', 'Vital_Signs_BP', 'Vital_Signs_Oxygen']].apply(pd.to_numeric, errors='coerce')

vital_signs_avg = data.groupby('Diagnosis_Description')[['Vital_Signs_Temperature', 'Vital_Signs_Heart_Rate', 'Vital_Signs_BP', 'Vital_Signs_Oxygen']].mean()
vital_signs_avg.plot(kind='bar', figsize=(10,6))
plt.title('Average Vital Signs by Diagnosis')
plt.xlabel('Diagnosis')
plt.ylabel('Average Vital Signs')
plt.xticks(rotation=45)
plt.show()

# 5. Percentage of patients discharged by status
discharge_status_percentage = data['Discharge_Status'].value_counts(normalize=True) * 100
discharge_status_percentage.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue', 'purple', 'yellow'])
plt.title('Patient Discharge Status Percentage')
plt.ylabel('')
plt.show()
