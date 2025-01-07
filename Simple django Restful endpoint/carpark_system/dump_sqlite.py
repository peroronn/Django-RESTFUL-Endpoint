import sqlite3

# Connect to the SQLite database
connection = sqlite3.connect("db.sqlite3")

# Open the output file
with open("output_file.txt", "w") as file:
    # Iterate through the database dump
    for line in connection.iterdump():
        file.write(f"{line}\n")

print("Database dump saved to output_file.txt")
