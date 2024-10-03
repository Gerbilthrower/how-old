
    # Get user input for age
age = int(input("Enter your age in years: "))
days_alive = age * 365
decades_alive = age // 10
weeks_alive = age * 52
minutes_alive = age * 365 * 24 * 60
print(f"You have been alive for:")
print(f"{days_alive} days")
print(f"{decades_alive} decades")
print(f"{weeks_alive} weeks")
print(f"{minutes_alive} minutes")

