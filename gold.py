import matplotlib.pyplot as plt
import numpy as np

# Data for Companies (Indian & Foreign)
companies = [
    'Titan Company (India)', 'Muthoot Finance (India)', 'Shree Ganesh Gold (India)', 'Hindustan Zinc (India)',
    'Barrick Gold (Canada)', 'Newmont Corporation (USA)', 'AngloGold Ashanti (South Africa)', 'SPDR Gold Trust (USA)'
]

investment_focus = ['Jewelry', 'Gold Loans', 'Gold Refining', 'Gold Mining', 'Gold Mining', 'Gold Mining', 'Gold Mining', 'Gold ETF']
current_holdings = ['Significant', 'Significant', 'Significant', 'Substantial', 'Substantial', 'Significant', 'Substantial', '100% ETF']
investment_years = [1990, 1997, 2000, 2000, 1983, 1921, 1998, 2004]
initial_investments = [5000000, 3000000, 4000000, 2500000, 10000000, 8000000, 9000000, 15000000]
buy_sell_activity = ['Ongoing', 'Ongoing', 'Ongoing', 'Ongoing', 'Ongoing', 'Ongoing', 'Ongoing', 'Daily']

gold_price_2015 = 25000
gold_price_2024 = 60000
growth_rate = gold_price_2024 / gold_price_2015

# Calculate the current value of the investments based on gold price growth
current_values = [investment * growth_rate for investment in initial_investments]

# Convert "Current Holdings" to numerical values for visualization
holding_values = {'Significant': 3, 'Substantial': 2, '100% ETF': 4}
holding_data = [holding_values[holding] for holding in current_holdings]

# Create a subplot grid
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
(ax1, ax2), (ax3, ax4) = axs

# Bar Chart: Number of Companies and their Holdings with Investment Amounts
ax1.barh(companies, holding_data, color='gold')

# Adding labels and title
ax1.set_xlabel('Gold Holdings Level')
ax1.set_ylabel('Companies')
ax1.set_title('Gold Investment by Indian & Foreign Companies')
ax1.set_yticks(np.arange(len(companies)))
ax1.set_yticklabels(companies)
ax1.set_xticks([1, 2, 3, 4])
ax1.set_xticklabels(["Substantial", "Significant", "100% ETF", "Ongoing"])
ax1.grid(True)

# Adding Investment Years and Current Investment Values as text on the chart
for i, (year, holding, initial, current) in enumerate(zip(investment_years, holding_data, initial_investments, current_values)):
    ax1.text(holding + 0.1, i, f"Invested: {year}\nInitial: ₹{initial:,}\nCurrent: ₹{current:,.2f}", va='center', ha='left', fontsize=8, bbox=dict(facecolor='white', alpha=0.7))

# Pie Chart: Focus of Investments
investment_focus_counts = {focus: investment_focus.count(focus) for focus in set(investment_focus)}
ax2.pie(investment_focus_counts.values(), labels=investment_focus_counts.keys(), autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
ax2.set_title('Investment Focus Distribution by Company')

# Scatter Plot: Showing Investment Growth (Initial vs. Current Value)
ax3.scatter(companies, initial_investments, color='blue', label='Initial Investment', s=100)
ax3.scatter(companies, current_values, color='green', label='Current Value', s=100)
ax3.plot(companies, initial_investments, linestyle='--', color='blue', alpha=0.6)
ax3.plot(companies, current_values, linestyle='--', color='green', alpha=0.6)

# Adding Labels and Title for Scatter Plot
ax3.set_title('Investment Growth (Initial vs Current Value)')
ax3.set_ylabel('Investment Amount (INR)')
ax3.set_xticks(np.arange(len(companies)))
ax3.set_xticklabels(companies, rotation=45, ha='right')
ax3.legend()

# Line Chart: Show the fluctuation in gold price over time
years = np.arange(2015, 2025)
gold_prices = np.linspace(gold_price_2015, gold_price_2024, len(years))

ax4.plot(years, gold_prices, marker='o', color='gold')
ax4.set_title('Fluctuations in Gold Price (2015 - 2024)')
ax4.set_xlabel('Year')
ax4.set_ylabel('Gold Price (INR per gram)')
ax4.grid(True)

# Show the plots with tight layout
plt.tight_layout()
plt.show()
