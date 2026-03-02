"""
Advanced examples demonstrating price elasticity analysis with data.
"""

import sys
sys.path.append('..')

from elasticity import PriceElasticity, calculate_optimal_price


def revenue_maximization_example():
    """
    Demonstrate how to find revenue-maximizing price point.
    """
    print("=" * 70)
    print("REVENUE MAXIMIZATION ANALYSIS")
    print("=" * 70)
    print("\nScenario: A streaming service wants to optimize subscription price")
    print("They test different price points and measure subscriber counts.\n")
    
    # Test price points
    test_scenarios = [
        (8, 500000),   # $8/month - 500k subscribers
        (10, 450000),  # $10/month - 450k subscribers
        (12, 400000),  # $12/month - 400k subscribers
        (15, 320000),  # $15/month - 320k subscribers
    ]
    
    print(f"{'Price':<10} {'Subscribers':<15} {'Revenue':<15} {'Elasticity':<12} {'Type':<15}")
    print("-" * 70)
    
    max_revenue = 0
    optimal_price = 0
    
    for i in range(len(test_scenarios) - 1):
        price1, subs1 = test_scenarios[i]
        price2, subs2 = test_scenarios[i + 1]
        
        revenue = price1 * subs1
        
        pe = PriceElasticity(price1, price2, subs1, subs2)
        elasticity = pe.calculate()
        
        print(f"${price1:<9} {subs1:<15,} ${revenue:<14,} {elasticity:<11.2f} {pe.get_type():<15}")
        
        if revenue > max_revenue:
            max_revenue = revenue
            optimal_price = price1
    
    # Last price point
    last_price, last_subs = test_scenarios[-1]
    last_revenue = last_price * last_subs
    print(f"${last_price:<9} {last_subs:<15,} ${last_revenue:<14,} {'N/A':<11} {'N/A':<15}")
    
    if last_revenue > max_revenue:
        max_revenue = last_revenue
        optimal_price = last_price
    
    print("\n" + "=" * 70)
    print(f"OPTIMAL PRICE: ${optimal_price}/month")
    print(f"MAXIMUM MONTHLY REVENUE: ${max_revenue:,}")
    print("=" * 70)
    print("\n")


def segment_analysis_example():
    """
    Analyze elasticity for different customer segments.
    """
    print("=" * 70)
    print("CUSTOMER SEGMENT ANALYSIS")
    print("=" * 70)
    print("\nScenario: A gym raises membership from $50 to $55/month")
    print("Different customer segments respond differently.\n")
    
    segments = [
        ("Students", 50, 55, 200, 140, "Price-sensitive, many alternatives"),
        ("Young Professionals", 50, 55, 300, 270, "Moderately price-sensitive"),
        ("Executives", 50, 55, 100, 95, "Less price-sensitive, value quality"),
    ]
    
    print(f"{'Segment':<20} {'Elasticity':<12} {'Type':<15} {'Members Lost':<15}")
    print("-" * 70)
    
    total_before = 0
    total_after = 0
    
    for segment_name, p1, p2, q1, q2, description in segments:
        pe = PriceElasticity(p1, p2, q1, q2)
        elasticity = pe.calculate()
        members_lost = q1 - q2
        
        print(f"{segment_name:<20} {elasticity:<11.2f} {pe.get_type():<15} {members_lost:<15}")
        print(f"  → {description}")
        
        total_before += q1
        total_after += q2
    
    revenue_before = 50 * total_before
    revenue_after = 55 * total_after
    
    print("\n" + "-" * 70)
    print(f"Total members before: {total_before}")
    print(f"Total members after: {total_after}")
    print(f"Total members lost: {total_before - total_after}")
    print(f"\nRevenue before: ${revenue_before:,}")
    print(f"Revenue after: ${revenue_after:,}")
    print(f"Revenue change: ${revenue_after - revenue_before:,} "
          f"({((revenue_after - revenue_before)/revenue_before)*100:.1f}%)")
    
    print("\n" + "=" * 70)
    print("RECOMMENDATION:")
    print("=" * 70)
    print("Consider differentiated pricing:")
    print("  • Student discount: $45/month (retain price-sensitive segment)")
    print("  • Standard rate: $55/month (young professionals)")
    print("  • Premium tier: $75/month with extras (executives)")
    print("=" * 70)
    print("\n")


def competitive_response_example():
    """
    Analyze how competitor pricing affects elasticity.
    """
    print("=" * 70)
    print("COMPETITIVE RESPONSE ANALYSIS")
    print("=" * 70)
    print("\nScenario: Coffee shop market with competitive dynamics\n")
    
    print("Phase 1: Your shop raises prices, competitors don't")
    print("-" * 70)
    
    pe1 = PriceElasticity(
        initial_price=4,
        new_price=4.50,
        initial_quantity=300,
        new_quantity=210
    )
    
    elasticity1 = pe1.calculate()
    revenue1 = pe1.get_revenue_impact()
    
    print(f"Your price: $4.00 → $4.50")
    print(f"Elasticity: {elasticity1:.2f} ({pe1.get_type()})")
    print(f"Revenue change: ${revenue1['revenue_change']:.2f} "
          f"({revenue1['revenue_change_percent']:.1f}%)")
    print(f"\nCustomers are VERY sensitive to your price increase")
    print(f"(they switch to competitors)")
    
    print("\n" + "=" * 70)
    print("\nPhase 2: All competitors raise prices together")
    print("-" * 70)
    
    pe2 = PriceElasticity(
        initial_price=4,
        new_price=4.50,
        initial_quantity=300,
        new_quantity=280
    )
    
    elasticity2 = pe2.calculate()
    revenue2 = pe2.get_revenue_impact()
    
    print(f"Your price: $4.00 → $4.50")
    print(f"Elasticity: {elasticity2:.2f} ({pe2.get_type()})")
    print(f"Revenue change: ${revenue2['revenue_change']:.2f} "
          f"({revenue2['revenue_change_percent']:.1f}%)")
    print(f"\nCustomers are LESS sensitive when all shops raise prices")
    print(f"(fewer alternatives available)")
    
    print("\n" + "=" * 70)
    print("KEY INSIGHT:")
    print("=" * 70)
    print("Elasticity depends on competitive context!")
    print("• Isolated price change: More elastic demand")
    print("• Industry-wide price change: Less elastic demand")
    print("=" * 70)
    print("\n")


def seasonal_elasticity_example():
    """
    Demonstrate how elasticity varies by season.
    """
    print("=" * 70)
    print("SEASONAL ELASTICITY ANALYSIS")
    print("=" * 70)
    print("\nScenario: Ice cream shop price elasticity across seasons\n")
    
    seasons = [
        ("Summer (Peak)", 5, 6, 1000, 900, "High demand, less elastic"),
        ("Fall", 5, 6, 600, 480, "Moderate demand"),
        ("Winter (Off-peak)", 5, 6, 200, 120, "Low demand, more elastic"),
    ]
    
    print(f"{'Season':<20} {'Price':<10} {'Elasticity':<12} {'Revenue Change':<15}")
    print("-" * 70)
    
    for season_name, p1, p2, q1, q2, note in seasons:
        pe = PriceElasticity(p1, p2, q1, q2)
        elasticity = pe.calculate()
        revenue_impact = pe.get_revenue_impact()
        
        print(f"{season_name:<20} ${p1}→${p2:<6} {elasticity:<11.2f} "
              f"{revenue_impact['revenue_change_percent']:>6.1f}%")
        print(f"  → {note}")
    
    print("\n" + "=" * 70)
    print("PRICING STRATEGY:")
    print("=" * 70)
    print("• Summer: Premium pricing (inelastic demand)")
    print("• Fall: Moderate pricing")
    print("• Winter: Deep discounts/promotions (stimulate elastic demand)")
    print("=" * 70)
    print("\n")


def bundling_example():
    """
    Analyze elasticity for bundled vs. individual products.
    """
    print("=" * 70)
    print("PRODUCT BUNDLING ANALYSIS")
    print("=" * 70)
    print("\nScenario: Software company selling products individually vs. bundled\n")
    
    print("Individual Products (10% price increase):")
    print("-" * 70)
    
    individual_products = [
        ("Word Processor", 50, 55, 1000, 700),
        ("Spreadsheet", 50, 55, 1000, 680),
        ("Presentation", 30, 33, 800, 520),
    ]
    
    total_individual_revenue_before = 0
    total_individual_revenue_after = 0
    
    for product, p1, p2, q1, q2 in individual_products:
        pe = PriceElasticity(p1, p2, q1, q2)
        revenue = pe.get_revenue_impact()
        
        total_individual_revenue_before += revenue['initial_revenue']
        total_individual_revenue_after += revenue['new_revenue']
        
        print(f"{product:<20} Ed={pe.calculate():>6.2f}  "
              f"Revenue: ${revenue['initial_revenue']:>8,.0f} → ${revenue['new_revenue']:>8,.0f}")
    
    print(f"\nTotal individual revenue: "
          f"${total_individual_revenue_before:,.0f} → ${total_individual_revenue_after:,.0f}")
    print(f"Change: ${total_individual_revenue_after - total_individual_revenue_before:,.0f}")
    
    print("\n" + "=" * 70)
    print("\nBundled Suite (10% price increase):")
    print("-" * 70)
    
    pe_bundle = PriceElasticity(
        initial_price=120,  # Bundle of all three
        new_price=132,
        initial_quantity=1000,
        new_quantity=900
    )
    
    bundle_revenue = pe_bundle.get_revenue_impact()
    
    print(f"Office Suite Bundle  Ed={pe_bundle.calculate():>6.2f}  "
          f"Revenue: ${bundle_revenue['initial_revenue']:>8,.0f} → "
          f"${bundle_revenue['new_revenue']:>8,.0f}")
    print(f"Change: ${bundle_revenue['revenue_change']:,.0f}")
    
    print("\n" + "=" * 70)
    print("INSIGHT:")
    print("=" * 70)
    print("Bundles often have LESS ELASTIC demand because:")
    print("• Higher perceived value")
    print("• Fewer comparable alternatives")
    print("• Convenience factor")
    print("• Psychological pricing benefits")
    print("=" * 70)
    print("\n")


if __name__ == "__main__":
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "ADVANCED ELASTICITY EXAMPLES" + " " * 24 + "║")
    print("╚" + "═" * 68 + "╝")
    print("\n")
    
    revenue_maximization_example()
    input("Press Enter to continue...")
    
    segment_analysis_example()
    input("Press Enter to continue...")
    
    competitive_response_example()
    input("Press Enter to continue...")
    
    seasonal_elasticity_example()
    input("Press Enter to continue...")
    
    bundling_example()
    
    print("\nAdvanced examples complete!")
    print("These scenarios demonstrate how context affects elasticity.")
