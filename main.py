import tkinter as tk
from tkinter import ttk

import numpy
import pandas as pd
data = pd.read_csv('comp.csv')
dataT = []
import re
#country,country_code,date_added,has_expired,job_board,job_description,job_title,job_type,location,organization,page_url,salary,sector,uniq_id
def count_IN(text):
    pattern = r'\bIN\b'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return len(matches)




def checkForWordMatch(str1, str2):
    words1 = str1.split()
    words2 = str2.split()
    
    for word1 in words1:
        for word2 in words2:
            if word1 == word2:
                return True
    return False
def extractMoneyAmounts(text):
    # Regular expression pattern to match currency amounts
    pattern = r'\b(?:\d{1,3}(?:,\d{3})*(?:\.\d+)?|\d+(?:,\d{3})*(?:\.\d+)?)\s*(?:USD|USDollars|dollars|USDollar|USDoll|USDs|US|US\$|US dollar|U.S. dollar|US Dollar|US\$|dollar|dollars|bucks|USD|U.S. dollars|US dollars|US dollar|Dollar|Dollars|Buck|Bucks|US|U\.S\.D\.|USDs|U\.S\.Dollars|U\.S\.Dollar|U\.S\.Doll|U\.S\.D|U\.S\.|US\$|U\.S\$)?\b'
    
    # Find all matches in the text
    matches = re.findall(pattern, text)
    
    # Convert matches to floats and remove dollar signs
    money_amounts = []
    for match in matches:
        # Remove non-digit characters and convert to float
        amount = float(re.sub(r'[^\d.]', '', match))
        money_amounts.append(amount)
    
    # Return the money amounts as floats
    return money_amounts

def Sift(state, city, zipcode, salaryminyear, salarymaxyear,salaryminhour, salarymaxhour, jobTitle,jobType):
    for index, row in data.iterrows():
        good = True
        percent = 0
        if state:
            if state in row['location'] and len(row['location']) < 45: #the 45 character limit prevents long descriptions being included with the locations
                good = True
            else: 
                good = False
        if city:
            if city in row['location'] and len(row['location']) < 45:
                good = True
            else:
                good = False
        if zipcode:
            if zipcode in row['location'] and len(row['location']) < 45:
                good = True
            else: 
                good = False
        if salaryminyear and salarymaxyear:
            if zipcode in row['salary'] and len(row['salary']) < 45:
                if "year" or "Year" or "YEAR" in row['salary']:
                    x = extractMoneyAmounts(row['salary'])
                    x= max(x)
                    if x >= salaryminyear and x <= salarymaxyear:
                        good = True
                    elif salaryminyear:
                        good = True
                    else:
                        good = False
                if "hour" or "Hour" or "HOUR" in row['salary']:
                    x = extractMoneyAmounts(row['salary'])
                    x= max(x)
                    if x >= salaryminhour and x <= salarymaxhour:
                        good = True
                    elif salaryminhour:
                        good = True
                    else: 
                        good = False
                if jobTitle:
                    if checkForWordMatch(row['job_title'], jobTitle):
                        good = True
                    else: 
                        good = False
                if jobType:
                    if checkForWordMatch(row['job_type'], jobType):
                        good = True
                    else: 
                        good = False
        if good:
            dataT.append("\n" + str(row['job_title']) + ' ' + str(row['job_type']) + ' ' + str(row['salary']) + ' ' + str(row['location'] + ' ' + str(row['page_url'])) + "\n")
    for x in dataT:
        update_text(x)     



def submit_function():
    # Get values from input fields
    input1_value = input1.get()
    input2_value = input2.get()
    input3_value = input3.get()
    input4_value = input4.get()
    input5_value = input5.get()
    input6_value = input6.get()
    input7_value = input7.get()
    input8_value = input8.get()
    input9_value = input9.get()
    # Call your actual Python function with the input values
    # Replace this with your actual function call
    restart_text(text_box)
    Sift(input1.get(),input2.get(),input3.get(),input4.get(),input5.get(),input6.get(),input7.get(),input8.get(),input9.get())
    
    
#state, city, zipcode, salaryminyear, salarymaxyear,salaryminhour, salarymaxhour, jobTitle,jobType
# Create main application window
root = tk.Tk()
root.title("JobQuest LP")

# Create style
style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")  # Set background color
style.configure("TLabel", background="#f0f0f0")  # Set background color for labels

# Create frame
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

# Create input fields
input1_label = ttk.Label(frame, text="State (EX: CA):")
input1_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
input1 = ttk.Entry(frame)
input1.grid(row=0, column=1, padx=5, pady=5)

input2_label = ttk.Label(frame, text="City (EX: San Diego):")
input2_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
input2 = ttk.Entry(frame)
input2.grid(row=1, column=1, padx=5, pady=5)

input3_label = ttk.Label(frame, text="Zipcode (EX: 91932):")
input3_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
input3 = ttk.Entry(frame)
input3.grid(row=2, column=1, padx=5, pady=5)

input4_label = ttk.Label(frame, text="Minimum Salary (year):")
input4_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
input4 = ttk.Entry(frame)
input4.grid(row=3, column=1, padx=5, pady=5)

input5_label = ttk.Label(frame, text="Maximum Salary (year)")
input5_label.grid(row=4, column=0, padx=5, pady=5, sticky="e")
input5 = ttk.Entry(frame)
input5.grid(row=4, column=1, padx=5, pady=5)

input6_label = ttk.Label(frame, text="Minimum Salary (hour)")
input6_label.grid(row=5, column=0, padx=5, pady=5, sticky="e")
input6 = ttk.Entry(frame)
input6.grid(row=5, column=1, padx=5, pady=5)

input7_label = ttk.Label(frame, text="Maximum Salary (hour)")
input7_label.grid(row=6, column=0, padx=5, pady=5, sticky="e")
input7 = ttk.Entry(frame)
input7.grid(row=6, column=1, padx=5, pady=5)

input8_label = ttk.Label(frame, text="Job Title:")
input8_label.grid(row=7, column=0, padx=5, pady=5, sticky="e")
input8 = ttk.Entry(frame)
input8.grid(row=7, column=1, padx=5, pady=5)

input9_label = ttk.Label(frame, text="Job Type (part/full time): ")
input9_label.grid(row=8, column=0, padx=5, pady=5, sticky="e")
input9 = ttk.Entry(frame)
input9.grid(row=8, column=1, padx=5, pady=5)

# Create submit button
submit_button = ttk.Button(frame, text="Submit", command=submit_function)
submit_button.grid(row=10, column=0, columnspan=2, padx=5, pady=10)
# Create frame for text box
text_frame = ttk.Frame(root)
text_frame.grid(row=0, column=1, padx=10, pady=10)

# Create text box
text_box = tk.Text(text_frame, height=15, width=100)
text_box.grid(row=0, column=0, padx=5, pady=5)
scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_box.yview)
scrollbar.grid(row=0, column=1, sticky='ns')

# Link scrollbar to text box
text_box.config(yscrollcommand=scrollbar.set)
# Initialize text box with some text
initial_text = ""
text_box.insert(tk.END, initial_text)
text_box.config(state=tk.DISABLED)  # Disable editing


def update_text(new_text):
    text_box.config(state=tk.NORMAL)  # Enable editing
     # Clear existing text
    text_box.insert(tk.END, new_text) # Insert new text
    text_box.config(state=tk.DISABLED)  # Disable editing


def restart_text(new_text):
    text_box.config(state=tk.NORMAL)  # Enable editing
    text_box.delete('1.0', tk.END)  # Clear existing text
    
    text_box.config(state=tk.DISABLED)  # Disable editing
root.mainloop()

