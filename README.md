# CS178 Programming Languages - Project 1.

**CS178: Cloud and Database Systems — Project #1**
**Author:** [Your Name]
**GitHub:** [your-username]

---

## Overview

<!-- Describe your project in 2-4 sentences. What does it do? Who is it for? What problem does it solve? -->

---

## Technologies Used

- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for programming languages from the GitHub Innovation Graph
- **AWS DynamoDB** — non-relational database for storing users and their favorite programming language
- **GitHub Actions** — auto-deploys code from GitHub to EC2 on push

---

## Project Structure

```
ProjectOne/
├── flaskapp.py          # Main Flask application — routes and app logic
├── dbCode.py            # Database helper functions (MySQL connection + queries)
├── creds_sample.py      # Sample credentials file (see Credential Setup below)
├── templates/
│   ├── home.html        # Landing page
│   ├── [other].html     # Add descriptions for your other templates
├── .gitignore           # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/Bloomy52/cs178-flask-app.git
   cd cs178-flask-app
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://127.0.0.1:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
https://flask.lnbloomberg.net
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "your-rds-endpoint"
user = "admin"
password = "your-password"
db = "your-database-name"
```

---

## Database Design

### SQL (MySQL on RDS)

<!-- Briefly describe your relational database schema. What tables do you have? What are the key relationships? -->

**Example:**

- `country` — stores ISO2 Codes and the name of said country; primary key is `iso2_code`
- `languages` — stores the ISO2 Code, programming language, number of developers, ; foreign key links to `country`

The JOIN query used in this project: <!-- describe it in plain English -->
Joining the ISO2 code from the `languages` table to the `country` table to get the country name for a specific programming langauge.

### DynamoDB

<!-- Describe your DynamoDB table. What is the partition key? What attributes does each item have? How does it connect to the rest of the app? -->

- **Table name:** `UserCodeLangs`
- **Partition key:** `username`
- **Used for:** storing a user's favorite programming language and their name.

---

## CRUD Operations

| Operation | Route           | Description                                                                                                         |
| --------- |-----------------|---------------------------------------------------------------------------------------------------------------------|
| Create    | `/add-user`     | Adds a user to DynamoDB                                                                                             |
| Read      | `/find-country` | Takes a username, takes their favorite language, and finds the country with the most programmers with said language |
| Update    | `/update-user`  | Update's a user's profile with their favorite programming language                                                  |
| Delete    | `/delete-user`  | Deletes the user's profile from DynamoDB                                                                            |

---

## Challenges and Insights

<!-- What was the hardest part? What did you learn? Any interesting design decisions? -->
The hardest part for me was coming up with an idea for the project. I learned that you can create very interesting things even with a small database. I had to decide on using only some of the columns from the datasets since it was a long dataset from the innovation graph.

---

## AI Assistance

<!-- List any AI tools you used (e.g., ChatGPT) and briefly describe what you used them for. Per course policy, AI use is allowed but must be cited in code comments and noted here. -->
(Links to chats will be cited by a 'citation' in the form of a `(#)` in the Markdown file).
I Used GitHub Copilot to help me write the code for the looping portion of the HTML code for `index.html` (1). 

I used Google Gemini to help me write the SQL code for my new database schema, github_innovation.sql (2).

I used a second GitHub Copilot chat to help me with fixing an error with my SQL code when I swapped databases (3).

#### AI Chat Links:
*Note: GitHub Copilot chats may expire after a certain period (I think 30 days) of which I cannot control. If the chat is lost, I will not be able to recover it.
(1) https://github.com/copilot/share/02410022-4a04-8cc1-b141-6e4ba03861d3
(2) https://gemini.google.com/share/baf4bce160c4
(3) https://github.com/copilot/share/c8004230-0b04-8445-b053-6e0b84f84982