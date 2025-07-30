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

for row in results:
    issue_description = row.get("issue_description")

response = client.responses.create(
    model="gpt-4.1-nano",
    input="Give a simple one line suggestion to help resolve the following issue:" + issue_description
)

print(response.output_text)
cursor.close()
conn.close()