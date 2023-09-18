import matplotlib.pyplot as plt

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]

# Plotting a line graph
plt.plot(year, pop)

# Plotting a scatter graph
plt.scatter(year, pop)

# Labels and title
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population Growth Over Time')

# Display the plot
plt.show()