import csv

# Function to convert height and weight to metric
def convert_to_metric(height, weight, units):
    if units == 'imperial':
        feet = height[0]
        inches = height[1]
        total_inches = feet * 12 + inches
        height_m = total_inches * 0.0254
        weight_kg = weight * 0.453592
    else:
        height_m = height / 100
        weight_kg = weight
    return height_m, weight_kg

# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Function to categorize BMI
def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

# Function to get one user's data
def get_user():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    unit = input("Choose units (metric/imperial): ").lower()

    if unit == "imperial":
        feet = int(input("Enter height - feet: "))
        inches = int(input("Enter height - inches: "))
        weight = float(input("Enter weight in lbs: "))
        height = (feet, inches)
    else:
        height = float(input("Enter height in cm: "))
        weight = float(input("Enter weight in kg: "))

    return name, age, height, weight, unit

# Function to show analytics
def show_analytics(all_users):
    total_users = len(all_users)
    if total_users == 0:
        print("No data available.")
        return

    bmi_list = [user["BMI"] for user in all_users]
    highest = max(bmi_list)
    lowest = min(bmi_list)
    average = round(sum(bmi_list) / total_users, 2)

    print("\n--- Analytics ---")
    print(f"Total users: {total_users}")
    print(f"Average BMI: {average}")
    print(f"Highest BMI: {highest}")
    print(f"Lowest BMI: {lowest}")

    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    for cat in categories:
        count = sum(1 for user in all_users if user["Category"] == cat)
        percent = (count / total_users) * 100
        print(f"{cat}: {count} users ({round(percent, 1)}%)")

# Function to save data to CSV
def save_to_csv(data, filename="data.csv"):
    keys = data[0].keys()
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
    print(f"\nData saved to {filename}")

# Main program
def main():
    users = []

    print("=== BMI Calculator ===")
    while True:
        name, age, height, weight, unit = get_user()
        height_m, weight_kg = convert_to_metric(height, weight, unit)
        bmi = calculate_bmi(weight_kg, height_m)
        category = get_category(bmi)

        print(f"{name}, your BMI is {bmi} ({category})")

        user_data = {
            "Name": name,
            "Age": age,
            "Height_m": round(height_m, 2),
            "Weight_kg": round(weight_kg, 2),
            "BMI": bmi,
            "Category": category
        }

        users.append(user_data)

        more = input("\nAdd another user? (y/n): ").lower()
        if more != 'y':
            break

    show_analytics(users)
    save_to_csv(users)

if __name__ == "__main__":
    main()
