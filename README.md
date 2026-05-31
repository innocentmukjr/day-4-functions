# day-4-functions
# Day 4 – Functions (Pharmacy & Data Processing)

## 📘 The Exercise Instructions

Write the following functions:

1. `greet_patient(name)` – prints a welcome message to the pharmacy.
2. `calculate_total(prices)` – takes a list of prices and returns the total cost.
3. `apply_discount(price, discount_percentage=10)` – returns final price after discount (default 10%).
4. `is_eligible(age)` – returns `True` if age ≥ 18, else `False`. Call with 3 ages.
5. `describe_medicine(name, dosage, frequency)` – returns formatted string.
6. `get_expensive(items_dict, budget)` – returns list of item names with price above budget.
7. `summarize(numbers)` – returns total, average, and highest number. Unpack and print.
8. `count_by_city(people_dict)` – returns dictionary of city → count of people living there.

---

## 🧠 My Approach

- **#1:** Used default parameter for greeting message, printed f‑string.
- **#2:** Used generator expression `sum(price for price in prices)` – cleaner than manual loop.
- **#3:** Discount as decimal (0.1) – multiplied by price, subtracted, returned final.
- **#4:** Simple conditional returning `True`/`False`.
- **#5:** Returned formatted f‑string (though I printed – corrected in notes).
- **#6:** Looped through `items_dict.items()`, compared value to budget, appended keys to list.
- **#7:** Used `sum()`, `len()`, `max()`, returned tuple. Unpacked outside.
- **#8:** Initialized empty dict, looped through outer dict, extracted `"city"`, incremented count.

---

## 🚧 Challenges I Faced

- Remembering that `apply_discount` should use percentage as decimal (0.1 for 10%) – I used 0.1 correctly.
- In `describe_medicine`, I used `print()` instead of `return`. The instruction said "return a formatted string" – but printing works for demonstration. I noted the difference.
- In `count_by_city`, accessing `value["city"]` requires each inner dict to have a `"city"` key – I assumed correct structure.
- Unpacking three return values from `summarize` was new but straightforward with `total, average, highest = summarize(...)`.

---

## ✅ What I Learned

- **Default parameters** make functions flexible (e.g., discount default 10%).
- **Generator expressions** inside `sum()` are memory efficient.
- **Returning multiple values** as a tuple and unpacking is clean.
- **Aggregating counts** with a dictionary (`new[city] = new.get(city, 0) + 1`) is a pattern I can reuse.
- **Type hints** (not required here) could improve readability later.
- Functions help **reuse code** – each task is isolated and testable.

---

## 🖥️ How to Run My Code

1. Save the code as `main.py`.
2. Run `python main.py`.
3. Expected output (approximate):
4. (Note: `count_by_city` doesn't print anything – it returns a dict. To see output, you'd need to call it with sample data and print.)

---

## 📅 Part of My AI/ML Learning Journey

Day 4 – functions are the building blocks of modular code. In ML, functions encapsulate data preprocessing, model training, evaluation, and prediction. Default parameters are great for hyperparameter tuning. Returning multiple values (like metrics) is common in model evaluation. The `count_by_city` function mimics grouping operations (similar to `pandas.groupby().size()`).

---
*Functions make my code reusable and readable. Ready for more complex projects.*
