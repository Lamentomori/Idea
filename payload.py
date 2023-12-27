# Code Created by Chat GPT did not waste my time on this.
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML
fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
text = ax.text(0.5, 0.5, '', ha='center', va='center', fontsize=20, color='red')
def update(frame):
    warning_text = "YOU COULD'VE BEEN HACKED!!!"
    text.set_text(warning_text[:frame])
    return text,
ani = animation.FuncAnimation(fig, update, frames=len("YOU COULD'VE BEEN HACKED!!!") + 1, interval=150)
HTML(ani.to_jshtml())
