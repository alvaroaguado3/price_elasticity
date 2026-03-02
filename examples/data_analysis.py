"""
Data analysis example using pandas and matplotlib.
Analyzes price elasticity from a dataset.
"""

import sys
sys.path.append('..')

import pandas as pd
import matplotlib.pyplot as plt
from elasticity import PriceElasticity


def load_and_analyze_data():
    """Load sample data and calculate elasticity for each product."""
    print("=" * 70)
    print("DATA ANALYSIS: PRICE ELASTICITY ACROSS PRODUCTS")
    print("=" * 70)
    print()
    
    # Load data
    df = pd.read_csv('../datasets/sample_price_data.csv')
    
    print("Sample Data:")
    print(df.head())
    print(f"\nTotal products analyzed: {len(df)}")
    print()
    
    # Calculate elasticity for each product
    elasticities = []
    types = []
    
    for _, row in df.iterrows():
        pe = PriceElasticity(
            row['Initial_Price'],
            row['New_Price'],
            row['Initial_Quantity'],
            row['New_Quantity']
        )
        elasticity = pe.calculate()
        elasticities.append(elasticity)
        types.append(pe.get_type())
    
    df['Elasticity'] = elasticities
    df['Elasticity_Type'] = types
    df['Abs_Elasticity'] = df['Elasticity'].abs()
    
    # Sort by absolute elasticity
    df_sorted = df.sort_values('Abs_Elasticity', ascending=False)
    
    print("\n" + "=" * 70)
    print("ELASTICITY RANKINGS (Most to Least Elastic)")
    print("=" * 70)
    print(f"\n{'Product':<25} {'Category':<15} {'Elasticity':<12} {'Type':<20}")
    print("-" * 70)
    
    for _, row in df_sorted.iterrows():
        print(f"{row['Product']:<25} {row['Category']:<15} "
              f"{row['Elasticity']:>10.2f}  {row['Elasticity_Type']:<20}")
    
    return df


def analyze_by_category(df):
    """Analyze average elasticity by product category."""
    print("\n" + "=" * 70)
    print("ELASTICITY BY CATEGORY")
    print("=" * 70)
    print()
    
    category_stats = df.groupby('Category').agg({
        'Abs_Elasticity': ['mean', 'min', 'max', 'count']
    }).round(2)
    
    category_stats.columns = ['Avg_Elasticity', 'Min', 'Max', 'Count']
    category_stats = category_stats.sort_values('Avg_Elasticity', ascending=False)
    
    print(category_stats)
    
    print("\n" + "=" * 70)
    print("INSIGHTS:")
    print("=" * 70)
    
    most_elastic = category_stats.index[0]
    least_elastic = category_stats.index[-1]
    
    print(f"\nMost elastic category: {most_elastic}")
    print(f"  → Consumers are very price-sensitive")
    print(f"  → Price increases will significantly reduce demand")
    print(f"  → Consider competitive pricing strategies")
    
    print(f"\nLeast elastic category: {least_elastic}")
    print(f"  → Consumers are less price-sensitive")
    print(f"  → Can sustain price increases without major volume loss")
    print(f"  → Focus on value and quality over price competition")
    
    return category_stats


def create_visualizations(df):
    """Create visualizations of elasticity data."""
    print("\n" + "=" * 70)
    print("CREATING VISUALIZATIONS...")
    print("=" * 70)
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Price Elasticity Analysis', fontsize=16, fontweight='bold')
    
    # 1. Elasticity distribution
    ax1 = axes[0, 0]
    df['Abs_Elasticity'].hist(bins=20, ax=ax1, color='steelblue', edgecolor='black')
    ax1.set_xlabel('Absolute Elasticity')
    ax1.set_ylabel('Frequency')
    ax1.set_title('Distribution of Price Elasticity')
    ax1.axvline(x=1, color='red', linestyle='--', linewidth=2, label='Unit Elastic')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Elasticity by category
    ax2 = axes[0, 1]
    category_means = df.groupby('Category')['Abs_Elasticity'].mean().sort_values()
    category_means.plot(kind='barh', ax=ax2, color='coral')
    ax2.set_xlabel('Average Absolute Elasticity')
    ax2.set_title('Elasticity by Product Category')
    ax2.grid(True, alpha=0.3, axis='x')
    
    # 3. Elasticity type pie chart
    ax3 = axes[1, 0]
    type_counts = df['Elasticity_Type'].value_counts()
    colors = {'Elastic': '#10b981', 'Inelastic': '#ef4444', 'Unit Elastic': '#f59e0b'}
    pie_colors = [colors.get(t, 'gray') for t in type_counts.index]
    ax3.pie(type_counts.values, labels=type_counts.index, autopct='%1.1f%%',
            colors=pie_colors, startangle=90)
    ax3.set_title('Distribution of Elasticity Types')
    
    # 4. Price change vs Quantity change scatter
    ax4 = axes[1, 1]
    df['Price_Change_%'] = ((df['New_Price'] - df['Initial_Price']) / df['Initial_Price'] * 100)
    df['Quantity_Change_%'] = ((df['New_Quantity'] - df['Initial_Quantity']) / df['Initial_Quantity'] * 100)
    
    scatter = ax4.scatter(df['Price_Change_%'], df['Quantity_Change_%'], 
                         c=df['Abs_Elasticity'], cmap='RdYlGn_r', 
                         s=100, alpha=0.6, edgecolors='black')
    ax4.set_xlabel('Price Change (%)')
    ax4.set_ylabel('Quantity Change (%)')
    ax4.set_title('Price vs Quantity Change')
    ax4.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax4.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
    ax4.grid(True, alpha=0.3)
    
    # Add colorbar
    cbar = plt.colorbar(scatter, ax=ax4)
    cbar.set_label('Absolute Elasticity')
    
    plt.tight_layout()
    
    # Save the figure
    output_path = '../visualizations/elasticity_analysis.png'
    try:
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"\nVisualizations saved to: {output_path}")
    except:
        print("\nNote: Could not save visualization file.")
        print("Displaying plots instead...")
    
    plt.show()
    
    print("Visualizations complete!")


def main():
    """Main analysis function."""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 18 + "DATA ANALYSIS EXAMPLE" + " " * 28 + "║")
    print("╚" + "═" * 68 + "╝")
    print("\n")
    
    try:
        # Load and analyze data
        df = load_and_analyze_data()
        
        # Analyze by category
        category_stats = analyze_by_category(df)
        
        # Create visualizations
        create_visualizations(df)
        
        print("\n" + "=" * 70)
        print("Analysis complete! Check the visualizations directory for charts.")
        print("=" * 70)
        
    except FileNotFoundError:
        print("\nError: Could not find data file.")
        print("Please ensure 'datasets/sample_price_data.csv' exists.")
    except Exception as e:
        print(f"\nError during analysis: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
