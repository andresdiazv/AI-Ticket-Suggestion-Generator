import os
import mysql.connector
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI()
conn = mysql.connector.connect(user=os.getenv("DB_USER"),
                               port=os.getenv("DB_PORT"),
                               password=os.getenv("DB_PASSWORD"),
                               host=os.getenv("DB_HOST"),
                               database=os.getenv("DB_NAME"))
cursor = conn.cursor(dictionary=True)

cursor.execute("SELECT * FROM ticket WHERE ticket_status = 'open'")
results = cursor.fetchall()

insert_suggestion_query = (
  "INSERT INTO ticket_suggestions (ticket_id, ticket_suggestion)"
  "VALUES (%s, %s)"
)

alter_status_query = (
    "UPDATE ticket "
    "SET ticket_status = 'closed' "
    "WHERE ticket_id = %s"
)

#     print(response.output_text)
for row in results:
    ticket_id = row.get("ticket_id")
    issue_description = row.get("issue_description")
    response_suggestion = client.responses.create(
    model="gpt-4.1-nano",
    input="Give a simple one line suggestion to help resolve the following issue:" + issue_description)
    suggestion_data = (ticket_id, response_suggestion.output_text)
    status_data = (ticket_id,)
    cursor.execute(insert_suggestion_query, suggestion_data)
    cursor.execute(alter_status_query, status_data)
    print(f"Processed ticket #{ticket_id} with GPT suggestion.")
    conn.commit()



cursor.close()
conn.close()