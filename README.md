
# Medicine Recommendation System

The Medicine Recommendation System is a web application built using Flask, a Python web framework. It provides a user-friendly interface to recommend medicines based on selected indications. This system aims to assist users in finding suitable medicines quickly and efficiently by categorizing medicines according to their indications.

## Features

- **Indication Selection**: Users can choose from a list of available indications, such as "Fever," "Diabetes," "High Cholesterol," etc.
  
- **Medicine Recommendation**: Based on the selected indication, the system recommends medicines that are suitable for treating or managing that particular health condition.
  
- **Detailed Information**: Users can view detailed information about each recommended medicine, including its category, dosage form, strength, manufacturer, and classification (prescription or over-the-counter).

## Prerequisites

- Python 3.x installed on your system.
- Flask framework (`pip install Flask`).

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install dependencies:**

   ```bash
   pip install Flask
   ```

## Usage

1. **Run the Flask application:**

   ```bash
   python app.py
   ```

2. **Access the application:**

   Open a web browser and go to `http://127.0.0.1:5000/`.

3. **Select an indication:**

   - Choose an indication from the dropdown list.
   - Click on "Get Recommendations".

4. **View recommended medicines:**

   - You will be directed to a page showing recommended medicines for the selected indication.
   - Click on any medicine to view detailed information.

5. **Navigate back:**

   - Use the "Back to Home" link to return to the home page and select a different indication.

## File Structure

```
├── app.py                    # Flask application code
└── templates                 # HTML templates
    ├── index.html            # Home page template
    └── recommend.html        # Recommendation results template
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

.
