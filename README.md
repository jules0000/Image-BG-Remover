# Image Background Remover with Flask

This project is a Flask-based web application that allows users to upload images and remove their backgrounds using the `rembg` library.

## Features

- **Flask Framework**: Manages the web server, routes, and templates.
- **Image Upload**: Supports `.png`, `.jpg`, `.jpeg`, and `.webp` formats.
- **Background Removal**: Integrates the `rembg` library for seamless background removal.
- **PIL Library**: Handles image processing and saving.
- **Secure File Uploads**: Ensures secure file handling using `werkzeug`.
- **Static Uploads Folder**: Saves both the original and processed images.
- **User Interface**: Renders `home.html` for uploading and displaying images.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jules0000/image-bg-remover.git
   ```

2. Navigate to the project directory:

   ```bash
   cd image-bg-remover
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

---

## Usage

- Access the application at `http://127.0.0.1:5000/`.
- Upload an image from the home page.
- View the original image and the background-removed version side by side.

---

## Project Structure

```
image-bg-remover/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
├── static/
│   └── uploads/           # Folder for uploaded images
├── templates/
│   └── home.html          # Frontend template
└── README.md               # Project documentation
```

---

## Dependencies

- Flask==2.2.5
- Pillow==9.4.0
- rembg==2.0.25
- Werkzeug==2.2.3

---

## Author

Julia Ayessa M. Castro
