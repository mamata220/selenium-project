from source.class_and_obj.robot_medandair import Robot


class MedicalRobot(Robot):
    def book_doc_apt(self, drname):
        drname.greet_user()
