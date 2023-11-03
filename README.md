# Books-store

Book Store API
This is a simple REST API for managing a list of books built using Django and Django REST Framework. The API provides endpoints for performing CRUD operations on the book model, along with JWT authentication for securing the API.


Setup and Running the Project
To set up and run the project locally, follow these steps:

1.Clone the repository to your local machine using the following command:
git clone {git-url}

2.Activate the virtual environment using the following command:
pipenv shell

3.Install the necessary dependencies using Pipenv:
pipenv install

4.Apply any initial migrations by running the following command:
python manage.py makemigrations

5.Apply the database migrations to set up the initial database schema:
python manage.py migrate

6.Start the development server using the following command:
python manage.py runserver


Using the API with Postman
To interact with the API using Postman, follow the steps outlined below:

1.Launch Postman and create a new request collection for the Book Store API.

2.Obtain the JWT token by sending a POST request to the following endpoint:
POST /api/token/
Ensure that you provide your credentials (username and password) in the request body.

3.After obtaining the JWT token, you can use it to access the protected API endpoints. Include the token in the request header with the following format:
Authorization: Bearer <your_access_token>

4.Use the appropriate HTTP methods (GET, POST, PUT, DELETE) to interact with the various API endpoints for managing the books. 
For example:
To retrieve all books, send a GET request to:
GET /api/books/
To create a new book, send a POST request to:
POST /api/books/
To update an existing book, send a PUT request to:
PUT /api/books/<id>/
To delete a book, send a DELETE request to:
DELETE /api/books/<id>/


Example API Requests:

To obtain a JWT token:
![Screenshot (15)](https://github.com/girish-katare13/Books-store/assets/100254272/ee7e691a-442f-48a4-9781-6e54636f9693)

To list all books.:
![Screenshot (16)](https://github.com/girish-katare13/Books-store/assets/100254272/3fc74508-1eb6-4c60-8086-f2f5ff7c06b7)

To retrieve a specific book by ID.:
![Screenshot (17)](https://github.com/girish-katare13/Books-store/assets/100254272/95a700ac-4a2e-447c-a18c-4fa6971ee824)

To create a new book.:
![Screenshot (18)](https://github.com/girish-katare13/Books-store/assets/100254272/cd845541-268d-41e3-b143-1ec1da75b48c)

To update an existing book.:
![Screenshot (19)](https://github.com/girish-katare13/Books-store/assets/100254272/b81b7726-f174-40dd-b7b1-1259b342b43f)

To delete a book.:
![Screenshot (20)](https://github.com/girish-katare13/Books-store/assets/100254272/c4c1d91f-d548-471f-bdbe-256aad0aaf8a)


Security Considerations
The project has implemented JWT authentication to secure the API endpoints. The access token's lifetime has been set to 60 minutes, while the refresh token's lifetime has been set to 1 day. This ensures that the tokens expire after the specified duration, enhancing the overall security of the application.


Acknowledgments:

Django REST Framework: We utilized the Django REST Framework for developing the RESTful API endpoints and taking advantage of its powerful serialization capabilities.

JSON Web Token (JWT): We implemented JWT authentication to secure our API endpoints and ensure secure communication between the client and the server. The implementation was made possible by leveraging the JSON Web Token library. 
