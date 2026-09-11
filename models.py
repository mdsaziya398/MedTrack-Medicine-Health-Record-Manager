from abc import ABC, abstractmethod


class Medicine:
    def __init__(
        self,
        medicine_id,
        name,
        dosage,
        time,
        duration,
        notes=""
    ):
        self.__medicine_id = medicine_id
        self.name = name
        self.dosage = dosage
        self.time = time
        self.duration = duration
        self.notes = notes
        self.status = "Pending"

    @property
    def medicine_id(self):
        return self.__medicine_id

    def to_dict(self):
        return {
            "id": self.__medicine_id,
            "name": self.name,
            "dosage": self.dosage,
            "time": self.time,
            "duration": self.duration,
            "notes": self.notes,
            "status": self.status
        }


class HealthRecord:
    def __init__(
        self,
        allergies="",
        medical_history="",
        blood_group="",
        notes=""
    ):
        self.allergies = allergies
        self.medical_history = medical_history
        self.blood_group = blood_group
        self.notes = notes

    def to_dict(self):
        return {
            "allergies": self.allergies,
            "medical_history": self.medical_history,
            "blood_group": self.blood_group,
            "notes": self.notes
        }


class Reminder(ABC):

    def __init__(self, time):
        self.time = time

    @abstractmethod
    def show_reminder(self):
        pass


class MedicineReminder(Reminder):

    def __init__(self, medicine_name, time):
        super().__init__(time)
        self.medicine_name = medicine_name

    def show_reminder(self):
        return (
            f"Medicine reminder: "
            f"{self.medicine_name} at {self.time}"
        )


class AppointmentReminder(Reminder):

    def __init__(self, doctor, date, time):
        super().__init__(time)
        self.doctor = doctor
        self.date = date

    def show_reminder(self):
        return (
            f"Appointment with {self.doctor} "
            f"on {self.date} at {self.time}"
        )


class Appointment:

    def __init__(
        self,
        appointment_id,
        doctor,
        date,
        time,
        purpose,
        notes=""
    ):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.date = date
        self.time = time
        self.purpose = purpose
        self.notes = notes

    def to_dict(self):
        return {
            "id": self.appointment_id,
            "doctor": self.doctor,
            "date": self.date,
            "time": self.time,
            "purpose": self.purpose,
            "notes": self.notes
        }