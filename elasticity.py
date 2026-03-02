"""
Price Elasticity of Demand Calculator

This module provides classes and functions for calculating and analyzing
price elasticity of demand.
"""


class PriceElasticity:
    """
    Calculate and analyze price elasticity of demand.
    
    Attributes:
        initial_price (float): The original price point
        new_price (float): The new price point
        initial_quantity (float): The original quantity demanded
        new_quantity (float): The new quantity demanded
    """
    
    def __init__(self, initial_price, new_price, initial_quantity, new_quantity):
        """
        Initialize the PriceElasticity calculator.
        
        Args:
            initial_price (float): Original price
            new_price (float): New price
            initial_quantity (float): Original quantity demanded
            new_quantity (float): New quantity demanded
            
        Raises:
            ValueError: If any value is zero or negative
        """
        if any(val <= 0 for val in [initial_price, new_price, initial_quantity, new_quantity]):
            raise ValueError("All values must be positive and non-zero")
        
        self.initial_price = initial_price
        self.new_price = new_price
        self.initial_quantity = initial_quantity
        self.new_quantity = new_quantity
        
        self._elasticity = None
        self._price_change_pct = None
        self._quantity_change_pct = None
    
    def calculate(self, method='midpoint'):
        """
        Calculate price elasticity of demand.
        
        Args:
            method (str): Calculation method - 'simple' or 'midpoint' (default)
                         Midpoint method is more accurate for large changes
        
        Returns:
            float: Price elasticity of demand (negative value)
        """
        if method == 'simple':
            self._price_change_pct = (self.new_price - self.initial_price) / self.initial_price
            self._quantity_change_pct = (self.new_quantity - self.initial_quantity) / self.initial_quantity
        elif method == 'midpoint':
            avg_price = (self.initial_price + self.new_price) / 2
            avg_quantity = (self.initial_quantity + self.new_quantity) / 2
            self._price_change_pct = (self.new_price - self.initial_price) / avg_price
            self._quantity_change_pct = (self.new_quantity - self.initial_quantity) / avg_quantity
        else:
            raise ValueError("Method must be 'simple' or 'midpoint'")
        
        if self._price_change_pct == 0:
            raise ValueError("Price change cannot be zero")
        
        self._elasticity = self._quantity_change_pct / self._price_change_pct
        return self._elasticity
    
    def get_type(self):
        """
        Get the elasticity type classification.
        
        Returns:
            str: Classification of elasticity
        """
        if self._elasticity is None:
            self.calculate()
        
        abs_elasticity = abs(self._elasticity)
        
        if abs_elasticity == 0:
            return "Perfectly Inelastic"
        elif abs_elasticity < 1:
            return "Inelastic"
        elif abs_elasticity == 1:
            return "Unit Elastic"
        elif abs_elasticity > 1 and abs_elasticity != float('inf'):
            return "Elastic"
        else:
            return "Perfectly Elastic"
    
    def get_revenue_impact(self):
        """
        Analyze the impact on total revenue.
        
        Returns:
            dict: Revenue analysis including initial, new, and change
        """
        if self._elasticity is None:
            self.calculate()
        
        initial_revenue = self.initial_price * self.initial_quantity
        new_revenue = self.new_price * self.new_quantity
        revenue_change = new_revenue - initial_revenue
        revenue_change_pct = (revenue_change / initial_revenue) * 100
        
        return {
            'initial_revenue': initial_revenue,
            'new_revenue': new_revenue,
            'revenue_change': revenue_change,
            'revenue_change_percent': revenue_change_pct
        }
    
    def get_interpretation(self):
        """
        Get a detailed interpretation of the elasticity.
        
        Returns:
            str: Human-readable interpretation
        """
        if self._elasticity is None:
            self.calculate()
        
        elasticity_type = self.get_type()
        abs_elasticity = abs(self._elasticity)
        price_increased = self.new_price > self.initial_price
        
        interpretation = f"Elasticity Type: {elasticity_type} (Ed = {self._elasticity:.3f})\n\n"
        
        if elasticity_type == "Perfectly Inelastic":
            interpretation += "Demand is completely unresponsive to price changes."
        elif elasticity_type == "Inelastic":
            interpretation += f"A 1% price change leads to a {abs_elasticity:.2f}% change in quantity.\n"
            interpretation += "Demand is relatively unresponsive. "
            if price_increased:
                interpretation += "Price increases will increase total revenue."
            else:
                interpretation += "Price decreases will decrease total revenue."
        elif elasticity_type == "Unit Elastic":
            interpretation += "Price changes and quantity changes are proportional.\n"
            interpretation += "Total revenue remains constant with price changes."
        elif elasticity_type == "Elastic":
            interpretation += f"A 1% price change leads to a {abs_elasticity:.2f}% change in quantity.\n"
            interpretation += "Demand is very responsive. "
            if price_increased:
                interpretation += "Price increases will decrease total revenue."
            else:
                interpretation += "Price decreases will increase total revenue."
        else:
            interpretation += "Demand is infinitely responsive to price changes."
        
        return interpretation
    
    def __repr__(self):
        """String representation of the PriceElasticity object."""
        return (f"PriceElasticity(P1={self.initial_price}, P2={self.new_price}, "
                f"Q1={self.initial_quantity}, Q2={self.new_quantity})")
    
    def __str__(self):
        """Human-readable string representation."""
        if self._elasticity is None:
            self.calculate()
        return f"Price Elasticity: {self._elasticity:.3f} ({self.get_type()})"


def calculate_elasticity(p1, p2, q1, q2, method='midpoint'):
    """
    Convenience function to calculate price elasticity.
    
    Args:
        p1 (float): Initial price
        p2 (float): New price
        q1 (float): Initial quantity
        q2 (float): New quantity
        method (str): 'simple' or 'midpoint'
    
    Returns:
        float: Price elasticity of demand
    """
    pe = PriceElasticity(p1, p2, q1, q2)
    return pe.calculate(method=method)


def calculate_optimal_price(current_price, current_quantity, elasticity, cost_per_unit):
    """
    Calculate the profit-maximizing price given elasticity and costs.
    
    This uses the formula: P = (E / (E + 1)) * MC
    where E is elasticity and MC is marginal cost
    
    Args:
        current_price (float): Current price
        current_quantity (float): Current quantity sold
        elasticity (float): Price elasticity of demand
        cost_per_unit (float): Cost to produce one unit
    
    Returns:
        dict: Optimal price and related metrics
    """
    if elasticity >= -1:
        return {
            'optimal_price': None,
            'message': 'Demand is inelastic (|Ed| < 1). No profit-maximizing price exists in simple model.'
        }
    
    # Lerner Index formula rearranged for optimal pricing
    markup = -1 / elasticity
    optimal_price = cost_per_unit / (1 - markup)
    
    return {
        'optimal_price': optimal_price,
        'current_price': current_price,
        'price_change': optimal_price - current_price,
        'price_change_percent': ((optimal_price - current_price) / current_price) * 100,
        'markup_percent': markup * 100
    }


if __name__ == "__main__":
    # Example usage
    print("Price Elasticity Calculator Example\n")
    
    # Example 1: Coffee shop
    print("Example 1: Coffee Shop")
    print("-" * 40)
    pe1 = PriceElasticity(
        initial_price=4,
        new_price=5,
        initial_quantity=200,
        new_quantity=150
    )
    
    elasticity1 = pe1.calculate()
    print(f"Elasticity: {elasticity1:.3f}")
    print(f"Type: {pe1.get_type()}")
    print(f"\n{pe1.get_interpretation()}\n")
    
    revenue1 = pe1.get_revenue_impact()
    print(f"Initial Revenue: ${revenue1['initial_revenue']:.2f}")
    print(f"New Revenue: ${revenue1['new_revenue']:.2f}")
    print(f"Revenue Change: ${revenue1['revenue_change']:.2f} ({revenue1['revenue_change_percent']:.1f}%)\n")
    
    # Example 2: Luxury item
    print("\nExample 2: Luxury Watch")
    print("-" * 40)
    pe2 = PriceElasticity(
        initial_price=5000,
        new_price=5500,
        initial_quantity=50,
        new_quantity=30
    )
    
    elasticity2 = pe2.calculate()
    print(f"Elasticity: {elasticity2:.3f}")
    print(f"Type: {pe2.get_type()}")
    print(f"\n{pe2.get_interpretation()}\n")
    
    revenue2 = pe2.get_revenue_impact()
    print(f"Initial Revenue: ${revenue2['initial_revenue']:,.2f}")
    print(f"New Revenue: ${revenue2['new_revenue']:,.2f}")
    print(f"Revenue Change: ${revenue2['revenue_change']:,.2f} ({revenue2['revenue_change_percent']:.1f}%)")
