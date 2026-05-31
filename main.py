# ================================================
# DAY 4 EXERCISES - FUNCTIONS 
# ================================================

# 1. Greet patient
def greet_patient(name, greeting="Welcome to MIJ General Clinic, Where Health Starts..."):
    """Print a welcome message."""
    print(f"{name}, {greeting}")

# 2. Calculate total from list of prices
def calculate_total(prices):
    """Return sum of all prices."""
    return sum(prices)  # simpler than generator expression

# 3. Apply discount (default 10%)
def apply_discount(price, discount_percentage=0.1):
    """Return price after discount (discount as decimal, e.g., 0.1 = 10%)."""
    return price - (price * discount_percentage)

# 4. Check age eligibility (18+)
def is_eligible(age):
    """Return True if age >= 18, else False."""
    return age >= 18  # direct boolean expression

# 5. Describe medicine (returns formatted string)
def describe_medicine(name, dosage, frequency):
    """Return formatted medicine string."""
    return f"Medicine: {name} | Dosage: {dosage} | Frequency: {frequency}"

# 6. Get items above budget
def get_expensive(items_dict, budget=200):
    """Return list of item names with price > budget."""
    return [item for item, price in items_dict.items() if price > budget]  # list comprehension

# 7. Summarize numbers: total, average, highest
def summarize(numbers):
    """Return tuple (total, average, highest)."""
    if not numbers:
        return 0, 0, None
    total = sum(numbers)
    average = total / len(numbers)
    highest = max(numbers)
    return total, average, highest

# 8. Count people by city
def count_by_city(people_dict):
    """Return dict with city names as keys and count of people as values.
       Expected structure: {'person1': {'city': 'Kampala'}, ...}
    """
    city_count = {}
    for person, info in people_dict.items():
        city = info.get("city")  # safer than direct access
        if city:
            city_count[city] = city_count.get(city, 0) + 1
    return city_count


# ================================================
# DEMONSTRATIONS (call each function)
# ================================================

if __name__ == "__main__":
    # 1
    greet_patient("Innocent")

    # 2
    total_cost = calculate_total([900, 600, 500])
    print(f"Total cost: {total_cost}")

    # 3
    final = apply_discount(11000)  # default 10% discount
    print(f"Price after 10% discount: {final}")

    # 4
    for age in [16, 18, 70]:
        print(f"Age {age}: eligible = {is_eligible(age)}")

    # 5
    med_info = describe_medicine("Paracetamol", "500mg", "Twice daily")
    print(med_info)

    # 6
    items = {"tomatoes": 500, "onions": 300, "garlic": 200}
    expensive_items = get_expensive(items, budget=200)
    print(f"Items above budget: {expensive_items}")

    # 7
    nums = [40, 50, 20, 54, 23]
    total, avg, highest = summarize(nums)
    print(f"Total: {total}, Average: {avg:.2f}, Highest: {highest}")

    # 8
    people = {
        "patient1": {"name": "John", "city": "Kampala"},
        "patient2": {"name": "Mary", "city": "Wakiso"},
        "patient3": {"name": "Sam", "city": "Kampala"},
        "patient4": {"name": "Inno", "city": "Masaka"}
    }
    city_counts = count_by_city(people)
    print(f"City counts: {city_counts}")
