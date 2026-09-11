from medicine_manager import MedicineManager
from health_manager import HealthManager
from appointment_manager import AppointmentManager
from reminder_manager import ReminderManager


def display_banner():

    print("\n")
    print("=" * 55)
    print("        💊 MEDTRACK")
    print("   Medicine Reminder & Health Manager")
    print("=" * 55)


def display_menu():

    print("\n========== MAIN MENU ==========")

    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Search Medicine")
    print("4. Update Medicine")
    print("5. Delete Medicine")
    print("6. Update Medicine Status")
    print("7. Medicine Summary")
    print("8. View Medicine Schedule")
    print("9. Check Current Reminders")
    print("10. Add/Update Health Record")
    print("11. View Health Record")
    print("12. Add Appointment")
    print("13. View Appointments")
    print("14. Delete Appointment")
    print("15. Exit")


def main():

    medicine_manager = MedicineManager()
    health_manager = HealthManager()
    appointment_manager = AppointmentManager()

    reminder_manager = ReminderManager(
        medicine_manager
    )

    display_banner()

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":
            medicine_manager.add_medicine()

        elif choice == "2":
            medicine_manager.view_medicines()

        elif choice == "3":
            medicine_manager.search_medicine()

        elif choice == "4":
            medicine_manager.update_medicine()

        elif choice == "5":
            medicine_manager.delete_medicine()

        elif choice == "6":
            medicine_manager.update_status()

        elif choice == "7":
            medicine_manager.summary()

        elif choice == "8":
            reminder_manager.show_all_reminders()

        elif choice == "9":
            reminder_manager.check_reminders()

        elif choice == "10":
            health_manager.add_or_update_record()

        elif choice == "11":
            health_manager.view_record()

        elif choice == "12":
            appointment_manager.add_appointment()

        elif choice == "13":
            appointment_manager.view_appointments()

        elif choice == "14":
            appointment_manager.delete_appointment()

        elif choice == "15":

            print("\nThank you for using MedTrack!")
            print("Stay organized and take care. 💊")
            break

        else:
            print("\n❌ Invalid choice. Please select 1-15.")


if __name__ == "__main__":
    main()