import matplotlib.pyplot as plt

# Data to plot
sizes_1 = [444, 111, 500, 666]
labels_1 = ['Category 1\n'+str("{0:.2f}".format(100*sizes_1[0]/sum(sizes_1)))+'%',
            'Category 2\n'+str("{0:.2f}".format(100*sizes_1[1]/sum(sizes_1)))+'%',
            'Category 3\n'+str("{0:.2f}".format(100*sizes_1[2]/sum(sizes_1)))+'%',
            'Category 4\n'+str("{0:.2f}".format(100*sizes_1[3]/sum(sizes_1)))+'%']
sizes_2 = [444, 111, 500, 400, 266]
which_subsection = 3
labels_2 = ['','','',
            'Category 4a\n'+str("{0:.2f}".format(100*sizes_2[which_subsection]/sum(sizes_1)))+'%',
            '']
colors_1 = ['#ff0000', '#00ff00', '#0000ff', '#ffff00']
colors_2 = ['#ffff00']

# Plot
m = plt.pie(sizes_1, labels=labels_1, colors=colors_1, startangle=90, radius=2)
n = plt.pie(sizes_2, labels=labels_2, colors=colors_2, startangle=90, radius=2)

# Transparency
for i in range(len(n[0])):
    n[0][i].set_alpha(0.0)
n[0][which_subsection].set_hatch('/')
n[0][which_subsection].set_alpha(1.0)

# Outline/Border
for i in range(len(m[0])):
    m[0][i].set_edgecolor('k')
n[0][which_subsection].set_edgecolor('k')

# Draw circle
centre_circle = plt.Circle((0, 0), 0.2, color='black', fc='white', linewidth=1)
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.tight_layout()
plt.show()