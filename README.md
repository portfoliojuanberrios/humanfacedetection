
# Human Face Detection

This is a simple Django application for detecting human faces in images using TensorFlow and MTCNN.

## Requirements

- Python 3.x
- Docker
- Docker Compose

## Installation

### Using Docker

1. Clone this repository:
   ```sh
   git clone https://github.com/portfoliojuanberrios/humanfacedetection.git
   cd humanfacedetection
   ```

2. Build and run the Docker containers:
   ```sh
   docker-compose build
   docker-compose up
   ```

3. Access the application in your web browser at `http://localhost:8011/upload/`.

## Usage

1. Upload an image from the upload page.
2. The application will process the image and indicate if it contains a person.

## Project Structure

- `manage.py`: Django management script.
- `requirements.txt`: List of project dependencies.
- `Dockerfile`: Instructions for building the Docker image.
- `docker-compose.yml`: Configuration for Docker Compose.
- `mi_aplicacion/`: Main application folder containing views, forms, and utilities.
  - `__init__.py`: Initializes the application.
  - `admin.py`: Admin site configuration.
  - `apps.py`: Application configuration.
  - `forms.py`: Form for uploading images.
  - `migrations/`: Database migrations.
  - `models.py`: Database models (if any).
  - `tests.py`: Tests for the application.
  - `urls.py`: URL routing for the application.
  - `utils.py`: Utility functions for image processing.
  - `views.py`: View functions for handling requests.
  - `templates/mi_aplicacion/`: HTML templates for the application.
    - `result.html`: Template for displaying the result.
    - `upload.html`: Template for uploading images.
- `humanfacedetection/`: Project configuration folder.
  - `__init__.py`: Initializes the project.
  - `asgi.py`: ASGI configuration.
  - `settings.py`: Project settings.
  - `urls.py`: URL routing for the project.
  - `wsgi.py`: WSGI configuration.

## Environment Variables

- `DJANGO_SETTINGS_MODULE`: Django settings module (default is `humanfacedetection.settings`).

## Contribution

If you would like to contribute to this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact Juan Berrios Moya at [info@softdeveloper.com.au].

---

Thank you for using the Human Face Detection application!
