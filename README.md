# Business Name Generator

A Flask-based web application that generates creative, relevant, and unique business names based on user-provided keywords and preferences. The application uses an AI-inspired scoring mechanism to rank generated names according to relevance and semantic fit.

## Features

* Generate multiple business names from user input
* Support for different naming styles (Modern, Professional, Creative, etc.)
* Input validation for keywords and generation count
* Regenerate names without re-entering details
* AI-style scoring and ranking of generated names
* Simple and user-friendly web interface

## Installation

### 1. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

```text
http://127.0.0.1:5000
```

## Usage

1. Enter one or more business-related keywords.
2. Select a preferred naming style.
3. Specify the number of names to generate.
4. Click **Generate Names**.
5. Review the generated names and use **Regenerate** if needed.

## Acceptance Criteria

* Generates 1 to N unique business names
* Produces relevant names based on user keywords
* Supports multiple naming styles
* Validates user input before processing
* Allows regeneration of names
* Displays ranked results using a scoring heuristic

## Documentation

* `SUMMARY.md` – Project overview and execution steps
* `IMPLEMENTATION.md` – System architecture and implementation details

## Technologies Used

* Python
* Flask
* HTML/CSS
* Jinja2 Templates

## Version

**Business Name Generator v1.0**

Developed by Neha P
