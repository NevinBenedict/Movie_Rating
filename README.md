Abstract: Movie Management System

The Movie Management System is a Django-based web application designed to manage and explore a collection of movies. It provides features for users to browse, review, and rate movies, while administrators can add, update, and delete movie records. The system is built with a responsive design using Bootstrap and includes user authentication for secure access.

Key Features:

User Authentication:

Users can register, log in, and log out securely.
Superusers have additional privileges to manage movies.

Movie Management:
Superusers can add, update, and delete movies.
Each movie includes details such as name, genre, language, year, director, and poster.

Movie Browsing:
Users can browse a list of movies with details like name, genre, language, year, and average rating.
Movies are displayed with posters and ratings for better user experience.

Review and Rating:
Users can add reviews and ratings for movies.
Reviews can be updated or deleted by the user who created them.

Dynamic Features:
Average ratings are dynamically calculated and displayed for each movie.
Posters are displayed as thumbnails during upload for better usability.

Responsive Design:
The application is fully responsive, ensuring compatibility across devices.

Search and Filter:
Users can search for movies by name, genre, language, or year.

Technology Stack:

Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap, JavaScript
Database: SQLite (default Django database)
Icons: Font Awesome

Project Structure:

Movie/
├── myapp/
│   ├── migrations/
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── movielist.html
│   │   ├── moviedetails.html
│   │   ├── movieadd.html
│   │   ├── reviewadd.html
│   │   ├── reviewlist.html
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
├── manage.py
├── db.sqlite3


How to Run:
Clone the repository:
git clone <repository-url>cd Movie

Apply migrations:
python manage.py makemigrations
python manage.py migrate

Run the development server:
python manage.py runserver

Access the application at http://127.0.0.1:8000/.

