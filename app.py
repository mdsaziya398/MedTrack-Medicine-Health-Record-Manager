import streamlit as st
import pandas as pd
from datetime import datetime, date

from medicine_manager import MedicineManager
from health_manager import HealthManager
from appointment_manager import AppointmentManager
from reminder_manager import ReminderManager


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="MedTrack",
    page_icon="💊",
    layout="wide"
)


# ==========================================
# MANAGERS
# ==========================================

medicine_manager = MedicineManager()
health_manager = HealthManager()
appointment_manager = AppointmentManager()

reminder_manager = ReminderManager(
    medicine_manager
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 0;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }

    .card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        background-color: #fafafa;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("💊 MedTrack")

st.sidebar.caption(
    "Medicine Reminder & Health Record Manager"
)

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Dashboard",
        "💊 Medicines",
        "➕ Add Medicine",
        "⏰ Reminders",
        "🏥 Health Records",
        "📅 Appointments",
        "📊 Reports"
    ]
)


# ==========================================
# DASHBOARD
# ==========================================

if page == "🏠 Dashboard":

    st.markdown(
        '<p class="main-title">MedTrack 💊</p>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle">'
        'Medicine Reminder & Health Record Manager'
        '</p>',
        unsafe_allow_html=True
    )

    total_medicines = len(
        medicine_manager.medicines
    )

    taken = sum(
        1
        for medicine in medicine_manager.medicines
        if medicine.get("status") == "Taken"
    )

    missed = sum(
        1
        for medicine in medicine_manager.medicines
        if medicine.get("status") == "Missed"
    )

    pending = sum(
        1
        for medicine in medicine_manager.medicines
        if medicine.get("status") == "Pending"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💊 Total Medicines",
            total_medicines
        )

    with col2:
        st.metric(
            "✅ Taken",
            taken
        )

    with col3:
        st.metric(
            "❌ Missed",
            missed
        )

    with col4:
        st.metric(
            "⏳ Pending",
            pending
        )

    st.divider()

    st.subheader("📅 Today's Medicine Schedule")

    if medicine_manager.medicines:

        df = pd.DataFrame(
            medicine_manager.medicines
        )

        st.dataframe(
            df[
                [
                    "id",
                    "name",
                    "dosage",
                    "time",
                    "duration",
                    "status"
                ]
            ],
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "No medicines added yet."
        )


# ==========================================
# MEDICINES
# ==========================================

elif page == "💊 Medicines":

    st.title("💊 Medicine Management")

    if medicine_manager.medicines:

        df = pd.DataFrame(
            medicine_manager.medicines
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        st.subheader("Update Medicine Status")

        medicine_ids = [
            medicine["id"]
            for medicine in medicine_manager.medicines
        ]

        selected_id = st.selectbox(
            "Select Medicine ID",
            medicine_ids
        )

        status = st.selectbox(
            "Status",
            [
                "Taken",
                "Missed",
                "Skipped",
                "Pending"
            ]
        )

        if st.button(
            "Update Status",
            type="primary"
        ):

            success = (
                medicine_manager.update_status(
                    selected_id,
                    status
                )
            )

            if success:

                st.success(
                    "Medicine status updated!"
                )

                st.rerun()

    else:

        st.info(
            "No medicines available."
        )


# ==========================================
# ADD MEDICINE
# ==========================================

elif page == "➕ Add Medicine":

    st.title("➕ Add Medicine")

    with st.form("medicine_form"):

        name = st.text_input(
            "Medicine Name"
        )

        dosage = st.text_input(
            "Dosage",
            placeholder="Example: 500 mg"
        )

        medicine_time = st.time_input(
            "Reminder Time"
        )

        duration = st.number_input(
            "Duration (days)",
            min_value=1,
            max_value=365,
            value=1
        )

        notes = st.text_area(
            "Notes",
            placeholder="Example: After food"
        )

        submitted = st.form_submit_button(
            "💾 Add Medicine"
        )

        if submitted:

            if not name.strip():

                st.error(
                    "Medicine name is required."
                )

            elif not dosage.strip():

                st.error(
                    "Dosage is required."
                )

            else:

                medicine_manager.add_medicine(
                    name.strip(),
                    dosage.strip(),
                    medicine_time.strftime("%H:%M"),
                    duration,
                    notes.strip()
                )

                st.success(
                    "✅ Medicine added successfully!"
                )


# ==========================================
# REMINDERS
# ==========================================

elif page == "⏰ Reminders":

    st.title("⏰ Medicine Reminders")

    current_time = datetime.now().strftime(
        "%H:%M"
    )

    st.info(
        f"Current time: {current_time}"
    )

    reminders = (
        reminder_manager
        .get_current_reminders()
    )

    if reminders:

        for medicine in reminders:

            st.warning(
                f"🔔 Reminder: "
                f"{medicine['name']} "
                f"({medicine['dosage']}) "
                f"is scheduled now."
            )

    else:

        st.success(
            "No medicine is scheduled for the current time."
        )

    st.subheader(
        "Today's Schedule"
    )

    if medicine_manager.medicines:

        sorted_medicines = sorted(
            medicine_manager.medicines,
            key=lambda x: x["time"]
        )

        for medicine in sorted_medicines:

            st.write(
                f"🕐 {medicine['time']} — "
                f"**{medicine['name']}** — "
                f"{medicine['dosage']}"
            )


# ==========================================
# HEALTH RECORDS
# ==========================================

elif page == "🏥 Health Records":

    st.title("🏥 Health Records")

    existing = health_manager.get_record()

    with st.form("health_form"):

        allergies = st.text_area(
            "Allergies",
            value=(
                existing.get("allergies", "")
                if existing else ""
            )
        )

        history = st.text_area(
            "Medical History",
            value=(
                existing.get(
                    "medical_history",
                    ""
                )
                if existing else ""
            )
        )

        blood_group = st.selectbox(
            "Blood Group",
            [
                "Not specified",
                "A+",
                "A-",
                "B+",
                "B-",
                "AB+",
                "AB-",
                "O+",
                "O-"
            ]
        )

        notes = st.text_area(
            "Additional Notes",
            value=(
                existing.get("notes", "")
                if existing else ""
            )
        )

        submitted = st.form_submit_button(
            "💾 Save Health Record"
        )

        if submitted:

            health_manager.save_record(
                allergies,
                history,
                blood_group,
                notes
            )

            st.success(
                "✅ Health record saved successfully!"
            )

    st.info(
        "MedTrack stores health information "
        "entered by the user. It does not "
        "provide diagnosis or treatment advice."
    )


# ==========================================
# APPOINTMENTS
# ==========================================

elif page == "📅 Appointments":

    st.title("📅 Appointments")

    tab1, tab2 = st.tabs(
        [
            "➕ Add Appointment",
            "📋 View Appointments"
        ]
    )

    with tab1:

        with st.form("appointment_form"):

            doctor = st.text_input(
                "Doctor Name"
            )

            appointment_date = st.date_input(
                "Appointment Date",
                min_value=date.today()
            )

            appointment_time = st.time_input(
                "Appointment Time"
            )

            purpose = st.text_input(
                "Purpose"
            )

            notes = st.text_area(
                "Notes"
            )

            submitted = st.form_submit_button(
                "💾 Add Appointment"
            )

            if submitted:

                if not doctor.strip():

                    st.error(
                        "Doctor name is required."
                    )

                elif not purpose.strip():

                    st.error(
                        "Purpose is required."
                    )

                else:

                    appointment_manager.add_appointment(
                        doctor.strip(),
                        appointment_date.isoformat(),
                        appointment_time.strftime(
                            "%H:%M"
                        ),
                        purpose.strip(),
                        notes.strip()
                    )

                    st.success(
                        "Appointment added successfully!"
                    )

    with tab2:

        if appointment_manager.appointments:

            df = pd.DataFrame(
                appointment_manager.appointments
            )

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

            st.subheader(
                "Delete Appointment"
            )

            appointment_ids = [
                appointment["id"]
                for appointment
                in appointment_manager.appointments
            ]

            selected_id = st.selectbox(
                "Appointment ID",
                appointment_ids
            )

            if st.button(
                "🗑️ Delete Appointment"
            ):

                if appointment_manager.delete_appointment(
                    selected_id
                ):

                    st.success(
                        "Appointment deleted."
                    )

                    st.rerun()

        else:

            st.info(
                "No appointments available."
            )


# ==========================================
# REPORTS
# ==========================================

elif page == "📊 Reports":

    st.title("📊 Medicine Reports")

    medicines = medicine_manager.medicines

    if medicines:

        df = pd.DataFrame(medicines)

        total = len(df)

        taken = len(
            df[df["status"] == "Taken"]
        )

        missed = len(
            df[df["status"] == "Missed"]
        )

        pending = len(
            df[df["status"] == "Pending"]
        )

        skipped = len(
            df[df["status"] == "Skipped"]
        )

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total",
            total
        )

        col2.metric(
            "Taken",
            taken
        )

        col3.metric(
            "Missed",
            missed
        )

        col4.metric(
            "Pending",
            pending
        )

        st.subheader(
            "Medicine Status Analysis"
        )

        status_counts = (
            df["status"]
            .value_counts()
        )

        st.bar_chart(
            status_counts
        )

        st.subheader(
            "Medicine Records"
        )

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.info(
            "Add medicines to generate reports."
        )