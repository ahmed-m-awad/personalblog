# personal Blog

A simple blog application built with Flask.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Docker](#docker)


## Introduction

This project is a basic blog application developed using Flask. It allows users to create new blog posts, view existing posts, and interact with the application through a web interface.

## Features

- **Create Posts:** Users can create new blog posts with a title and content.
- **View Posts:** Existing blog posts are displayed on the main page.
- **Responsive Design:** The application is designed to work well on different screen sizes.

## Installation

To run this application locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ahmed-m-awad/personalblog.git
   cd presonalblog


2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```
4. **Set up environment variables:**
```bash 
FLASK_APP=app.py
FLASK_ENV=development
```
5. **Run the application:**
```bash 
flask run
```
The application will be accessible at http://127.0.0.1:5000
***

## Usage
1. Open your web browser and go to http://127.0.0.1:5000/ to view the blog.
2. Click on New Post to create a new blog post.

## Testing
To run tests for this application using pytest, execute the following command:
```bash 
pytest
```
## Docker

To run this application in a Docker container:

1. Pull the Docker image from Docker Hub:
```bash
docker pull ahmedmohamedawad/presonalblog:latest
```
2. Run the Docker container:
```bash
docker run -p 5000:5000 ahmedmohamedawad/presonalblog:latest
```
