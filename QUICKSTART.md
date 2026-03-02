# Quick Start Guide

Get started with the Price Elasticity project in just a few minutes!

## Web Application (No installation required)

The easiest way to start is using the web application:

1. **Navigate to the app folder:**
   ```bash
   cd app
   ```

2. **Open in your browser:**
   ```bash
   open index.html
   ```
   
   Or on Linux/Windows:
   ```bash
   # Linux
   xdg-open index.html
   
   # Windows
   start index.html
   ```

3. **Start calculating!** Try the pre-loaded examples or enter your own values.

## Python Library

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/price_elasticity.git
   cd price_elasticity
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Basic Usage

```python
from elasticity import PriceElasticity

# Create an instance with your data
pe = PriceElasticity(
    initial_price=10,
    new_price=12,
    initial_quantity=100,
    new_quantity=80
)

# Calculate elasticity
elasticity = pe.calculate()
print(f"Elasticity: {elasticity:.2f}")

# Get classification
print(f"Type: {pe.get_type()}")

# Analyze revenue impact
revenue = pe.get_revenue_impact()
print(f"Revenue change: ${revenue['revenue_change']:.2f}")
```

### Running Examples

```bash
# Basic examples
python examples/basic_calculation.py

# Advanced analysis
python examples/advanced_analysis.py

# Data analysis with visualizations
python examples/data_analysis.py
```

## 5-Minute Tutorial

### Scenario: Coffee Shop Pricing

You run a coffee shop and want to know if raising prices will increase revenue.

**Current situation:**
- Price: $4 per coffee
- Daily sales: 200 coffees
- Daily revenue: $800

**Proposed change:**
- New price: $5 per coffee
- Expected sales: 150 coffees
- Projected revenue: $750

**Analysis:**

```python
from elasticity import PriceElasticity

pe = PriceElasticity(4, 5, 200, 150)
elasticity = pe.calculate()

print(f"Elasticity: {elasticity:.2f}")
# Output: Elasticity: -1.22

print(f"Type: {pe.get_type()}")
# Output: Type: Elastic

print("\n" + pe.get_interpretation())
# Output: Detailed interpretation...
```

**Result:** Demand is elastic (|Ed| > 1), so raising prices will **reduce** revenue by $50/day or $18,250/year!

**Recommendation:** Don't raise the price, or raise it by less.

## Common Use Cases

### 1. Should I raise or lower prices?

```python
pe = PriceElasticity(your_current_price, proposed_price, 
                    current_sales, expected_sales)

if pe.calculate() < -1:  # Elastic
    print("Revenue optimization: Lower prices increase revenue")
else:  # Inelastic
    print("Revenue optimization: Higher prices increase revenue")
```

### 2. What's my optimal price?

```python
from elasticity import calculate_optimal_price

optimal = calculate_optimal_price(
    current_price=10,
    current_quantity=1000,
    elasticity=-2.0,  # Your measured elasticity
    cost_per_unit=5
)

print(f"Optimal price: ${optimal['optimal_price']:.2f}")
```

### 3. Comparing different scenarios

```python
scenarios = [
    ("Low price", 8, 120),
    ("Medium price", 10, 100),
    ("High price", 12, 80),
]

for name, price, quantity in scenarios:
    revenue = price * quantity
    print(f"{name}: ${revenue}")
    
# Find the revenue-maximizing price
```

## Interactive Web App Features

The web application provides:

✅ **Real-time calculations** - Instant results as you type
✅ **Visual demand curves** - See how elasticity affects the curve
✅ **Pre-loaded examples** - Learn from real-world scenarios
✅ **Business insights** - Get actionable recommendations
✅ **No installation** - Works in any modern browser

## Learning Path

**Beginners:**
1. Read the main [README.md](README.md) for theory
2. Use the web app with pre-loaded examples
3. Try the basic Python examples

**Intermediate:**
1. Study [docs/theory.md](docs/theory.md) for deeper understanding
2. Run [examples/advanced_analysis.py](examples/advanced_analysis.py)
3. Analyze your own business data

**Advanced:**
1. Review [docs/calculations.md](docs/calculations.md)
2. Use the library for data analysis
3. Contribute new examples or features

## Next Steps

- 📖 Read the [complete theory guide](docs/theory.md)
- 🔢 Learn about [calculation methods](docs/calculations.md)
- 💡 Explore [advanced examples](examples/advanced_analysis.py)
- 🤝 Check out [contributing guidelines](CONTRIBUTING.md)

## Getting Help

- 📧 Open an issue on GitHub
- 💬 Ask questions in discussions
- 📚 Check the documentation in `/docs`

## Quick Reference

### Elasticity Types

| Type | Value | Meaning |
|------|-------|---------|
| Perfectly Inelastic | 0 | Demand unchanged by price |
| Inelastic | 0 to -1 | Demand changes less than price |
| Unit Elastic | -1 | Demand changes equal to price |
| Elastic | < -1 | Demand changes more than price |
| Perfectly Elastic | -∞ | Infinite demand response |

### Revenue Impact

| Elasticity | Price ↑ | Price ↓ |
|------------|---------|---------|
| Elastic | Revenue ↓ | Revenue ↑ |
| Unit Elastic | Revenue → | Revenue → |
| Inelastic | Revenue ↑ | Revenue ↓ |

Happy analyzing! 📊
