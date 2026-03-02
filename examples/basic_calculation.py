"""
Basic examples of using the Price Elasticity calculator.
"""

from elasticity import PriceElasticity, calculate_elasticity


def example_coffee_shop():
    """Example: A coffee shop considering a price increase."""
    print("=" * 60)
    print("EXAMPLE 1: COFFEE SHOP PRICING")
    print("=" * 60)
    print("\nScenario:")
    print("A local coffee shop is considering raising the price of")
    print("their signature latte from $4 to $5.")
    print("They estimate sales would drop from 200 to 150 cups/day.\n")
    
    pe = PriceElasticity(
        initial_price=4,
        new_price=5,
        initial_quantity=200,
        new_quantity=150
    )
    
    elasticity = pe.calculate()
    
    print(f"Price Elasticity: {elasticity:.3f}")
    print(f"Elasticity Type: {pe.get_type()}\n")
    
    print("Interpretation:")
    print(pe.get_interpretation())
    print()
    
    revenue = pe.get_revenue_impact()
    print("Revenue Impact:")
    print(f"  Current daily revenue: ${revenue['initial_revenue']:.2f}")
    print(f"  Projected daily revenue: ${revenue['new_revenue']:.2f}")
    print(f"  Change: ${revenue['revenue_change']:.2f} ({revenue['revenue_change_percent']:.1f}%)")
    
    if revenue['revenue_change'] > 0:
        annual_increase = revenue['revenue_change'] * 365
        print(f"\n  Annual revenue increase: ${annual_increase:,.2f}")
    
    print("\n")


def example_airline_tickets():
    """Example: An airline running a promotional sale."""
    print("=" * 60)
    print("EXAMPLE 2: AIRLINE PROMOTIONAL PRICING")
    print("=" * 60)
    print("\nScenario:")
    print("An airline reduces ticket prices from $300 to $270")
    print("for a promotional sale. Bookings increase from 100 to 130.\n")
    
    pe = PriceElasticity(
        initial_price=300,
        new_price=270,
        initial_quantity=100,
        new_quantity=130
    )
    
    elasticity = pe.calculate()
    
    print(f"Price Elasticity: {elasticity:.3f}")
    print(f"Elasticity Type: {pe.get_type()}\n")
    
    print("Interpretation:")
    print(pe.get_interpretation())
    print()
    
    revenue = pe.get_revenue_impact()
    print("Revenue Impact:")
    print(f"  Regular revenue: ${revenue['initial_revenue']:,.2f}")
    print(f"  Promotional revenue: ${revenue['new_revenue']:,.2f}")
    print(f"  Change: ${revenue['revenue_change']:,.2f} ({revenue['revenue_change_percent']:.1f}%)")
    
    print("\n  Recommendation: The promotion is SUCCESSFUL!")
    print("  Lower prices led to increased revenue due to elastic demand.")
    print("\n")


def example_necessity_good():
    """Example: A necessity good with inelastic demand."""
    print("=" * 60)
    print("EXAMPLE 3: NECESSITY GOOD (SALT)")
    print("=" * 60)
    print("\nScenario:")
    print("Salt prices increase from $1.00 to $1.20 (20% increase).")
    print("Quantity sold decreases only slightly, from 1000 to 980 units.\n")
    
    pe = PriceElasticity(
        initial_price=1.00,
        new_price=1.20,
        initial_quantity=1000,
        new_quantity=980
    )
    
    elasticity = pe.calculate()
    
    print(f"Price Elasticity: {elasticity:.3f}")
    print(f"Elasticity Type: {pe.get_type()}\n")
    
    print("Interpretation:")
    print(pe.get_interpretation())
    print()
    
    revenue = pe.get_revenue_impact()
    print("Revenue Impact:")
    print(f"  Initial revenue: ${revenue['initial_revenue']:,.2f}")
    print(f"  New revenue: ${revenue['new_revenue']:,.2f}")
    print(f"  Change: ${revenue['revenue_change']:,.2f} ({revenue['revenue_change_percent']:.1f}%)")
    
    print("\n  This demonstrates INELASTIC demand:")
    print("  Consumers continue buying despite price increase,")
    print("  as salt is a necessity with no close substitutes.")
    print("\n")


def example_luxury_good():
    """Example: A luxury good with elastic demand."""
    print("=" * 60)
    print("EXAMPLE 4: LUXURY GOOD (DESIGNER WATCH)")
    print("=" * 60)
    print("\nScenario:")
    print("A luxury watch retailer raises prices from $5,000 to $5,500.")
    print("Monthly sales drop from 50 to 30 units.\n")
    
    pe = PriceElasticity(
        initial_price=5000,
        new_price=5500,
        initial_quantity=50,
        new_quantity=30
    )
    
    elasticity = pe.calculate()
    
    print(f"Price Elasticity: {elasticity:.3f}")
    print(f"Elasticity Type: {pe.get_type()}\n")
    
    print("Interpretation:")
    print(pe.get_interpretation())
    print()
    
    revenue = pe.get_revenue_impact()
    print("Revenue Impact:")
    print(f"  Initial monthly revenue: ${revenue['initial_revenue']:,.2f}")
    print(f"  New monthly revenue: ${revenue['new_revenue']:,.2f}")
    print(f"  Change: ${revenue['revenue_change']:,.2f} ({revenue['revenue_change_percent']:.1f}%)")
    
    if revenue['revenue_change'] < 0:
        annual_loss = abs(revenue['revenue_change']) * 12
        print(f"\n  Annual revenue loss: ${annual_loss:,.2f}")
        print("\n  Recommendation: REDUCE prices back to original level.")
        print("  Luxury items have elastic demand - consumers are price-sensitive.")
    
    print("\n")


def comparison_example():
    """Compare elasticity across different product categories."""
    print("=" * 60)
    print("COMPARISON: ELASTICITY ACROSS PRODUCT CATEGORIES")
    print("=" * 60)
    print("\nAll products experience a 10% price increase.\n")
    
    products = [
        ("Insulin", 100, 110, 1000, 995, "Life-saving medication"),
        ("Bread", 2, 2.20, 500, 450, "Basic necessity"),
        ("Restaurant Meal", 25, 27.50, 200, 160, "Discretionary spending"),
        ("Luxury Car", 50000, 55000, 10, 4, "Luxury item")
    ]
    
    results = []
    
    for name, p1, p2, q1, q2, category in products:
        pe = PriceElasticity(p1, p2, q1, q2)
        elasticity = pe.calculate()
        results.append((name, category, elasticity, abs(elasticity), pe.get_type()))
    
    print(f"{'Product':<20} {'Category':<25} {'Elasticity':<12} {'Type':<20}")
    print("-" * 85)
    
    for name, category, elasticity, abs_e, etype in results:
        print(f"{name:<20} {category:<25} {elasticity:>10.3f}  {etype:<20}")
    
    print("\n" + "=" * 60)
    print("KEY INSIGHT:")
    print("=" * 60)
    print("As products become more 'necessary' or have fewer substitutes,")
    print("demand becomes more inelastic (closer to 0).")
    print("\nAs products become more 'luxury' or have more substitutes,")
    print("demand becomes more elastic (farther from 0).")
    print("\n")


if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 10 + "PRICE ELASTICITY CALCULATION EXAMPLES" + " " * 10 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\n")
    
    example_coffee_shop()
    input("Press Enter to continue to next example...")
    
    example_airline_tickets()
    input("Press Enter to continue to next example...")
    
    example_necessity_good()
    input("Press Enter to continue to next example...")
    
    example_luxury_good()
    input("Press Enter to continue to next example...")
    
    comparison_example()
    
    print("Examples complete! Try modifying the values to see different scenarios.")
