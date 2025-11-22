# 🧾 Python Bill Splitter

A lightweight, pure Python command-line tool designed to help groups track shared expenses, calculate taxes and tips, and determine exactly how much each person owes.

# 📖 Overview
This project is a CLI (Command Line Interface) utility built to solve a common real-world problem: splitting a restaurant bill or group expense. 

*Key Technical Constraint:** This project was built entirely using **standard Python libraries** only. No external modules (like Pandas or NumPy) were used, demonstrating core competency in logic, data structures, and string formatting.

# ✨ Features
* **Dynamic Item Entry:** Uses a `while` loop to accept an unlimited number of items until the user is finished.
* **Robust Error Handling:** Validates user input to ensure the program doesn't crash if non-numeric values are entered.
* **Automated Math:** Instantly calculates Subtotal, Tax (%), and Tip (%) to generate a Grand Total.
* **Professional Output:** Generates a formatted "Receipt" view using Python f-strings for alignment.
* **Fair Splitting:** Calculates the exact cost per person based on the group size.

# 🚀 How to Run

# Prerequisites
* You need **Python 3.x** installed on your machine.

# 💻 Example Usage
Here is what the program looks like in action:

```text
--- 🧾 BILL SPLITTER TOOL ---
Enter your items. Type 'done' as the name when finished.

Item Name (or 'done'): Large Pizza
Price for Large Pizza: 22.50
Item Name (or 'done'): Garlic Bread
Price for Garlic Bread: 8.00
Item Name (or 'done'): Pitcher of Soda
Price for Pitcher of Soda: 12
Item Name (or 'done'): done

--- Details ---
Enter Tax Rate % (e.g., 5 for 5%): 8
Enter Tip % (e.g., 15 for 15%): 18
How many people are splitting this?: 4

================================
        📄 FINAL RECEIPT        
================================
Large Pizza          $     22.50
Garlic Bread         $      8.00
Pitcher of Soda      $     12.00
--------------------------------
Subtotal:            $     42.50
Tax:                 $      3.40
Tip:                 $      7.65
================================
GRAND TOTAL:         $     53.55
================================

Each person owes: $13.39
