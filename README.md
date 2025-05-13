🏦 Bank Branches API (REST)
This project is a simple Django-based REST API to fetch bank and branch details using a PostgreSQL database.

In this assignment, I have used REST API to fetch data.
I first imported the data given in the GitHub repo (sql dump) into my device.
Then I configured and imported the data from that dump to my own separate postgres database.




🚀 How to Run the Project
Set up a PostgreSQL database using WIN1252 encoding.

Import the provided SQL dump.

Clone this repository and set up a virtual environment.

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up your .env file with the required configurations.

Run the server:

bash
Copy
Edit
python manage.py runserver


| Method | Endpoint                             | Description                                             |
| ------ | ------------------------------------ | ------------------------------------------------------- |
| `GET`  | `/`                                  | Home page                                               |
| `GET`  | `/details`                           | Returns a list of all bank names                        |
| `GET`  | `/details/branches/<BANK NAME>`      | Returns all branches of the given bank                  |
| `GET`  | `/details/branchdetails/<IFSC CODE>` | Returns details of a specific branch based on IFSC code |

🔸 Examples
GET http://127.0.0.1:8000/details

GET http://127.0.0.1:8000/details/branches/CANARA%20BANK

GET http://127.0.0.1:8000/details/branchdetails/HDFC0001347


BANK LIST
![image](https://github.com/user-attachments/assets/d7e62e36-f2ec-4cb2-8cfb-4724b19349a2)

BRANCHES
![image](https://github.com/user-attachments/assets/6a8f61ed-4f34-4899-82c9-494278ae03d8)

BRANCH DETAILS
![image](https://github.com/user-attachments/assets/5e8f7576-2ad4-4c07-8519-433653298753)




⚠️ Challenges Faced:
The given database dump was encoded in WIN1252 format. Initially while importing the dump there was always encoding error. 
This took me a lot of time to realise that we could instead use our own database in WIN1252 encoding instead of the default UTF-8 encoding.

🕒 Time Taken
It took me a period of over 2 days to do this project. Most of the time was spent in figuring how to correctly import the database. After that I wrote the endpoints and some test cases, 
such as entering incorrect Bank names and incorrect IFSC codes.

🧪 Testing
The project includes basic testing for invalid inputs:

Nonexistent IFSC codes

![image](https://github.com/user-attachments/assets/c09c9dbb-eb4b-4036-ac1d-8af938b4e4d4)


Invalid or misspelled bank names
![image](https://github.com/user-attachments/assets/ceed148c-c6c7-4e63-a324-4b54da46ebad)


These return appropriate error messages.
📌 Note
This project is currently running on the Django development server(Localhost).

Deployment is not yet done due to potential issues with deploying a non-UTF8 PostgreSQL database (e.g., on Heroku).

