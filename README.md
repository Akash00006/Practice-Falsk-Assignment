# Flask Password Manager

## 1. Flask Password Manager

A simple password manager application developed using Python and Flask. The application allows users to add, retrieve, and delete username-password records using REST API endpoints.

---

## 2. Description

This project is a basic in-memory Password Manager built using Flask.

Users can store a username and password using the `/add` API endpoint. The stored password can be retrieved using the `/get/<username>` endpoint.

In Version 2, a delete functionality was added using the `/delete/<username>` endpoint.

The application stores data temporarily in a Python dictionary, so the data will be lost whenever the application is restarted.

### API Endpoints

| Endpoint             | Method | Description                               |
| -------------------- | ------ | ----------------------------------------- |
| `/`                  | GET    | Displays the welcome message              |
| `/health`            | GET    | Checks whether the application is running |
| `/add`               | POST   | Adds a username and password              |
| `/get/<username>`    | GET    | Retrieves the password for a username     |
| `/delete/<username>` | DELETE | Deletes a username and password           |

### Example `/add` Request

```json
{
    "username": "akash",
    "password": "abcd12345"
}
```

### Example `/get/<username>` Response

```json
{
    "username": "akash",
    "password": "abcd12345"
}
```

### Example `/delete/<username>` Response

```json
{
    "message": "User deleted successfully"
}
```

---

## 3. Tech Stack

The following technologies were used to develop this project:

* **Python 3.x** – Programming language
* **Flask** – Web framework used to create the REST API
* **Git** – Version control
* **GitHub** – Source code repository and project hosting
* **Postman** – Used for API testing
* **VS Code** – Code editor

### Data Storage

The application uses a Python dictionary for in-memory storage.

No external database is required for this project.

---

## 4. Deployment

### Run Locally

### Step 1: Clone the Repository

```bash
git clone https://github.com/Akash00006/Assesment_Project_shopping_app.git
```

### Step 2: Navigate to the Project Folder

```bash
cd <YOUR_PROJECT_FOLDER>
```

### Step 3: Install Flask

```bash
pip install flask
```

### Step 4: Run the Application

```bash
python -m flask --app app run --debug
```

The application will start on:

```text
http://localhost:5000
```

<img width="1259" height="771" alt="1" src="https://github.com/user-attachments/assets/439a28d5-123a-44c2-a6c6-31c314a985b8" />


### Step 5: Test the Application

Open the following URL in a browser:

```text
http://localhost:5000/
```

Health check:

```text
http://localhost:5000/health
```
<img width="1140" height="776" alt="2" src="https://github.com/user-attachments/assets/82a677e7-1699-478e-8b77-745a3595e6cd" />



For the `/add`, `/get/<username>`, and `/delete/<username>` APIs, Postman can be used for testing.

### Git Branching Workflow

The project uses two branches:

```text
main
  |
  |---- Version 1
  |
  |---- Version 2

dev
  |
  |---- Development
  |
  |---- Testing
  |
  +---- Merge into main
```

All development work was performed in the `dev` branch.

After testing and verifying the functionality, the changes were merged into the `main` branch.

---

## 5. Screenshots

### Application Running

The following screenshot shows the Flask application running successfully.

<img width="1259" height="771" alt="1" src="https://github.com/user-attachments/assets/559ec0b5-7bdc-4162-bca0-73c8aa7d6002" />


---

### GitHub Branches

The following screenshot shows the `dev` and `main` branches in the GitHub repository.

<img width="347" height="258" alt="image" src="https://github.com/user-attachments/assets/357307e1-73c0-4910-bec9-f7e3461b6dff" />


---

### Git Version History

The following screenshot shows the Version 1 and Version 2 commit/merge history.


<img width="1402" height="733" alt="image" src="https://github.com/user-attachments/assets/7f0da6e8-f159-4a73-ba5c-5fea6045d27b" />

---

### API Testing in Postman

The following screenshot shows the Password Manager APIs being tested using Postman.

<img width="700" height="484" alt="8" src="https://github.com/user-attachments/assets/d2aa4b3a-c5ed-41b0-aaa5-97c7328eafe5" />

<img width="715" height="516" alt="9" src="https://github.com/user-attachments/assets/ae9a2a43-0c76-4f7d-90c8-9ae2323e16b0" />

<img width="722" height="481" alt="10" src="https://github.com/user-attachments/assets/507807c8-71d0-49fe-8307-e4e91026a83d" />

---

## 6. Troubleshooting


### Problem: 

<img width="762" height="628" alt="6" src="https://github.com/user-attachments/assets/7d3e4862-04cf-4c75-8c20-c51b700b4c8a" />

<img width="655" height="651" alt="12" src="https://github.com/user-attachments/assets/4a54ba76-15df-4165-8443-145fbf5cddc0" />

