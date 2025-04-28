CREATE DATABASE IF NOT EXISTS library_system;
USE library_system;
CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO admin (username, password)
VALUES ('admin', 'admin123');

CREATE TABLE IF NOT EXISTS books (
    book_id VARCHAR(50) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    status ENUM('available', 'unavailable') DEFAULT 'available'
);
INSERT INTO books (book_id, title, author, year, price, status) VALUES
('B001', 'The Great Gatsby', 'F. Scott Fitzgerald', 1925, 10.99, 'available'),
('B002', 'To Kill a Mockingbird', 'Harper Lee', 1960, 12.49, 'available'),
('B003', '1984', 'George Orwell', 1949, 9.99, 'available'),
('B004', 'The Catcher in the Rye', 'J.D. Salinger', 1951, 8.99, 'available'),
('B005', 'Moby Dick', 'Herman Melville', 1851, 14.99, 'unavailable'),
('B006', 'Pride and Prejudice', 'Jane Austen', 1813, 7.99, 'available'),
('B007', 'The Hobbit', 'J.R.R. Tolkien', 1937, 11.99, 'available'),
('B008', 'War and Peace', 'Leo Tolstoy', 1869, 19.99, 'available'),
('B009', 'Crime and Punishment', 'Fyodor Dostoevsky', 1866, 13.49, 'available'),
('B010', 'Brave New World', 'Aldous Huxley', 1932, 10.49, 'available'),
('B011', 'The Odyssey', 'Homer', -800, 5.99, 'unavailable'),
('B012', 'The Iliad', 'Homer', -750, 6.99, 'available'),
('B013', 'The Picture of Dorian Gray', 'Oscar Wilde', 1890, 9.99, 'unavailable'),
('B014', 'The Brothers Karamazov', 'Fyodor Dostoevsky', 1880, 15.99, 'available'),
('B015', 'Anna Karenina', 'Leo Tolstoy', 1877, 18.99, 'available'),
('B016', 'Fahrenheit 451', 'Ray Bradbury', 1953, 10.49, 'available'),
('B017', 'Dracula', 'Bram Stoker', 1897, 8.49, 'unavailable'),
('B018', 'Wuthering Heights', 'Emily Brontë', 1847, 12.99, 'available'),
('B019', 'Frankenstein', 'Mary Shelley', 1818, 11.49, 'available'),
('B020', 'The Grapes of Wrath', 'John Steinbeck', 1939, 14.49, 'available'),
('B021', 'The Shining', 'Stephen King', 1977, 15.99, 'unavailable'),
('B022', 'The Road', 'Cormac McCarthy', 2006, 13.99, 'available'),
('B023', 'The Great Alone', 'Kristin Hannah', 2018, 16.99, 'available'),
('B024', 'Educated', 'Tara Westover', 2018, 12.99, 'available'),
('B025', 'Where the Crawdads Sing', 'Delia Owens', 2018, 14.49, 'available'),
('B026', 'Circe', 'Madeline Miller', 2018, 11.49, 'available'),
('B027', 'Sapiens: A Brief History of Humankind', 'Yuval Noah Harari', 2011, 18.99, 'available'),
('B028', 'Becoming', 'Michelle Obama', 2018, 17.49, 'unavailable'),
('B029', 'The Silent Patient', 'Alex Michaelides', 2019, 9.99, 'available'),
('B030', 'The Alchemist', 'Paulo Coelho', 1988, 10.99, 'available');

CREATE TABLE IF NOT EXISTS borrowers (
    member_id VARCHAR(255),
    member_type ENUM('student', 'teacher', 'other') NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    address TEXT,
    mobile_number VARCHAR(20),
    book_id VARCHAR(50),
    book_status ENUM('borrow', 'return') DEFAULT 'borrow',
    borrow_date DATE,
    due_date DATE,
    return_date DATE,
    late_return_days INT,
    late_return_fine DECIMAL(10,2)
);
