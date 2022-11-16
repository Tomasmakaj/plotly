# Rolling the Die
# Before creating a visualization base on the Die class, lets roll a D6 print the results and check that the results look reasonable:

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)


# Analyzing the Results

# We will analyze the results of rolling on D6 by counting how many times we roll each number

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Because we no longer printing the results we can increates the number of simulated rolls to 1000.
# To analyze the rolls we create the empty lists of frequencies to store the number of times each value is rolled.
# We loop through all the possible values (1 through 6)
# And count how many times each number appears in results and then append this value to the frequencies list.


# Making a Histogram
# With a list of frequenices, we can make a histogram of the results. A histogram is a bar chart showing how often certain results occur

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6
die = Die()

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
# Visualize the results in histogram
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')
