# car_rental.py

from datetime import datetime, timedelta

class CarRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"\n[INFO] We currently have {self.stock} car(s) available to rent.")
        return self.stock

    def rent_hourly(self, num_cars):
        if num_cars <= 0:
            print("[ERROR] Number of cars should be positive!")
            return None
        elif num_cars > self.stock:
            print("[ERROR] Not enough cars available!")
            return None
        else:
            now = datetime.now()
            print(f"[SUCCESS] Rented {num_cars} car(s) on hourly basis at {now.hour}:{now.minute}")
            self.stock -= num_cars
            return now

    def rent_daily(self, num_cars):
        if num_cars <= 0:
            print("[ERROR] Number of cars should be positive!")
            return None
        elif num_cars > self.stock:
            print("[ERROR] Not enough cars available!")
            return None
        else:
            now = datetime.now()
            print(f"[SUCCESS] Rented {num_cars} car(s) on daily basis at {now.date()}")
            self.stock -= num_cars
            return now

    def rent_weekly(self, num_cars):
        if num_cars <= 0:
            print("[ERROR] Number of cars should be positive!")
            return None
        elif num_cars > self.stock:
            print("[ERROR] Not enough cars available!")
            return None
        else:
            now = datetime.now()
            print(f"[SUCCESS] Rented {num_cars} car(s) on weekly basis.")
            self.stock -= num_cars
            return now

    def return_car(self, request):
        rental_time, rental_basis, num_cars = request
        bill = 0
        print (rental_basis)
        print (rental_time)
        print (num_cars)
        
        if rental_time and rental_basis and num_cars:
            self.stock += num_cars
            now = datetime.now() +  timedelta(hours=9)
            rental_period = now - rental_time
            print (rental_period)
            if rental_basis == 1:  # hourly
                bill = round(rental_period.total_seconds() / 3600) * 10 * num_cars
            elif rental_basis == 2:  # daily
                bill = round(rental_period.total_seconds() / (3600 * 24)) * 40 * num_cars
            elif rental_basis == 3:  # weekly
                bill = round(rental_period.total_seconds() / (3600 * 24 * 7)) * 200 * num_cars

            print(f"[INFO] Total bill: ${bill}")
            return bill
        else:
            print("[ERROR] There are no more cars to return!")
            return None


class Customer:
    def __init__(self):
        self.cars = 0
        self.rental_basis = 0
        self.rental_time = None

    def request_car(self):
        try:
            cars = int(input("How many cars would you like to rent? "))
            if cars <= 0:
                raise ValueError
        except ValueError:
            print("[ERROR] Invalid input. Please enter a positive number.")
            return -1
        self.cars = cars
        return self.cars

    def return_car(self):
        if self.rental_time and self.rental_basis and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return 0, 0, 0