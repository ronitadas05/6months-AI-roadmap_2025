# 🏥 Online Doctor Appointment System

A comprehensive web-based doctor appointment booking system built with Python, Streamlit, and MySQL.

## Features

### 👥 Patient Features
- **Patient Registration**: Create new patient accounts with secure password hashing
- **Patient Login**: Secure authentication system
- **Appointment Booking**: Book appointments with available doctors
- **Appointment History**: View all past and upcoming appointments
- **Symptom Description**: Add symptoms when booking appointments

### 👨‍⚕️ Doctor Management
- **Doctor Database**: Comprehensive doctor profiles with specializations
- **Specialization Categories**: Cardiology, Neurology, Pediatrics, Orthopedics, Dermatology
- **Experience & Fees**: Track doctor experience and consultation fees
- **Availability**: Manage appointment slots and schedules

### 🔧 Admin Features
- **Admin Panel**: View all appointments and system data
- **Database Management**: Monitor patient and doctor registrations
- **Appointment Overview**: Complete system overview for administrators

## 🚀 Setup Instructions

### Prerequisites
- Python 3.7+
- MySQL Server
- pip (Python package manager)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. MySQL Database Setup
1. Start your MySQL server
2. Create a new database:
```sql
CREATE DATABASE doctor_appointment_db;
```

### 3. Configure Database Connection
Edit the `DB_CONFIG` in `doctor_appointment_system.py`:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_mysql_password',  # Add your MySQL password
    'database': 'doctor_appointment_db'
}
```

### 4. Run the Application
```bash
streamlit run doctor_appointment_system.py
```

## 📋 Database Schema

### Patients Table
- `id`: Primary key
- `name`: Patient full name
- `email`: Unique email address
- `phone`: Contact number
- `password_hash`: Hashed password for security
- `created_at`: Registration timestamp

### Doctors Table
- `id`: Primary key
- `name`: Doctor full name
- `specialization`: Medical specialization
- `email`: Contact email
- `phone`: Contact number
- `experience_years`: Years of experience
- `consultation_fee`: Appointment fee
- `created_at`: Registration timestamp

### Appointments Table
- `id`: Primary key
- `patient_id`: Foreign key to patients
- `doctor_id`: Foreign key to doctors
- `appointment_date`: Scheduled date
- `appointment_time`: Scheduled time
- `status`: Appointment status (scheduled/completed/cancelled)
- `symptoms`: Patient symptoms description
- `created_at`: Booking timestamp

## 🎯 Usage Guide

### For Patients
1. **Register**: Create a new account with your details
2. **Login**: Access your account
3. **Book Appointment**: 
   - Select a doctor and specialization
   - Choose date and time slot
   - Describe your symptoms
   - Confirm booking
4. **View Appointments**: Check your appointment history

### For Administrators
1. **Access Admin Panel**: Use password "admin123" (demo)
2. **View All Appointments**: Monitor system activity
3. **Add Sample Data**: Use the "Add Sample Doctors" button for demo

## 🔒 Security Features
- Password hashing using SHA-256
- Session management for logged-in users
- Input validation and sanitization
- Secure database connections

## 🛠️ Customization

### Adding New Specializations
Edit the `add_sample_data()` function to include new doctor specializations.

### Modifying Time Slots
Update the `time_slots` list in the booking form to change available appointment times.

### Database Schema Changes
Modify the table creation SQL in the `init_db()` function.

## 📱 Demo Features
- Sample doctors with various specializations
- Pre-configured time slots
- Admin panel for system overview
- Responsive web interface

## 🚨 Important Notes
- This is a demo system - implement proper security for production
- Add proper error handling and logging
- Consider adding email notifications
- Implement appointment cancellation features
- Add doctor availability management

## 🤝 Contributing
Feel free to enhance the system with additional features like:
- Email notifications
- Payment integration
- Video consultation
- Prescription management
- Patient medical history

## 📞 Support
For issues or questions, please check the error messages in the application or review the database connection settings. 