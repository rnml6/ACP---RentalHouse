# Rental House Management System

The **Rental House Management System** is an application that allows users, especially landlords, to manage room rental details, including user accounts, room assignments, and monthly billing.

## Features

- **User Login**: Users can log in to their accounts to view their room details and payment information.
- **Admin Login**: Administrators can log in to manage room occupancies and user accounts.
- **Room Management**: Admins can add, update, or delete user data for room assignments.
- **View Dashboard**: Administrators can view the current statuses of rooms, including whether they are occupied or vacant, as well as tenant information. In contrast, users are only allowed to view their occupied rooms, billing details, and the contact information of their landlords using their user accounts.
- **Database Integration**: The application uses a MySQL database to store user and room data.

## Technologies Used

- **Python**: The application is built using Python 3.
- **Tkinter**: A GUI toolkit for creating the application's user interface.
- **MySQL Connector**: To facilitate database connections.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Install Required Packages**:
   Ensure that you have Python installed, then install the required packages:
   ```bash
   pip install mysql-connector-python
   ```
3. **Set Up MySQL Database**:
   - Create a MySQL database named `ronmeldb`.
   - Create the following tables with appropriate schema:
     - `ronmeltb`: For storing room and user data.
       - **Database Structure:** `room (Primary Key)`, `username`, `password`, `name`, `contacts`, `monthly`, `duedate`
     - `admintb`: For storing admin user data.
       - **Database Structure:** `admin`, `password`
   
4. **Run the Application**:
   Execute the main Python file:
   ```bash
   python main.py
   ```

## Usage

- **Admin Login**: Click on the **admin** button to access the admin features. Admins can manage room assignments through the dashboard.
- **User Login**: Users can log in with their username and password to view their room and payment details.

## Note

You can change the database connection settings in the code to match your local MySQL database credentials.
