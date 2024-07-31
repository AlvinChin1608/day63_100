# day63_100

# Enhancing Flask Applications with SQLAlchemy
Today, I made significant strides in enhancing my Flask applications with SQLAlchemy for better database management. Here’s a summary of the key concepts and improvements:

### DEMO
![](https://github.com/AlvinChin1608/day63_100/blob/main/gif_demo/full_demo_SQLDBconverter.gif)

Note: To access the SQL database, you will need to download SQLite to open the db file

## Using SQLAlchemy for Database Management:

- __Table Creation:__
  - Moved from manually writing SQL queries to using SQLAlchemy’s ORM (Object-Relational Mapping) for table creation. This approach reduces the risk of human error and makes the code more maintainable.
  - Defined a Book model class with SQLAlchemy that maps to a table in the SQLite database. The class specifies columns and their attributes, allowing SQLAlchemy to handle the SQL commands behind the scenes.
 
- __Database Configuration:__
  - Configured the Flask app to use an SQLite database through SQLAlchemy. This setup involves setting the database URI and initializing the SQLAlchemy extension.
 
- __CRUD Operations:__
  - __Create:__ Added new records to the database using SQLAlchemy’s session management.
    
    ![](https://github.com/AlvinChin1608/day63_100/blob/main/gif_demo/adding-ezgif.com-video-to-gif-converter.gif)
    
  - __Read:__ Queried the database to retrieve and display records.
  - __Update:__ Modified existing records by querying and updating them.

    ![](https://github.com/AlvinChin1608/day63_100/blob/main/gif_demo/update-ezgif.com-video-to-gif-converter.gif)
    
  - __Delete:__ Removed records from the database as needed.
    
    ![](https://github.com/AlvinChin1608/day63_100/blob/main/gif_demo/delete-ezgif.com-video-to-gif-converter.gif)

By integrating SQLAlchemy with Flask, I streamlined database operations, improved the maintainability of my code, and enhanced the user interface of my application. This approach allows me to manage my database more effectively while ensuring a user-friendly experience through well-organized HTML templates.

## What I Learned Today
### SQLite
- Database Basics: Gained a solid understanding of SQLite, a lightweight, disk-based database that doesn't require a separate server process. Ideal for small to medium-sized applications.
- Database File: Learned how to configure SQLite in a Flask application using a .db file to store data persistently.
- Schema Management: Explored creating and managing database schemas programmatically, which ensures that the database structure aligns with the application's needs.

### SQLAlchemy
- ORM Fundamentals: Mastered the basics of SQLAlchemy, an Object-Relational Mapping (ORM) library that allows for the mapping of Python classes to database tables.
- Declarative Base: Utilized DeclarativeBase to define the base class for all models, simplifying model creation and schema management.
- Model Definition: Implemented SQLAlchemy models using Python classes, defining table columns with types such as Integer, String, and Float.
- CRUD Operations: Learned how to perform Create, Read, Update, and Delete operations on database records. This includes adding new records, querying existing ones, updating attributes, and deleting entries.
- Session Management: Used SQLAlchemy's session object to manage transactions and persist changes to the database.
- Integration with Flask: Integrated SQLAlchemy with Flask to handle database interactions seamlessly within a web application. This includes initializing the database, creating tables, and performing CRUD operations within the Flask app context.

### Transition from In-Memory Storage
- Enhanced Data Persistence: Transitioned from using a Python dictionary to store data in memory to using an SQL database. This shift ensures data is persistently stored and reliably managed across application sessions.
- Error Reduction: Reduced potential for human error by leveraging SQLAlchemy’s ORM capabilities to handle database interactions instead of manually writing SQL queries.
