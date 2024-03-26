from datetime import datetime


class Airline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []

    def add_plane(self, plane):
        self.planes.append(plane)

    def __str__(self):
        return f"Airline: {self.name} (ID: {self.id})"

    def __repr__(self):
        return f"Airline('{self.id}', '{self.name}')"


class Airplane:
    def __init__(self, id, company):
        self.id = id
        self.current_location = None
        self.company = company
        self.next_flights = []

    def __str__(self):
        return f"Airplane ID: {self.id}, Location: {self.current_location.city}, Company: {self.company.name}"

    def __repr__(self):
        return f"Airplane({self.id}, {repr(self.current_location)}, {repr(self.company)})"

    def fly(self, destination):
        if self.next_flights:
            flight = self.next_flights.pop(0)
            flight.take_off()
            flight.land(destination)

    def location_on_date(self, date):
        for flight in self.next_flights:
            if flight.date == date:
                return flight.origin
        return self.current_location

    def available_on_date(self, date, location):
        if self.current_location != location:
            return False
        for flight in self.next_flights:
            if flight.date == date:
                return False
        return True


class Flight:
    def __init__(self, date, origin, destination, plane):
        self.date = date
        self.origin = origin
        self.destination = destination
        self.plane = plane
        self.id = f"{destination}-{plane.company.id}-{date.strftime('%Y%m%d')}"

    def __str__(self):
        return f"Flight ID: {self.id}, Date: {self.date}, From: {self.origin.city} To: {self.destination.city}"

    def __repr__(self):
        return f"Flight({self.date}, {repr(self.destination)}, {repr(self.origin)}, {repr(self.plane)}, '{self.id}')"

    def take_off(self):
        self.plane.current_location = self.origin
        self.origin.planes.remove(self.plane)

    def land(self, destination):
        self.plane.current_location = destination
        destination.planes.append(self.plane)


class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []

    def schedule_flight(self, destination, datetime):
        for plane in self.planes:
            if plane.available_on_date(datetime.date(), self):
                flight = Flight(datetime.date(), self, destination, plane)
                plane.next_flights.append(flight)
                self.scheduled_departures.append(flight)
                destination.scheduled_arrivals.append(flight)
                return
        print("No available airplanes for this flight.")

    def __str__(self):
        return f"Airport: {self.city}, Planes: {len(self.planes)}, Departures: {len(self.scheduled_departures)}, Arrivals: {len(self.scheduled_arrivals)}"

    def __repr__(self):
        return f"Airport('{self.city}')"

    def info(self, start_date, end_date):
        print(f"Scheduled flights from {self.city} airport:")
        for flight in self.scheduled_departures + self.scheduled_arrivals:
            if start_date.date() <= flight.date <= end_date.date():
                print(f"Flight ID: {flight.id}, Date: {flight.date}, Origin: {flight.origin.city}, "
                      f"Destination: {flight.destination.city}, Airline: {flight.plane.company.name}")


airport_svo = Airport("SVO")
airport_jfk = Airport("JFK")

airline_dl = Airline("DL", "Delta Airlines")


plane_1 = Airplane(101, airline_dl)
plane_2 = Airplane(102, airline_dl)


airline_dl.planes.append(plane_1)
airline_dl.planes.append(plane_2)


airport_svo.planes.append(plane_1)
airport_svo.planes.append(plane_2)
plane_1.current_location = airport_svo
plane_2.current_location = airport_svo


flight_date = datetime(2024, 4, 1, 10, 0)  # 1 апреля 2024 года, 10:00
airport_svo.schedule_flight(airport_jfk, flight_date)

airport_svo.info(datetime(2024, 3, 31), datetime(2024, 4, 2))

