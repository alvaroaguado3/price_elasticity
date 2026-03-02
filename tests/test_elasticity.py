"""
Unit tests for the Price Elasticity calculator.
"""

import pytest
from elasticity import PriceElasticity, calculate_elasticity, calculate_optimal_price


class TestPriceElasticity:
    """Test cases for PriceElasticity class."""
    
    def test_basic_calculation_midpoint(self):
        """Test basic elasticity calculation using midpoint method."""
        pe = PriceElasticity(10, 12, 100, 80)
        elasticity = pe.calculate(method='midpoint')
        
        # Expected: ((80-100)/90) / ((12-10)/11) = -0.222 / 0.182 = -1.22
        assert abs(elasticity - (-1.22)) < 0.01
    
    def test_basic_calculation_simple(self):
        """Test basic elasticity calculation using simple method."""
        pe = PriceElasticity(10, 12, 100, 80)
        elasticity = pe.calculate(method='simple')
        
        # Expected: ((80-100)/100) / ((12-10)/10) = -0.2 / 0.2 = -1.0
        assert elasticity == -1.0
    
    def test_invalid_values(self):
        """Test that invalid values raise ValueError."""
        with pytest.raises(ValueError):
            PriceElasticity(0, 10, 100, 80)
        
        with pytest.raises(ValueError):
            PriceElasticity(10, -5, 100, 80)
        
        with pytest.raises(ValueError):
            PriceElasticity(10, 12, 0, 80)
    
    def test_elasticity_types(self):
        """Test classification of elasticity types."""
        # Perfectly inelastic
        pe1 = PriceElasticity(10, 12, 100, 100)
        pe1.calculate()
        assert pe1.get_type() == "Perfectly Inelastic"
        
        # Inelastic
        pe2 = PriceElasticity(10, 12, 100, 90)
        pe2.calculate()
        assert pe2.get_type() == "Inelastic"
        
        # Unit elastic (approximately)
        pe3 = PriceElasticity(10, 12, 100, 80)
        pe3.calculate()
        assert pe3.get_type() in ["Unit Elastic", "Elastic"]
        
        # Elastic
        pe4 = PriceElasticity(10, 12, 100, 50)
        pe4.calculate()
        assert pe4.get_type() == "Elastic"
    
    def test_revenue_impact(self):
        """Test revenue impact calculation."""
        pe = PriceElasticity(10, 12, 100, 80)
        pe.calculate()
        revenue = pe.get_revenue_impact()
        
        assert revenue['initial_revenue'] == 1000
        assert revenue['new_revenue'] == 960
        assert revenue['revenue_change'] == -40
        assert abs(revenue['revenue_change_percent'] - (-4.0)) < 0.01
    
    def test_interpretation(self):
        """Test that interpretation is generated."""
        pe = PriceElasticity(10, 12, 100, 80)
        pe.calculate()
        interpretation = pe.get_interpretation()
        
        assert isinstance(interpretation, str)
        assert len(interpretation) > 0
        assert "Elasticity Type" in interpretation
    
    def test_string_representations(self):
        """Test string representations."""
        pe = PriceElasticity(10, 12, 100, 80)
        
        repr_str = repr(pe)
        assert "PriceElasticity" in repr_str
        assert "10" in repr_str
        
        pe.calculate()
        str_str = str(pe)
        assert "Price Elasticity" in str_str


class TestConvenienceFunctions:
    """Test convenience functions."""
    
    def test_calculate_elasticity_function(self):
        """Test the convenience calculate_elasticity function."""
        elasticity = calculate_elasticity(10, 12, 100, 80, method='midpoint')
        assert abs(elasticity - (-1.22)) < 0.01
    
    def test_optimal_price_calculation(self):
        """Test optimal price calculation."""
        result = calculate_optimal_price(
            current_price=10,
            current_quantity=100,
            elasticity=-2.0,
            cost_per_unit=5
        )
        
        assert result['optimal_price'] is not None
        assert result['optimal_price'] > result['current_price']
    
    def test_optimal_price_inelastic(self):
        """Test that inelastic demand returns no optimal price."""
        result = calculate_optimal_price(
            current_price=10,
            current_quantity=100,
            elasticity=-0.5,  # Inelastic
            cost_per_unit=5
        )
        
        assert result['optimal_price'] is None
        assert 'message' in result


class TestEdgeCases:
    """Test edge cases and special scenarios."""
    
    def test_price_decrease(self):
        """Test with price decrease instead of increase."""
        pe = PriceElasticity(12, 10, 80, 100)
        elasticity = pe.calculate()
        
        # Elasticity should still be negative
        assert elasticity < 0
    
    def test_large_price_change(self):
        """Test with large price change."""
        pe = PriceElasticity(10, 30, 1000, 200)
        elasticity = pe.calculate()
        
        # Should be very elastic
        assert abs(elasticity) > 1
    
    def test_very_small_quantities(self):
        """Test with very small quantities."""
        pe = PriceElasticity(100, 120, 5, 3)
        elasticity = pe.calculate()
        
        assert isinstance(elasticity, float)
        assert elasticity < 0
    
    def test_symmetry_midpoint_method(self):
        """Test that midpoint method is symmetric."""
        # A to B
        pe1 = PriceElasticity(10, 12, 100, 80)
        e1 = pe1.calculate(method='midpoint')
        
        # B to A
        pe2 = PriceElasticity(12, 10, 80, 100)
        e2 = pe2.calculate(method='midpoint')
        
        # Should be equal
        assert abs(e1 - e2) < 0.001


class TestRealWorldScenarios:
    """Test with real-world scenarios."""
    
    def test_coffee_shop_example(self):
        """Test coffee shop scenario from examples."""
        pe = PriceElasticity(4, 5, 200, 150)
        elasticity = pe.calculate()
        
        # Should be approximately unit elastic
        assert abs(abs(elasticity) - 1.0) < 0.3
    
    def test_luxury_good_example(self):
        """Test luxury good scenario."""
        pe = PriceElasticity(5000, 5500, 50, 30)
        elasticity = pe.calculate()
        
        # Should be elastic
        assert abs(elasticity) > 1
        assert pe.get_type() == "Elastic"
    
    def test_necessity_good_example(self):
        """Test necessity good scenario."""
        pe = PriceElasticity(1.00, 1.20, 1000, 980)
        elasticity = pe.calculate()
        
        # Should be inelastic
        assert abs(elasticity) < 1
        assert pe.get_type() == "Inelastic"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
