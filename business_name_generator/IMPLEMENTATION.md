# Business Name Generator Implementation

## Architecture
- Flask serves the web UI and processes form submissions.
- The generator module builds business name suggestions using keywords, styles, and industry.
- The UI uses a custom dropdown for multi-select keyword selection and handles `Other` values.

## Flow
1. User opens the page and submits keyword/industry/style/count values.
2. `app.py` validates the input and constructs a combined search string.
3. `generator.py` combines keywords with prefixes, suffixes, and style words.
4. Names are filtered for uniqueness and relevance before display.

## Generator details
- `generator.generate_names(text_input, industry, style, count)`
- Uses default styles for `modern`, `professional`, and `creative`
- Uses a simple AI-style scoring heuristic to rank and pick the best names by relevance and semantic fit
- Builds suggestions with:
  - keyword + suffix
  - prefix + keyword
  - adjective + keyword
  - keyword + industry
- If too few names are generated, it adds fallback combinations.

## UI details
- `templates/index.html` contains the form and results area.
- Custom dropdown shows selected keywords in the input label.
- `Other` keyword and industry fields appear when selected.
- `static/style.css` keeps the layout simple and aligned.

## Testing
- `tests.py` validates core generator behavior:
  - at least one result for valid input
  - exact count when requested
  - empty input validation raises a `ValueError`
