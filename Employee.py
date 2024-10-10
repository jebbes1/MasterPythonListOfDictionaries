employees = [
    {"Employee name": "Juan Carlos", "Job Title": "Software Developer", "Employee ID": "EMP0123", "Age": 36, "Date of hire": "March 22, 2009"},
    {"Employee name": "Jose Rizal", "Job Title": "IT Support Specalist", "Employee ID": "EMP0234", "Age": 40, "Date of hire": "February 9, 2014"},
    {"Employee name": "Juan Luna", "Job Title": "Network Adminitrator", "Employee ID": "EMP0345", "Age": 37, "Date of hire": "October 10, 2016"},
    {"Employee name": "Andres Bonifacio", "Job Title": "Software Engineer", "Employee ID": "EMP0456", "Age": 38, "Date of hire": "December 10, 2010"},
    {"Employee name": "Justin Bieber", "Job Title": "Cyber Security Analyst", "Employee ID": "EMP0567", "Age": 40, "Date of hire": "June 20, 2008"},
]

for employee in employees:
    print(f"Employee name: {employee['Employee name']} | Job Title: {employee['Job Title']} | Employee ID: {employee['Employee ID']} | Age: {employee['Age']} | Date of hire: {employee['Date of hire']}")
