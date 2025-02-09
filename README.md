# Library Management System

A Python-based library management system built using Tkinter for the GUI and integrated with Microsoft SQL Server for data storage. The system helps manage books, users, and borrowing records, making it easy for libraries to maintain and track their collections.


## Features

- **Book Management**: Add, update, and delete books in the library.
- **User Management**: Add, update, and delete users.
- **Borrowing System**: Track books that have been borrowed and return dates.
- **Search Functionality**: Search for books or users in the system.
- **Database Integration**: Connects to a Microsoft SQL Server database for data persistence.

## Tech Stack

- **Frontend**: Tkinter (GUI framework)
- **Backend**: Python
- **Database**: Microsoft SQL Server
- **Libraries**:
  - `tkinter` for the GUI
  - `pyodbc` for connecting to SQL Server
  - Other required libraries in `requirements.txt`

## Installation

### Prerequisites

- Python 3.x
- Microsoft SQL Server (locally or remotely hosted)

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Haran29/Library-Management-System.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd Library-Management-System
    ```

3. **Install required Python libraries**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    - Ensure Microsoft SQL Server is running and accessible.
    - Create a database named `library_management`.
    - Modify the `config.py` file to include the correct connection details (host, database name, user, password).

5. **Run the application**:
    ```bash
    python main.py
    ```

## Usage

1. **Launch the application**: 
    - Run the `main.py` script to open the Tkinter-based GUI.
   
2. **Add Books**:
    - Navigate to the "Books" section and add new books to the library.

3. **Manage Users**:
    - Add, modify, or remove user profiles for borrowers.

4. **Track Borrowed Books**:
    - Keep track of books that are borrowed and their respective due dates.

5. **Search**:
    - Use the search bar to quickly find books or users.



## Contributing

1. Fork the repository.
2. Create a new branch for your feature or fix (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add feature'`).
4. Push to your fork (`git push origin feature-branch`).
5. Create a pull request detailing your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
