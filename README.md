# Django React Search Application

The application is Developed by following Features:
# Video Output: https://drive.google.com/file/d/1B66jSCueoRyVUvJ2DhlKyqoVJVLHU0jN/view?usp=sharing
### Features
* This App used for Search value in list of value
* At frist user can register with image, then login with JWT authentication
* After Authentication user redirect into Value Input Page
* User Input Value like Comma separated integer, Search value 
* Input Value page show if Search value in included in input True Otherwise False
* User Registration Details Showed in profile portion
* Dashboard page show List of Search and input result
 

## Getting Started

```bash
python manage.py runserver
npm start
```

# Create the Django API with token-based JWT authentication: django App
* add vurtual environment
* For the First, Install Django
* install all requirement.txt file package
* Set up a Django project and create an API app.
```bash
django-admin startproject khoj_project
cd khoj_project
python manage.py startapp khoj_app

```
* Implement token-based authentication using Django Rest Framework (DRF) for user login and registration.
* Generate tokens for authenticated users.

# Set up the ReactJS frontend: with Create React App

* Create a ReactJS app and set up the necessary components and routing.
* Implement  registration, login page where users can enter their credentials and obtain a token.
* Create a value Input template that will be shown to authenticated users after login.
* Design template with input fields for "Input Values" and "Search Value," and a button labeled "Khoj".
* Allow users to input comma-separated integers as "Input Values" and a single integer as the "Search Value.
* cd project folde
* npm start
---
# Sort and store the "Input Values" in the database:
* Split the comma-separated "Input Values" into a list of integers.
* Sort the list of integers in descending order.
* conversion shorted list to string 
* Create a database entry for the sorted "string Values" along with the logged-in user's ID and the timestamp of the input.
* Check if the "Search Value" is present in the sorted "Input Values" obtained from the database.
* Return response to react app If the "Search Value" is found in the "Input Values," print "True" or False.
---
## Available Scripts

In the project directory, you can run:

### `npm start`

### `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)


## Available Scripts


**Progress:**
Version 1 completed and hosted

## SCREENSHOTS:**


<h2>Registraton Page</h2>
<img src="https://github.com/nusratdevo/evident_search_app/blob/main/screen/pic1.png" height="400">
---


<h2>Value Input Page</h2>
<img src="https://github.com/nusratdevo/evident_search_app/blob/main/screen/pic2.png" height="400">
---

<h2>Search list Page</h2>
<img src="https://github.com/nusratdevo/evident_search_app/blob/main/screen/pic3.png" height="400">
---

<h2>Api show</h2>
<img src="https://github.com/nusratdevo/evident_search_app/blob/main/screen/api.PNG" height="400">
---

