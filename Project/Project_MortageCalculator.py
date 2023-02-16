from tkinter import *

root = Tk()
root.title('Mortgage Calculator')
root.geometry("800x800")

def payment():
	if amount_entry.get() and interest_entry.get() and term_entry.get():
		# Convert Entry Boxes to numbers
		years = int(term_entry.get())
		months = years * 12
		rate = float(interest_entry.get())
		loan = int(amount_entry.get())
		# Calculate The Loan
		# Monthly Interest Rate
		monthly_rate = rate / 100 / 12 
		# Get Our Payment
		payment = (monthly_rate / (1 - (1 + monthly_rate)**(-months))) * loan
		# Format Payment
		payment = f"{payment:,.2f}"

		# Output Payment to the screen
		payment_label.config(text=f"Monthly Payment is: ${payment}")

	else:
		payment_label.config(text="Something is Wrong! (Invalid)")


my_label_frame = LabelFrame(root, text="\tNeja's Mortgage Calculator", bg = "#9AD1F0", font=("Arial Black", 20))
my_label_frame.pack(pady=80)

my_frame = Frame(my_label_frame, border=3)
my_frame.pack(pady=100, padx=50)

# Define Labels and Entry Boxes

amount_label = Label(my_frame, text="Loan Amount", font=("Arial Black", 25))
amount_entry = Entry(my_frame, font=("Arial", 20))

interest_label = Label(my_frame, text="Interest Rate", font=("Arial Black", 25))
interest_entry = Entry(my_frame, font=("Arial", 20))

term_label = Label(my_frame, text="Term in years", font=("Arial Black", 25))
term_entry = Entry(my_frame, font=("Arial", 20))

# Put Labels and Entry Boxes on the Screen
amount_label.grid(row=0, column=0)
amount_entry.grid(row=0, column=1)

interest_label.grid(row=1, column=0)
interest_entry.grid(row=1, column=1, pady=20)

term_label.grid(row=2, column=0)
term_entry.grid(row=2, column=1)

# Button
my_button = Button(my_label_frame, text="Calculate Payment", command=payment, font=("Arial Black", 18))
my_button.pack(pady=20)

# Output Label
payment_label = Label(root, text="", font=("Arial Black", 25))
payment_label.pack(pady=20)

root.mainloop()