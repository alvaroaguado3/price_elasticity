# Project Structure

```
price_elasticity/
│
├── README.md                          # Main project documentation
├── QUICKSTART.md                      # Quick start guide
├── CONTRIBUTING.md                    # Contribution guidelines
├── LICENSE                            # MIT License
├── .gitignore                         # Git ignore rules
├── requirements.txt                   # Python dependencies
├── setup.py                          # Package setup file
├── elasticity.py                     # Main Python module
│
├── app/                              # Interactive Web Application
│   ├── index.html                   # Main HTML page
│   ├── styles.css                   # Styling
│   └── app.js                       # JavaScript logic
│
├── docs/                             # Documentation
│   ├── theory.md                    # Detailed theory guide
│   └── calculations.md              # Calculation methods
│
├── examples/                         # Python Examples
│   ├── basic_calculation.py         # Basic examples
│   ├── advanced_analysis.py         # Advanced scenarios
│   └── data_analysis.py             # Data analysis with viz
│
├── datasets/                         # Sample Data
│   └── sample_price_data.csv        # Sample dataset
│
├── tests/                            # Unit Tests
│   ├── __init__.py
│   ├── README.md                    # Test documentation
│   └── test_elasticity.py          # Main test suite
│
└── visualizations/                   # Output folder for charts
    └── .gitkeep
```

## File Descriptions

### Core Files

- **elasticity.py** - Main Python library with PriceElasticity class and utilities
- **setup.py** - Package installation and distribution setup
- **requirements.txt** - Python package dependencies

### Web Application

- **app/index.html** - Interactive calculator with visualizations
- **app/styles.css** - Modern, responsive styling
- **app/app.js** - Calculator logic and Chart.js integration

### Documentation

- **README.md** - Overview, theory, and getting started
- **QUICKSTART.md** - 5-minute quick start guide
- **docs/theory.md** - Deep dive into elasticity theory
- **docs/calculations.md** - Calculation methods explained
- **CONTRIBUTING.md** - How to contribute to the project

### Examples

- **basic_calculation.py** - 4 basic examples with explanations
- **advanced_analysis.py** - Real-world business scenarios
- **data_analysis.py** - Pandas/Matplotlib analysis with visualizations

### Data & Tests

- **datasets/sample_price_data.csv** - 20 product examples
- **tests/test_elasticity.py** - Comprehensive test suite
- **visualizations/** - Output directory for generated charts

## Key Features

### 📊 Interactive Web App
- Real-time calculations
- Demand curve visualization
- Pre-loaded examples (coffee, airline, salt, luxury)
- Business insights and recommendations
- Mobile-responsive design

### 🐍 Python Library
- Midpoint and simple calculation methods
- Revenue impact analysis
- Elasticity type classification
- Optimal price calculation
- Rich interpretations

### 📚 Educational Content
- Complete theory guide
- Multiple calculation methods
- Real-world examples
- Business applications
- Economic principles

### 🧪 Production Ready
- Unit tests with pytest
- Type documentation
- Error handling
- Clean code structure
- MIT License

## Getting Started

### Web Application (Instant)
```bash
cd app
open index.html
```

### Python Library
```bash
pip install -r requirements.txt
python elasticity.py
python examples/basic_calculation.py
```

### Run Tests
```bash
pytest tests/
```

## Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+), Chart.js
- **Backend**: Python 3.7+
- **Libraries**: NumPy, SciPy, Pandas, Matplotlib
- **Testing**: pytest
- **Version Control**: Git

## License

MIT License - Free for educational and commercial use
