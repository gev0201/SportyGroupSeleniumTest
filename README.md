# Twitch Mobile Web Testing Framework

A scalable Selenium-based test framework for testing the Twitch mobile web application using Chrome's mobile emulator.

## Project Structure

```
SportyGroupSeleniumTest/
├── .env                 # Environment variables (URLs)
├── conftest.py          # Pytest fixtures and Chrome mobile emulation setup
├── requirements.txt     # Project dependencies
├── pages/
│   ├── base_page.py     # Base page object with common methods
│   └── twitch_page.py   # Twitch-specific page object
├── tests/
│   └── test_twitch_search.py  # Test cases
└── screenshots/         # Directory for test screenshots
```

## Prerequisites

- Python 3.8+
- Google Chrome browser installed

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd SportyGroupSeleniumTest
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # macOS/Linux
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables (optional):
```bash
# .env file contains:
TWITCH_URL=https://m.twitch.tv
TWITCH_BROWSE_URL=https://m.twitch.tv/directory
```

## Running Tests

Run all tests:
```bash
pytest tests/ -v
```

Run with HTML report:
```bash
pytest tests/ -v --html=report.html
```

## Demo

![Test Demo](demo.gif)

> To create the demo.gif, record your screen while running `pytest tests/ -v` and convert to GIF using tools like [ScreenToGif](https://www.screentogif.com/) (Windows) or [Gifski](https://gif.ski/) (macOS).

## Test Case

The test `test_search_starcraft_and_select_streamer` performs the following steps:
1. Navigate to Twitch mobile site
2. Navigate to browse/directory page and search for "StarCraft II"
3. Scroll down to load more content
4. Select a streamer from the results
5. Handle any potential modals or pop-ups (mature content, cookie banners)
6. Wait for the stream page to load and take a screenshot

## Features

- **Page Object Model**: Scalable architecture with `BasePage` providing common methods
- **Template Method Pattern**: `navigate_to_url()` with `_after_navigate()` hook for page-specific logic
- **Chrome Mobile Emulation**: Tests run in mobile viewport (iPhone 14 Pro Max - 430x932)
- **Environment Configuration**: URLs managed via `.env` file using python-dotenv
- **Screenshot Capture**: Automatic screenshot on test completion
- **Modal Handling**: Handles cookie banners and mature content warnings
- **Explicit Waits**: Centralized `explicitly_wait()` static method for consistent timing
