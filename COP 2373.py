"""
population_RF.py

Creates a population database, inserts Florida city data for 2025,
simulates 20 years of growth/decline, and visualizes results.

Author: Robyn Franklin
Date: 2026
"""

import sqlite3
import random
import matplotlib.pyplot as plt


# -------- FUNCTION 1: CREATE DATABASE AND TABLE --------
def create_database():
    conn = sqlite3.connect("population_YI.db")  # <-- CHANGE YOUR INITIALS
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER,
            PRIMARY KEY (city, year)
        )
    """)

    conn.commit()
    return conn, cursor


# -------- FUNCTION 2: INSERT INITIAL DATA --------
def insert_initial_data(cursor, conn):
    cities_data = {
        "Miami": 470000,
        "Orlando": 320000,
        "Tampa": 400000,
        "Jacksonville": 1000000,
        "Tallahassee": 200000,
        "Fort Lauderdale": 185000,
        "St. Petersburg": 260000,
        "Hialeah": 220000,
        "Cape Coral": 230000,
        "Gainesville": 145000
    }

    for city, population in cities_data.items():
        cursor.execute("""
            INSERT OR IGNORE INTO population (city, year, population)
            VALUES (?, ?, ?)
        """, (city, 2025, population))

    conn.commit()


# -------- FUNCTION 3: SIMULATE POPULATION --------
def simulate_population(cursor, conn):
    cursor.execute("SELECT city, population FROM population WHERE year = 2025")
    initial_data = cursor.fetchall()

    for city, population in initial_data:
        current_population = population

        for year in range(2026, 2046):  # 20 years
            growth_rate = random.uniform(-0.02, 0.05)  # -2% to +5%
            current_population = int(current_population * (1 + growth_rate))

            cursor.execute("""
                INSERT OR IGNORE INTO population (city, year, population)
                VALUES (?, ?, ?)
            """, (city, year, current_population))

    conn.commit()


# -------- FUNCTION 4: VISUALIZE DATA --------
def plot_population(cursor):
    cursor.execute("SELECT DISTINCT city FROM population ORDER BY city")
    cities = [row[0] for row in cursor.fetchall()]

    print("\nAvailable Cities:")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")

    try:
        choice = int(input("\nChoose a city (1-10): "))
        selected_city = cities[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Please run again.")
        return

    cursor.execute("""
        SELECT year, population 
        FROM population 
        WHERE city = ?
        ORDER BY year
    """, (selected_city,))

    data = cursor.fetchall()
    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    plt.figure(figsize=(8, 5))
    plt.plot(years, populations, marker='o')
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# -------- MAIN FUNCTION --------
def main():
    conn, cursor = create_database()

    insert_initial_data(cursor, conn)
    simulate_population(cursor, conn)
    plot_population(cursor)

    conn.close()


if __name__ == "__main__":
    main()