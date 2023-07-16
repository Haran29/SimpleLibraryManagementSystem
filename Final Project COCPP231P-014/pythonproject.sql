create database lms;
use lms;


-- Create Books table
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    publication_date DATE,
    isbn VARCHAR(255),
    availability_status VARCHAR(50)
);

-- Create Members table
CREATE TABLE Members (
    member_id INT PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(20)
);

-- Create Loans table
CREATE TABLE Loans (
    loan_id INT PRIMARY KEY,
    member_id INT,
    book_id INT,
    loan_date DATE,
    due_date DATE,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Create Admins table
CREATE TABLE Admins (
    admin_id INT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO Admins (admin_id,username, password) VALUES (1,'admin1', 'password1');
INSERT INTO Admins (admin_id,username, password) VALUES (2,'admin2', 'password2');
INSERT INTO Admins (admin_id,username, password) VALUES (3,'admin3', 'password3');
INSERT INTO Admins (admin_id,username, password) VALUES (4,'admin4', 'password4');
INSERT INTO Admins (admin_id,username, password) VALUES (5,'admin5', 'password5');

select *
from Admins



delete from books
where book_id = 1

INSERT INTO Books (book_id, title, author, publication_date, isbn, availability_status)
VALUES
    (1, 'The Great Gatsby', 'F. Scott Fitzgerald', '1925-04-10', '9780743273565', 'Available'),
    (2, 'To Kill a Mockingbird', 'Harper Lee', '1960-07-11', '9780446310789', 'Available'),
    (3, '1984', 'George Orwell', '1949-06-08', '9780452284234', 'On Loan'),
    (4, 'Pride and Prejudice', 'Jane Austen', '1813-01-28', '9780141439518', 'Available'),
    (5, 'The Catcher in the Rye', 'J.D. Salinger', '1951-07-16', '9780316769174', 'Available');

INSERT INTO Members (member_id, name, address, email, phone_number)
VALUES
    (1, 'John Smith', '123 Main St', 'john@example.com', '555-1234'),
    (2, 'Jane Doe', '456 Elm St', 'jane@example.com', '555-5678'),
    (3, 'David Johnson', '789 Oak St', 'david@example.com', '555-9012'),
    (4, 'Emily Wilson', '321 Pine St', 'emily@example.com', '555-3456'),
    (5, 'Michael Brown', '654 Cedar St', 'michael@example.com', '555-7890');


INSERT INTO Loans (loan_id, member_id, book_id, loan_date, due_date, return_date)
VALUES
    (1, 1, 2, '2023-05-01', '2023-05-15', NULL),
    (2, 3, 4, '2023-06-05', '2023-06-19', NULL),
    (3, 2, 1, '2023-05-10', '2023-05-24', NULL),
    (4, 4, 5, '2023-06-08', '2023-06-22', NULL),
    (5, 5, 3, '2023-05-20', '2023-06-03', NULL);

select * from  loans 
select * 
from books