## Ticket Suggestion Generator

This project takes open support tickets from a MySQL database, uses an AI model to generate a resolution suggestion, then stores the suggestion and closes the ticket.

---

### Requirements

* Python 3.10+
* MySQL
* `.env` file with the following keys:

  * `DB_HOST`
  * `DB_USER`
  * `DB_PASSWORD`
  * `DB_PORT`
  * `DB_NAME`
  * `OPENAI_API_KEY`

Install dependencies:

```bash
pip install openai mysql-connector-python python-dotenv
```

---

### Create Tables

```sql
CREATE TABLE ticket (
  ticket_id INT NOT NULL AUTO_INCREMENT,
  customer_name VARCHAR(100),
  customer_email VARCHAR(100),
  issue_description TEXT,
  ticket_status VARCHAR(20),
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (ticket_id)
);
```

```sql
CREATE TABLE ticket_suggestions (
  ticket_id INT NOT NULL,
  ticket_suggestion TEXT,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (ticket_id),
  FOREIGN KEY (ticket_id) REFERENCES ticket(ticket_id)
);
```

---

### Sample Data

```sql
INSERT INTO ticket (customer_name, customer_email, issue_description, ticket_status)
VALUES ("Mark Cuban", "mcuban@gmail.com", "website page is freezing", "open");
```

---
