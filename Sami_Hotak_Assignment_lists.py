print("-------------------------------------")
print("----------Assignment on Lists--------")
print("--------------Sami Hotak-------------")
print("-------------------------------------")
temperatures = [25, 27, 26, 28, 30, 24, 29]  
# Step 1: Calculate total sum of temperatures
total_sum = sum(temperatures)

# Step 2: Calculate average temperature for the week
average_temperature = total_sum / len(temperatures)

# Step 3: Initialize variable to count number of days with temperatures above average
days_above_average = 0

# Step 4: Iterate through each temperature in the list
for temp in temperatures:
    # Step 5: Check if temperature is above the average
    if temp > average_temperature:
        # Step 6: Increment count of days above average
        days_above_average += 1

# Step 7: Print the average temperature for the week and the count of days above average
print(" The Average temperature for the week:", average_temperature)
print("Number of the days with temperatures above average:", days_above_average)