# Café Calle Ocho — EGN 475 Week 2 Assignment 2.2

Static HTML mockup using Pico CSS v2. Open `mockup/menu.html` in a browser. No backend, JavaScript, or data persistence.

## Screens
- `menu.html` — menu items and category labels
- `order.html` — order summary and pickup name
- `confirmation.html` — order confirmation
- `kitchen.html` — kitchen order board
- `history.html` — recent order history
- `admin.html` — sample menu administration

## Suggested commit sequence
Commit each HTML page separately, e.g. `git add mockup/menu.html && git commit -m "Add menu mockup"`, repeating for each page. Then commit documentation and push. Do not claim commits were made until verified.

## AI log guidance
The initial six HTML files in this package were drafted with ChatGPT, not GitHub Copilot. If you use Copilot to revise each screen, add the exact prompts and changes you actually made to the AI log before submitting.

## Week 3 - Flask Application

The Cafe Calle Ocho prototype is now a Flask application
with dynamic Jinja templates and sample data.

### Features

- Home page
- Menu with six products
- Individual item details
- Order creation form
- Kitchen board
- Order history
- Custom 404 error page
- Shared navigation using url_for()
- Prices stored as integer cents

### How to Run

1. Create a virtual environment:
   py -m venv .venv

2. Install dependencies:
   pip install -r requirements.txt

3. Start the application:
   python -m flask --app app run --debug

4. Open http://127.0.0.1:5000

### Current Limitations

The application uses sample data.
Database integration and order saving will be
implemented in Week 4.
