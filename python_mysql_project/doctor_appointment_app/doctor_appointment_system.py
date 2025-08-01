import streamlit as st
import mysql.connector
from datetime import datetime, timedelta
import pandas as pd
import hashlib

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',  # Add your MySQL password here
    'database': 'doctor_appointment_db'
}

# Initialize database connection
def init_db():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Create tables if they don't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                phone VARCHAR(15) NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                specialization VARCHAR(100) NOT NULL,
                email VARCHAR(100) UNIQUE NOT NULL,
                phone VARCHAR(15) NOT NULL,
                experience_years INT NOT NULL,
                consultation_fee DECIMAL(10,2) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                patient_id INT NOT NULL,
                doctor_id INT NOT NULL,
                appointment_date DATE NOT NULL,
                appointment_time TIME NOT NULL,
                status ENUM('scheduled', 'completed', 'cancelled') DEFAULT 'scheduled',
                symptoms TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (patient_id) REFERENCES patients(id),
                FOREIGN KEY (doctor_id) REFERENCES doctors(id)
            )
        """)
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Database connection error: {e}")
        return False

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Patient registration
def register_patient(name, email, phone, password):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        password_hash = hash_password(password)
        cursor.execute("""
            INSERT INTO patients (name, email, phone, password_hash)
            VALUES (%s, %s, %s, %s)
        """, (name, email, phone, password_hash))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Registration error: {e}")
        return False

# Patient login
def patient_login(email, password):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        password_hash = hash_password(password)
        cursor.execute("""
            SELECT id, name FROM patients 
            WHERE email = %s AND password_hash = %s
        """, (email, password_hash))
        
        result = cursor.fetchone()
        conn.close()
        
        if result:
            return {'id': result[0], 'name': result[1]}
        return None
    except Exception as e:
        st.error(f"Login error: {e}")
        return None

# Get all doctors
def get_doctors():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM doctors")
        doctors = cursor.fetchall()
        conn.close()
        
        return doctors
    except Exception as e:
        st.error(f"Error fetching doctors: {e}")
        return []

# Book appointment
def book_appointment(patient_id, doctor_id, date, time, symptoms):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time, symptoms)
            VALUES (%s, %s, %s, %s, %s)
        """, (patient_id, doctor_id, date, time, symptoms))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Booking error: {e}")
        return False

# Get patient appointments
def get_patient_appointments(patient_id):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT a.*, d.name as doctor_name, d.specialization
            FROM appointments a
            JOIN doctors d ON a.doctor_id = d.id
            WHERE a.patient_id = %s
            ORDER BY a.appointment_date DESC, a.appointment_time DESC
        """, (patient_id,))
        
        appointments = cursor.fetchall()
        conn.close()
        
        return appointments
    except Exception as e:
        st.error(f"Error fetching appointments: {e}")
        return []

# Add sample data
def add_sample_data():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        
        # Add sample doctors
        sample_doctors = [
            ("Dr. Sarah Johnson", "Cardiology", "sarah.johnson@hospital.com", "555-0101", 15, 150.00),
            ("Dr. Michael Chen", "Neurology", "michael.chen@hospital.com", "555-0102", 12, 180.00),
            ("Dr. Emily Davis", "Pediatrics", "emily.davis@hospital.com", "555-0103", 8, 120.00),
            ("Dr. Robert Wilson", "Orthopedics", "robert.wilson@hospital.com", "555-0104", 20, 200.00),
            ("Dr. Lisa Brown", "Dermatology", "lisa.brown@hospital.com", "555-0105", 10, 140.00)
        ]
        
        for doctor in sample_doctors:
            cursor.execute("""
                INSERT IGNORE INTO doctors (name, specialization, email, phone, experience_years, consultation_fee)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, doctor)
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        st.error(f"Error adding sample data: {e}")
        return False

# Main application
def main():
    st.set_page_config(page_title="Online Doctor Appointment System", page_icon="🏥", layout="wide")
    
    # Initialize database
    if not init_db():
        st.error("Failed to initialize database. Please check your MySQL connection.")
        return
    
    st.title("🏥 Online Doctor Appointment System")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.selectbox(
        "Choose a page",
        ["Home", "Patient Registration", "Patient Login", "Book Appointment", "My Appointments", "Admin Panel"]
    )
    
    # Initialize session state
    if 'patient_logged_in' not in st.session_state:
        st.session_state.patient_logged_in = False
    if 'patient_data' not in st.session_state:
        st.session_state.patient_data = None
    
    if page == "Home":
        st.header("Welcome to Online Doctor Appointment System")
        st.write("""
        This system allows you to:
        - Register as a patient
        - Book appointments with doctors
        - View your appointment history
        - Manage your healthcare appointments
        """)
        
        # Add sample data button (for demo purposes)
        if st.button("Add Sample Doctors (Demo)"):
            if add_sample_data():
                st.success("Sample doctors added successfully!")
    
    elif page == "Patient Registration":
        st.header("Patient Registration")
        
        with st.form("registration_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
            password = st.text_input("Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            
            submitted = st.form_submit_button("Register")
            
            if submitted:
                if password != confirm_password:
                    st.error("Passwords do not match!")
                elif not all([name, email, phone, password]):
                    st.error("Please fill in all fields!")
                else:
                    if register_patient(name, email, phone, password):
                        st.success("Registration successful! Please login.")
    
    elif page == "Patient Login":
        st.header("Patient Login")
        
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            
            submitted = st.form_submit_button("Login")
            
            if submitted:
                patient_data = patient_login(email, password)
                if patient_data:
                    st.session_state.patient_logged_in = True
                    st.session_state.patient_data = patient_data
                    st.success(f"Welcome back, {patient_data['name']}!")
                else:
                    st.error("Invalid email or password!")
    
    elif page == "Book Appointment":
        if not st.session_state.patient_logged_in:
            st.warning("Please login first to book an appointment.")
        else:
            st.header("Book Appointment")
            
            # Get available doctors
            doctors = get_doctors()
            
            if not doctors:
                st.warning("No doctors available. Please contact admin.")
            else:
                with st.form("appointment_form"):
                    # Doctor selection
                    doctor_options = {f"{d[1]} - {d[2]}": d[0] for d in doctors}
                    selected_doctor = st.selectbox("Select Doctor", list(doctor_options.keys()))
                    doctor_id = doctor_options[selected_doctor]
                    
                    # Date and time selection
                    today = datetime.now().date()
                    appointment_date = st.date_input("Appointment Date", min_value=today)
                    
                    # Available time slots
                    time_slots = [
                        "09:00", "09:30", "10:00", "10:30", "11:00", "11:30",
                        "14:00", "14:30", "15:00", "15:30", "16:00", "16:30"
                    ]
                    appointment_time = st.selectbox("Appointment Time", time_slots)
                    
                    symptoms = st.text_area("Describe your symptoms")
                    
                    submitted = st.form_submit_button("Book Appointment")
                    
                    if submitted:
                        if book_appointment(
                            st.session_state.patient_data['id'],
                            doctor_id,
                            appointment_date,
                            appointment_time,
                            symptoms
                        ):
                            st.success("Appointment booked successfully!")
                        else:
                            st.error("Failed to book appointment. Please try again.")
    
    elif page == "My Appointments":
        if not st.session_state.patient_logged_in:
            st.warning("Please login first to view your appointments.")
        else:
            st.header("My Appointments")
            
            appointments = get_patient_appointments(st.session_state.patient_data['id'])
            
            if not appointments:
                st.info("No appointments found.")
            else:
                # Convert to DataFrame for better display
                df = pd.DataFrame(appointments, columns=[
                    'ID', 'Patient ID', 'Doctor ID', 'Date', 'Time', 'Status',
                    'Symptoms', 'Created At', 'Doctor Name', 'Specialization'
                ])
                
                # Display appointments
                for _, appointment in df.iterrows():
                    with st.expander(f"Appointment on {appointment['Date']} at {appointment['Time']}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**Doctor:** {appointment['Doctor Name']}")
                            st.write(f"**Specialization:** {appointment['Specialization']}")
                            st.write(f"**Status:** {appointment['Status']}")
                        with col2:
                            st.write(f"**Date:** {appointment['Date']}")
                            st.write(f"**Time:** {appointment['Time']}")
                            if appointment['Symptoms']:
                                st.write(f"**Symptoms:** {appointment['Symptoms']}")
    
    elif page == "Admin Panel":
        st.header("Admin Panel")
        
        # Simple admin authentication (in real app, use proper authentication)
        admin_password = st.text_input("Admin Password", type="password")
        
        if admin_password == "admin123":  # Simple password for demo
            st.success("Admin access granted!")
            
            # View all appointments
            st.subheader("All Appointments")
            try:
                conn = mysql.connector.connect(**DB_CONFIG)
                cursor = conn.cursor()
                
                cursor.execute("""
                    SELECT a.*, p.name as patient_name, d.name as doctor_name
                    FROM appointments a
                    JOIN patients p ON a.patient_id = p.id
                    JOIN doctors d ON a.doctor_id = d.id
                    ORDER BY a.appointment_date DESC
                """)
                
                all_appointments = cursor.fetchall()
                conn.close()
                
                if all_appointments:
                    df = pd.DataFrame(all_appointments, columns=[
                        'ID', 'Patient ID', 'Doctor ID', 'Date', 'Time', 'Status',
                        'Symptoms', 'Created At', 'Patient Name', 'Doctor Name'
                    ])
                    st.dataframe(df)
                else:
                    st.info("No appointments found.")
                    
            except Exception as e:
                st.error(f"Error fetching appointments: {e}")
        elif admin_password:
            st.error("Invalid admin password!")

if __name__ == "__main__":
    main() 