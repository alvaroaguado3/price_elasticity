# Price Elasticity Test Suite

This directory contains unit tests for the price elasticity calculator.

## Running Tests

### Run all tests:
```bash
pytest
```

### Run with coverage report:
```bash
pytest --cov=elasticity --cov-report=html
```

### Run specific test file:
```bash
pytest tests/test_elasticity.py
```

### Run with verbose output:
```bash
pytest -v
```

## Test Structure

- `test_elasticity.py` - Main test suite for the PriceElasticity class
  - `TestPriceElasticity` - Basic functionality tests
  - `TestConvenienceFunctions` - Tests for helper functions
  - `TestEdgeCases` - Edge cases and boundary conditions
  - `TestRealWorldScenarios` - Real-world example validation

## Adding New Tests

When adding new functionality:
1. Write tests first (TDD approach)
2. Ensure tests cover normal cases, edge cases, and error conditions
3. Aim for >80% code coverage
4. Use descriptive test names

Example:
```python
def test_new_feature(self):
    """Test description of what this validates."""
    # Arrange
    pe = PriceElasticity(10, 12, 100, 80)
    
    # Act
    result = pe.new_feature()
    
    # Assert
    assert result == expected_value
```
