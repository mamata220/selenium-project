from source.class_and_obj.robot_medandair import Robot


class AirRobot(Robot):
    def book_a_flight(self,flightname):
        print(f"Your booking has been made for flight: {flightname}")