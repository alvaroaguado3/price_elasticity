# Calculation Methods

This guide explains the different methods for calculating price elasticity of demand and when to use each one.

## 1. Simple Percentage Method

### Formula

$$
E_d = \frac{\frac{Q_2 - Q_1}{Q_1}}{\frac{P_2 - P_1}{P_1}} = \frac{\Delta Q / Q_1}{\Delta P / P_1}
$$

### When to Use
- Small price changes (< 10%)
- Quick approximations
- Teaching/learning purposes

### Advantages
- Simple to calculate
- Intuitive

### Disadvantages
- Asymmetric: gives different results depending on direction of change
- Less accurate for large changes

### Example

A product's price increases from $10 to $12, and quantity falls from 100 to 80.

```python
Q1, Q2 = 100, 80
P1, P2 = 10, 12

quantity_change_pct = (Q2 - Q1) / Q1  # -20%
price_change_pct = (P2 - P1) / P1      # 20%

elasticity = quantity_change_pct / price_change_pct  # -1.0
```

### Asymmetry Problem

Going from A to B:
- Price $10 → $12: +20%
- Quantity 100 → 80: -20%
- Elasticity = -20% / 20% = -1.0

Going from B to A:
- Price $12 → $10: -16.67%
- Quantity 80 → 100: +25%
- Elasticity = 25% / -16.67% = -1.5

**Different results for the same change!**

## 2. Midpoint (Arc) Method

### Formula

$$
E_d = \frac{\frac{Q_2 - Q_1}{(Q_1 + Q_2)/2}}{\frac{P_2 - P_1}{(P_1 + P_2)/2}}
$$

### When to Use
- Moderate to large price changes
- When direction of change matters
- Research and analysis
- **Recommended for most practical applications**

### Advantages
- Symmetric: same result regardless of direction
- More accurate for larger changes
- Standard in economic analysis

### Disadvantages
- Slightly more complex calculation

### Example

Same data: Price from $10 to $12, quantity from 100 to 80.

```python
Q1, Q2 = 100, 80
P1, P2 = 10, 12

avg_quantity = (Q1 + Q2) / 2  # 90
avg_price = (P1 + P2) / 2      # 11

quantity_change_pct = (Q2 - Q1) / avg_quantity  # -22.22%
price_change_pct = (P2 - P1) / avg_price        # 18.18%

elasticity = quantity_change_pct / price_change_pct  # -1.22
```

### Symmetry Check

Going from A to B or B to A gives the same result: **-1.22**

## 3. Point Elasticity Method

### Formula

For a demand function $Q = f(P)$:

$$
E_d = \frac{dQ}{dP} \times \frac{P}{Q}
$$

### When to Use
- Theoretical analysis
- Continuous demand functions known
- Calculus-based optimization
- Very small changes (infinitesimal)

### Example: Linear Demand

For $Q = 100 - 2P$:

$$
\frac{dQ}{dP} = -2
$$

At price $P = 20$:
- $Q = 100 - 2(20) = 60$
- $E_d = -2 \times \frac{20}{60} = -0.67$ (inelastic)

At price $P = 40$:
- $Q = 100 - 2(40) = 20$
- $E_d = -2 \times \frac{40}{20} = -4$ (elastic)

### Example: Power Function Demand

For $Q = 100P^{-2}$:

$$
\frac{dQ}{dP} = -200P^{-3}
$$

$$
E_d = -200P^{-3} \times \frac{P}{100P^{-2}} = -2
$$

Constant elasticity of -2 at all prices!

### Python Implementation

```python
from scipy.misc import derivative

def demand_function(P):
    return 100 - 2 * P

def point_elasticity(P, demand_func):
    Q = demand_func(P)
    dQ_dP = derivative(demand_func, P, dx=1e-6)
    return dQ_dP * (P / Q)

# Calculate at P = 20
elasticity = point_elasticity(20, demand_function)
print(f"Elasticity at P=20: {elasticity:.2f}")
```

## 4. Log-Linear Method (Constant Elasticity)

### Formula

For demand function: $\ln Q = a + E_d \ln P$

The coefficient $E_d$ is the price elasticity.

### When to Use
- Econometric estimation
- Regression analysis
- Large datasets

### Example

```python
import numpy as np
from scipy import stats

# Sample data
prices = np.array([10, 12, 14, 16, 18, 20])
quantities = np.array([100, 85, 73, 64, 56, 50])

# Take logarithms
ln_P = np.log(prices)
ln_Q = np.log(quantities)

# Linear regression
slope, intercept, r_value, p_value, std_err = stats.linregress(ln_P, ln_Q)

print(f"Price Elasticity: {slope:.2f}")
print(f"R-squared: {r_value**2:.3f}")
```

## Comparison of Methods

| Method | Accuracy | Complexity | Symmetry | Best For |
|--------|----------|------------|----------|----------|
| Simple % | Low | Low | No | Small changes |
| Midpoint | High | Medium | Yes | **Most cases** |
| Point | Very High | High | N/A | Theoretical work |
| Log-Linear | High | High | Yes | Econometrics |

## Special Cases

### 1. Zero Denominator

If $P_1 = P_2$, elasticity is undefined (division by zero).

**Solution:** The question itself is invalid—need a price change to measure elasticity.

### 2. Infinite Elasticity

If quantity changes but price doesn't ($\Delta P = 0$ but $\Delta Q \neq 0$):

This represents perfectly elastic demand.

### 3. Zero Elasticity

If price changes but quantity doesn't ($\Delta Q = 0$ but $\Delta P \neq 0$):

This represents perfectly inelastic demand.

## Practical Calculation Tips

### 1. Always Use Midpoint for Discrete Data

Unless you have a specific reason, use the midpoint method for real-world price changes.

### 2. Check Your Sign

Price elasticity of demand should be **negative** (demand curve slopes down). If you get a positive number, check your calculation!

### 3. Interpret the Magnitude

Remember: it's the **absolute value** that matters for classification:
- $|E_d| < 1$: Inelastic
- $|E_d| = 1$: Unit elastic
- $|E_d| > 1$: Elastic

### 4. Consider the Context

- Short-term vs. long-term elasticity may differ
- Different customer segments have different elasticities
- Elasticity varies along the demand curve

## Common Mistakes to Avoid

### 1. Swapping Numerator and Denominator

$$
\text{WRONG: } E_d = \frac{\Delta P / P}{\Delta Q / Q}
$$

$$
\text{CORRECT: } E_d = \frac{\Delta Q / Q}{\Delta P / P}
$$

### 2. Forgetting the Negative Sign

Price and quantity move in opposite directions, so elasticity is negative!

### 3. Using Simple % for Large Changes

For changes > 20%, always use midpoint method.

### 4. Confusing Elasticity with Slope

Slope is $\Delta Q / \Delta P$

Elasticity is $(\Delta Q / Q) / (\Delta P / P)$

They're related but different!

## Python Implementation Summary

```python
def calculate_elasticity_simple(P1, P2, Q1, Q2):
    """Simple percentage method."""
    price_change_pct = (P2 - P1) / P1
    quantity_change_pct = (Q2 - Q1) / Q1
    return quantity_change_pct / price_change_pct

def calculate_elasticity_midpoint(P1, P2, Q1, Q2):
    """Midpoint (arc) method - RECOMMENDED."""
    avg_price = (P1 + P2) / 2
    avg_quantity = (Q1 + Q2) / 2
    price_change_pct = (P2 - P1) / avg_price
    quantity_change_pct = (Q2 - Q1) / avg_quantity
    return quantity_change_pct / price_change_pct

def calculate_elasticity_point(P, Q, dQ_dP):
    """Point elasticity method."""
    return dQ_dP * (P / Q)
```

## Further Reading

- Nicholson, W., & Snyder, C. (2011). *Microeconomic Theory: Basic Principles and Extensions*. Chapter 5.
- Pindyck & Rubinfeld (2018). *Microeconomics*. Chapter 2.
- Wooldridge, J. (2015). *Introductory Econometrics*. Chapter 6 (for log-linear models).
