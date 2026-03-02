# Price Elasticity of Demand

A comprehensive educational resource and interactive application for understanding and calculating price elasticity of demand.

## 📊 What is Price Elasticity of Demand?

Price Elasticity of Demand (PED) measures how responsive the quantity demanded of a good is to changes in its price. It's a crucial concept in economics that helps businesses and policymakers understand consumer behavior.

### Mathematical Definition

The price elasticity of demand is calculated as:

$$
E_d = \frac{\% \text{ change in quantity demanded}}{\% \text{ change in price}} = \frac{\Delta Q / Q}{\Delta P / P}
$$

Or more formally:

$$
E_d = \frac{dQ}{dP} \times \frac{P}{Q}
$$

Where:
- $E_d$ = Price elasticity of demand
- $Q$ = Quantity demanded
- $P$ = Price
- $\Delta Q$ = Change in quantity
- $\Delta P$ = Change in price

## 🎯 Types of Price Elasticity

### 1. **Perfectly Inelastic** ($E_d = 0$)
- Quantity demanded doesn't change regardless of price
- Examples: Life-saving medications, insulin

### 2. **Inelastic** ($0 < |E_d| < 1$)
- Quantity demanded changes less than proportionally to price changes
- Examples: Gasoline, electricity, basic food items
- A 10% price increase leads to less than 10% decrease in demand

### 3. **Unit Elastic** ($|E_d| = 1$)
- Quantity demanded changes proportionally to price changes
- A 10% price increase leads to exactly 10% decrease in demand

### 4. **Elastic** ($|E_d| > 1$)
- Quantity demanded changes more than proportionally to price changes
- Examples: Luxury goods, restaurant meals, vacations
- A 10% price increase leads to greater than 10% decrease in demand

### 5. **Perfectly Elastic** ($E_d = \infty$)
- Any price increase leads to zero demand
- Theoretical concept; rarely seen in practice

## 💡 Factors Affecting Price Elasticity

1. **Availability of Substitutes**: More substitutes → more elastic
2. **Necessity vs. Luxury**: Necessities → less elastic
3. **Proportion of Income**: Larger % of income → more elastic
4. **Time Horizon**: Longer time → more elastic (consumers can adjust)
5. **Brand Loyalty**: Stronger loyalty → less elastic
6. **Market Definition**: Narrower market → more elastic

## 🎨 Interactive Application

This repository includes an interactive web application where you can:
- Calculate price elasticity with real-time visualizations
- Explore different elasticity scenarios
- See how demand curves change with different elasticity values
- Test your understanding with interactive examples

👉 **[Launch the App](./app/index.html)**

## 🐍 Python Implementation

```python
from elasticity import PriceElasticity

# Calculate elasticity
pe = PriceElasticity(
    initial_price=10,
    new_price=12,
    initial_quantity=100,
    new_quantity=80
)

print(f"Elasticity: {pe.calculate()}")
print(f"Type: {pe.get_type()}")
```

## 📈 Business Applications

### Revenue Optimization
- **Inelastic demand**: Price increases → Revenue increases
- **Elastic demand**: Price decreases → Revenue increases
- **Unit elastic**: Revenue maximized at current price

### Pricing Strategies
1. **Premium Pricing**: Works with inelastic demand
2. **Penetration Pricing**: Effective with elastic demand
3. **Dynamic Pricing**: Adjust based on elasticity shifts

## 🚀 Getting Started

### Using the Web App

Simply open `app/index.html` in your browser:

```bash
open app/index.html
```

Or use a local server:

```bash
python -m http.server 8000
# Navigate to http://localhost:8000/app/
```

### Using the Python Library

```bash
pip install -r requirements.txt
python examples/basic_calculation.py
```

## 📚 Examples

### Example 1: Coffee Shop
A coffee shop raises prices from $4 to $5 (25% increase). Sales drop from 200 to 150 cups per day (25% decrease).

$$
E_d = \frac{-25\%}{25\%} = -1
$$

**Result**: Unit elastic demand

### Example 2: Airline Tickets
An airline reduces prices from $300 to $270 (10% decrease). Bookings increase from 100 to 130 (30% increase).

$$
E_d = \frac{30\%}{-10\%} = -3
$$

**Result**: Elastic demand (|E_d| = 3)

### Example 3: Salt
Salt price increases from $1 to $1.20 (20% increase). Quantity sold decreases from 1000 to 980 units (2% decrease).

$$
E_d = \frac{-2\%}{20\%} = -0.1
$$

**Result**: Inelastic demand (|E_d| = 0.1)

## 📖 Additional Resources

- `/docs/theory.md` - Deep dive into elasticity theory
- `/docs/calculations.md` - Detailed calculation methods
- `/examples/` - Python code examples
- `/datasets/` - Sample datasets for practice

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

MIT License - feel free to use this for educational purposes.

## 🔗 References

1. Mankiw, N. G. (2020). *Principles of Economics*
2. Varian, H. R. (2014). *Intermediate Microeconomics*
3. Pindyck, R. S., & Rubinfeld, D. L. (2018). *Microeconomics*

---

**Made with ❤️ for economics students and business professionals**
