MySQL Workbench

ticket table:
==============
CREATE TABLE ticket (
ticket_id INT NOT NULL AUTO_INCREMENT,
customer_name VARCHAR(100),
customer_email VARCHAR(100),
issue_description TEXT,
ticket_status VARCHAR(20),
created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (ticket_id)
);

ticket_summaries table:
==============
CREATE TABLE ticket_summaries (
ticket_id INT NOT NULL AUTO_INCREMENT,
summary_text TEXT,
summary_suggestion TEXT,
created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(ticket_id) REFERENCES tickets(ticket_id)
);

Populating Ticket Table:
============== 
INSERT INTO tickets (customer_name, customer_email, issue_description, ticket_status)
VALUES ("Mark Cuban", "mcuban@gmail.com", "website page is freezing", "open");