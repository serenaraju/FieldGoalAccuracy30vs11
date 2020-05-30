
import requests
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.patches import Circle, Rectangle, Arc
import PIL
from PIL import Image

steph = pd.read_table('StephShots.txt',sep = '\n',names = ['div'])

#StephShots.txt was made into a txt file from 'https://www.basketball-reference.com/players/c/curryst01/shooting/2019'

#Finding x and y coordinates of Steph's Shots

steph['LOC_Y'] = steph['div'].str.extract(r'top:(.*)px;l')
steph['LOC_X'] = steph['div'].str.extract(r'left:(.*)px')

#Extracting only the shots that were made; Missed shots are removed (Cleaning data)

steph['Make/Miss'] = steph['div'].str.extract(r'class="tooltip (.*)"')
steph_made = steph[steph['Make/Miss']=='make']

kyrie = pd.read_table('KyrieShots.txt',sep = '\n',names = ['div'])

#KyrieShots.txt was made into a txt file from https://www.basketball-reference.com/players/i/irvinky01/shooting/2019


#Finding x and y coordinates of Kyrie's Shots

kyrie['LOC_Y'] = kyrie['div'].str.extract(r'top:(.*)px;l')
kyrie['LOC_X'] = kyrie['div'].str.extract(r'left:(.*)px')

#Extracting only the shots that were made; Missed shots are removed (Cleaning data)

kyrie['Make/Miss'] = kyrie['div'].str.extract(r'class="tooltip (.*)"')
kyrie_made = kyrie[kyrie['Make/Miss']=='make']

#'http://savvastjortjoglou.com/nba-shot-sharts.html' The draw_court() method is 
# a modified version of Savvas Tjortjoglou's draw_court method 
# on his blog with changes made according to my dataset

def draw_court(ax=None, color='black', lw=2, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()

    # Create the various parts of an NBA basketball court

    # Create the basketball hoop

    hoop = Circle((250, 40), radius=7.5, linewidth=lw, color=color, fill=False)

    # Create backboard
    backboard = Rectangle((220, 32.5), 60, 1, linewidth=lw, color=color)

    # The paint
    outer_box = Rectangle((170, 30), 160, 190, linewidth=lw, color=color,
                          fill=False)
    inner_box = Rectangle((190, 30), 120, 190, linewidth=lw, color=color,
                          fill=False)

    # Create free throw top arc
    top_free_throw = Arc((251, 215), 120, 120, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((251, 215), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')

    restricted = Arc((250, 50), 80, 80, theta1=0, theta2=180, linewidth=lw,color=color)

    # Three point line

    corner_three_a = Rectangle((30, 0), 0, 140, linewidth=lw, color=color)
    corner_three_b = Rectangle((470, 0), 0, 140, linewidth=lw, color=color)

    # 3pt arc - center of arc will be the hoop
    three_arc = Arc((250, 50), 475, 475, theta1=22, theta2=158, linewidth=lw, color=color)

    # Center Court
    center_outer_arc = Arc((250, 470), 120, 120, theta1=180, theta2=0, linewidth=lw, color=color)
    center_inner_arc = Arc((250, 470), 40, 40, theta1=180, theta2=0, linewidth=lw, color=color)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((0, 47.5-6.5), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)

    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)

    return ax


#Plotting Steph's Chart

steph_plot = sns.jointplot(steph_made.LOC_X.values.astype(int) ,steph_made.LOC_Y.values.astype(int), kind='hex', color = 'blue',space = 0,joint_kws = dict(gridsize=15));

#Removing ticks and labels for Steph

ax_2 = steph_plot.ax_joint
ax_2.set_ylim(top = 470)
ax_2.tick_params(labelbottom = False,labelleft = False,top = False, bottom = False,left =False, right = False)
ax_4 = steph_plot.ax_marg_x
ax_4.tick_params(labelbottom = False,labelleft = False,top = False, bottom = False,left =False, right = False)
ax_6 = steph_plot.ax_marg_y
ax_6.tick_params(labelbottom = False,labelleft = False,top = False, bottom = False,left =False, right = False)

#Removing Spines

sns.despine(bottom = True, top = True, left =True, right =True,trim = True)

steph_plot.fig.subplots_adjust(top = 0.87)
cbar_ax = steph_plot.fig.add_axes([.95, .25, .05, .4])  # x, y, width, height
plt.colorbar(cax=cbar_ax)
ax_6.text(180,420,'Higher \nAcuuracy',
        fontsize=10)
ax_6.text(180, 100,'Lower \nAcuuracy',
        fontsize=10)
steph_plot.fig.suptitle('Stephen Curry Field Goal Accuracy \nOverview 2017-2019' ,fontsize = 20)
draw_court(ax_2)

plt.savefig('steph_plot.png')

plt.show()

#Plotting Kyrie's Chart

kyrie_plot = sns.jointplot(kyrie_made.LOC_X.values.astype(int) ,kyrie_made.LOC_Y.values.astype(int), kind='hex', color = 'green',space = 0,joint_kws = dict(gridsize=15));

#Removing ticks and labels for Kyrie

ax_1 = kyrie_plot.ax_joint
ax_1.tick_params(labelbottom = False,labelleft = False,length = 0)
ax_1.set_ylim(top = 470)
ax_3 = kyrie_plot.ax_marg_x
ax_3.tick_params(labelbottom = False,labelleft = False,top = False, bottom = False,left =False, right = False)
ax_5 = kyrie_plot.ax_marg_y
ax_5.tick_params(labelbottom = False,labelleft = False,top = False, bottom = False,left =False, right = False)

#Removing Spines
sns.despine(bottom = True, top = True, left =True, right =True,trim = True)

draw_court(ax_1)

#Colorbar for Kyrie's Shots
kyrie_plot.fig.subplots_adjust(top = 0.87)
cbar_ax = kyrie_plot.fig.add_axes([.95, .25, .05, .4])  # x, y, width, height
plt.colorbar(cax=cbar_ax)
ax_5.text(200,420,'Higher \nAcuuracy',
        fontsize=10)
ax_5.text(200,95,'Lower \nAcuuracy',
        fontsize=10)

#Title for Kyrie's Plot

kyrie_plot.fig.suptitle('Kyrie Irving Field Goal Accuracy \nOverview 2017-2019',fontsize = 20)
plt.savefig('kyrie_plot.png')
plt.show()

#Comparison Chart (Concatenating the two images to visualize better)

#Learnt how to concatenate images from 'https://www.codespeedy.com/merge-two-images-in-python/'

images = [Image.open(x) for x in ['steph_plot.png', 'kyrie_plot.png']]
total_width = 0
max_height = 0
# find the width and height of the final image
for img in images:
    total_width += img.size[0]
    max_height = max(max_height, img.size[1])

new_img = Image.new('RGB', (total_width, max_height))
# Write the contents of the new image
current_width = 0
for img in images:
  new_img.paste(img, (current_width,0))
  current_width += img.size[0]
# Save the image
new_img.save('Compare.jpg')

#Made using a lot of techniques learnt from the 
#Applied Data Science with Python Specialization