# Business Name Generator Summary

This project is a simple Flask web application that generates business name suggestions based on user input.

## What it does
- Accepts business-related keywords from a custom multi-select dropdown
- Supports an `Other` option for custom keywords
- Accepts an industry selection with an `Other` option for custom industries
- Includes a business description field to improve relevance
- Generates multiple unique name suggestions in a single request
- Prevents empty submissions and shows validation errors
- Displays generated names clearly in an easy-to-read list

## Key files
- `app.py` — Flask application and form handling
- `generator.py` — business name generation logic
- `templates/index.html` — UI template
- `static/style.css` — app styling
- `tests.py` — basic validation tests

## Run instructions
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the app:
   ```bash
   python app.py
   ```
3. Open `http://127.0.0.1:5000`
