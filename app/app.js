// Price Elasticity Calculator Application

// Examples data
const examples = {
    coffee: {
        initialPrice: 4,
        newPrice: 5,
        initialQuantity: 200,
        newQuantity: 150
    },
    airline: {
        initialPrice: 300,
        newPrice: 270,
        initialQuantity: 100,
        newQuantity: 130
    },
    salt: {
        initialPrice: 1,
        newPrice: 1.20,
        initialQuantity: 1000,
        newQuantity: 980
    },
    luxury: {
        initialPrice: 5000,
        newPrice: 5500,
        initialQuantity: 50,
        newQuantity: 30
    }
};

// Chart instance
let demandChart = null;

// Initialize event listeners
document.addEventListener('DOMContentLoaded', function() {
    // Calculate button
    document.getElementById('calculateBtn').addEventListener('click', calculateElasticity);

    // Example buttons
    document.querySelectorAll('.example-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            loadExample(this.dataset.example);
        });
    });

    // Input change listeners for real-time updates
    const inputs = ['initialPrice', 'newPrice', 'initialQuantity', 'newQuantity'];
    inputs.forEach(id => {
        document.getElementById(id).addEventListener('input', function() {
            // Hide results when inputs change
            document.getElementById('results').classList.add('hidden');
        });
    });

    // Initialize chart
    initChart();
});

function loadExample(exampleName) {
    const example = examples[exampleName];
    
    document.getElementById('initialPrice').value = example.initialPrice;
    document.getElementById('newPrice').value = example.newPrice;
    document.getElementById('initialQuantity').value = example.initialQuantity;
    document.getElementById('newQuantity').value = example.newQuantity;
    
    // Automatically calculate
    calculateElasticity();
}

function calculateElasticity() {
    // Get input values
    const P1 = parseFloat(document.getElementById('initialPrice').value);
    const P2 = parseFloat(document.getElementById('newPrice').value);
    const Q1 = parseFloat(document.getElementById('initialQuantity').value);
    const Q2 = parseFloat(document.getElementById('newQuantity').value);

    // Validate inputs
    if (isNaN(P1) || isNaN(P2) || isNaN(Q1) || isNaN(Q2)) {
        alert('Please enter valid numbers for all fields');
        return;
    }

    if (P1 <= 0 || P2 <= 0 || Q1 <= 0 || Q2 <= 0) {
        alert('All values must be greater than zero');
        return;
    }

    // Calculate percentage changes
    const priceChange = ((P2 - P1) / P1) * 100;
    const quantityChange = ((Q2 - Q1) / Q1) * 100;

    // Calculate elasticity using midpoint method for accuracy
    const avgPrice = (P1 + P2) / 2;
    const avgQuantity = (Q1 + Q2) / 2;
    const elasticity = ((Q2 - Q1) / avgQuantity) / ((P2 - P1) / avgPrice);

    // Get elasticity type and interpretation
    const { type, className, interpretation, businessInsight } = classifyElasticity(elasticity, priceChange);

    // Display results
    displayResults(priceChange, quantityChange, elasticity, type, className, interpretation, businessInsight);

    // Update chart
    updateChart(P1, P2, Q1, Q2, elasticity);
}

function classifyElasticity(elasticity, priceChange) {
    const absElasticity = Math.abs(elasticity);
    let type, className, interpretation, businessInsight;

    if (absElasticity === 0) {
        type = 'Perfectly Inelastic';
        className = 'perfectly-inelastic';
        interpretation = 'Demand is completely unresponsive to price changes. Consumers will buy the same quantity regardless of price. This is rare and typically only seen with essential goods like life-saving medications.';
        businessInsight = 'You have complete pricing power. Price increases will directly increase revenue without affecting sales volume.';
    } else if (absElasticity < 1) {
        type = 'Inelastic';
        className = 'inelastic';
        interpretation = `Demand is relatively unresponsive to price changes. A 1% change in price leads to a ${absElasticity.toFixed(2)}% change in quantity demanded. The good is likely a necessity or has few substitutes.`;
        if (priceChange > 0) {
            businessInsight = 'A price increase will increase total revenue. Consumers need this product and will continue buying despite higher prices.';
        } else {
            businessInsight = 'A price decrease will decrease total revenue. Consider raising prices to maximize revenue.';
        }
    } else if (absElasticity === 1) {
        type = 'Unit Elastic';
        className = 'unit-elastic';
        interpretation = 'Demand changes proportionally with price. A 1% change in price leads to exactly a 1% change in quantity demanded. Revenue remains constant regardless of price changes.';
        businessInsight = 'You are at the revenue-maximizing price point. Price changes in either direction will not affect total revenue, but may affect market share and competitive position.';
    } else if (absElasticity > 1 && absElasticity < Infinity) {
        type = 'Elastic';
        className = 'elastic';
        interpretation = `Demand is very responsive to price changes. A 1% change in price leads to a ${absElasticity.toFixed(2)}% change in quantity demanded. The good likely has many substitutes or is a luxury item.`;
        if (priceChange > 0) {
            businessInsight = 'A price increase will decrease total revenue. Consider lowering prices to increase sales volume and revenue.';
        } else {
            businessInsight = 'A price decrease will increase total revenue. Lower prices stimulate significant demand growth.';
        }
    } else {
        type = 'Perfectly Elastic';
        className = 'perfectly-elastic';
        interpretation = 'Demand is infinitely responsive to price changes. Any price increase will result in zero sales. This occurs in perfectly competitive markets where products are identical.';
        businessInsight = 'You must match competitor prices exactly. Any price above market price will eliminate all sales.';
    }

    return { type, className, interpretation, businessInsight };
}

function displayResults(priceChange, quantityChange, elasticity, type, className, interpretation, businessInsight) {
    // Show results section
    document.getElementById('results').classList.remove('hidden');

    // Update values
    document.getElementById('priceChange').textContent = `${priceChange > 0 ? '+' : ''}${priceChange.toFixed(2)}%`;
    document.getElementById('quantityChange').textContent = `${quantityChange > 0 ? '+' : ''}${quantityChange.toFixed(2)}%`;
    document.getElementById('elasticity').textContent = elasticity.toFixed(3);
    
    // Update elasticity type with badge
    const typeElement = document.getElementById('elasticityType');
    typeElement.textContent = type;
    typeElement.className = `value badge ${className}`;
    
    // Update interpretation
    document.getElementById('interpretation').textContent = interpretation;
    document.getElementById('businessInsight').textContent = businessInsight;

    // Scroll to results
    document.getElementById('results').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function initChart() {
    const ctx = document.getElementById('demandChart').getContext('2d');
    
    demandChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Demand Curve',
                data: [],
                borderColor: 'rgba(37, 99, 235, 0.8)',
                backgroundColor: 'rgba(37, 99, 235, 0.1)',
                showLine: true,
                tension: 0.4,
                borderWidth: 3
            }, {
                label: 'Original Point',
                data: [],
                backgroundColor: 'rgba(37, 99, 235, 1)',
                borderColor: '#ffffff',
                borderWidth: 2,
                pointRadius: 10,
                pointHoverRadius: 12
            }, {
                label: 'New Point',
                data: [],
                backgroundColor: 'rgba(239, 68, 68, 1)',
                borderColor: '#ffffff',
                borderWidth: 2,
                pointRadius: 10,
                pointHoverRadius: 12
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `Price: $${context.parsed.x}, Quantity: ${context.parsed.y}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    type: 'linear',
                    position: 'bottom',
                    title: {
                        display: true,
                        text: 'Quantity',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Price ($)',
                        font: {
                            size: 14,
                            weight: 'bold'
                        }
                    },
                    grid: {
                        color: 'rgba(0, 0, 0, 0.05)'
                    }
                }
            }
        }
    });
}

function updateChart(P1, P2, Q1, Q2, elasticity) {
    // Generate demand curve points
    const curvePoints = generateDemandCurve(P1, P2, Q1, Q2, elasticity);
    
    // Update chart data
    demandChart.data.datasets[0].data = curvePoints;
    demandChart.data.datasets[1].data = [{ x: Q1, y: P1 }];
    demandChart.data.datasets[2].data = [{ x: Q2, y: P2 }];
    
    // Update chart scales
    const minQ = Math.min(Q1, Q2);
    const maxQ = Math.max(Q1, Q2);
    const minP = Math.min(P1, P2);
    const maxP = Math.max(P1, P2);
    
    demandChart.options.scales.x.min = Math.max(0, minQ * 0.5);
    demandChart.options.scales.x.max = maxQ * 1.5;
    demandChart.options.scales.y.min = Math.max(0, minP * 0.5);
    demandChart.options.scales.y.max = maxP * 1.5;
    
    demandChart.update();
}

function generateDemandCurve(P1, P2, Q1, Q2, elasticity) {
    // Generate a smooth demand curve through both points
    const points = [];
    const numPoints = 50;
    
    const minQ = Math.min(Q1, Q2) * 0.5;
    const maxQ = Math.max(Q1, Q2) * 1.5;
    
    // Calculate curve parameters using the two points
    // Using a power function: P = a * Q^b where b relates to elasticity
    const a = P1 * Math.pow(Q1, -1/elasticity);
    
    for (let i = 0; i < numPoints; i++) {
        const q = minQ + (maxQ - minQ) * (i / (numPoints - 1));
        const p = a * Math.pow(q, -1/Math.max(0.1, Math.abs(elasticity)));
        
        if (p > 0 && !isNaN(p) && isFinite(p)) {
            points.push({ x: q, y: p });
        }
    }
    
    // Sort points by quantity for proper line drawing
    points.sort((a, b) => a.x - b.x);
    
    return points;
}
