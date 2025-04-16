import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

class StackVisualizer:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        return None

    def get_stack(self):
        return self.stack

def update_stack_plot(frame, stack, bar_rects):
    # Randomly push or pop
    if random.choice([True, False]):
        stack.push(random.randint(1, 100))
    else:
        stack.pop()

    values = stack.get_stack()
    for rect, h in zip(bar_rects, values + [0]*(len(bar_rects) - len(values))):
        rect.set_height(h)
    return bar_rects

def visualize_stack():
    stack = StackVisualizer()

    fig, ax = plt.subplots()
    bar_rects = ax.bar(range(10), [0]*10)
    ax.set_ylim(0, 120)
    ax.set_title("Stack Visualizer (Push/Pop Randomly)")

    ani = animation.FuncAnimation(
        fig, update_stack_plot, fargs=(stack, bar_rects), interval=1000, blit=False
    )

    plt.show()

if __name__ == "__main__":
    visualize_stack()
