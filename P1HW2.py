# Eric Corbett
# 9/29/2024
# P1HW2



#1. Start
#2. Ask user for budget
#3. Ask user for Location
#4. Ask user for fuel expenses
#5. Ask user for accommodation expenses
#6. Ask user for food expenses
#7. Calculate total expenses 
#8. Calculate remaining budget 
#9. Display Location, total expenses, and remaining budget
#10. End

budget = float(input("Enter your budget: "))  
Location = input("Enter your travel Location: ")  
fuel_expense = float(input("Enter amount you will spend on fuel: "))  
accommodation_expense = float(input("Enter amount you will spend on accommodation: "))  
food_expense = float(input("Enter amount you will spend on food: "))  


total_expenses = fuel_expense + accommodation_expense + food_expense


remaining_budget = budget - total_expenses

print(f"{'Location:':<25} {Location}")
print(f"{'budget:':<25} ${budget:.2f}")
print(f"{'fuel:':<25} {fuel_expense}")
print(f"{'accommodation:':<25} {accommodation_expense}")
print(f"{'Remaining Budget:':<25} ${remaining_budget:.2f}")
