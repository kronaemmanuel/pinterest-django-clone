# Pinterest Django Clone

This is a bare bones clone of the Pinterest Web app which has the following functionality:
- User can Signup/Login
- User can upload image(s)
    - Images have a size limit
- User can see a Home Feed of images
- User can like an image
    - Image Likes are counted globally and are shown to everyone
    - Users can sort images by likes
- User can comment on an image
    - Comments are shown globally to everyone
- User can save an image
    - Saved images can be viewed in a separate page for each user

## Quickstart
- Make sure you have a new virtual environment with `Django` and `mysqlclient` installed
- Make sure you have a working MySQL server
- Create an empty database for the project, Django will automatically create all the tables in the database
    ```sql
    mysql> CREATE DATABASE pinterest;
    ```
- Make a `local_settings.py` file using `local_settings.example.py` as a template. In the project folder, run:
    ```
    cp local_settings.example.py local_settings.py
    ```
- Replace the variables inside the `local_settings.py` with the corresponding settings for your own database and MySQL server user.
- Make appropriate migrations and migrate your database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
- Run the server
    ```
    python manage.py runserver
    ```

## Extra Libraries
- Pillow: `python -m pip install Pillow`
