import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_hickory_venn_diagram():

    fig, ax = plt.subplots(figsize=(10, 10))

    fig.patch.set_facecolor('#E6E6E6')
    ax.set_facecolor('#E6E6E6')

    circle_settings = [
        {'center': (0.35, 0.6), 'radius': 0.35},  # Top Left
        {'center': (0.65, 0.6), 'radius': 0.35},  # Top Right
        {'center': (0.5, 0.35), 'radius': 0.35}   # Bottom
    ]

    for circle in circle_settings:
        c = patches.Circle(
            circle['center'],
            circle['radius'],
            linewidth=6,
            edgecolor='black',
            facecolor='none'
        )
        ax.add_patch(c)

    text_elements = [
        (0.20, 0.69, 'E', 'black', 35),
        (0.16, 0.60, 'F', 'black', 35),
        (0.28, 0.55, 'H', 'blue', 35),
        (0.24, 0.76, 'L', 'black', 35),

        (0.79, 0.71, 'Q', 'black', 35),
        (0.83, 0.62, 'D', 'green', 35),
        (0.72, 0.56, 'G', 'black', 35),
        (0.76, 0.79, '3', 'black', 35),

        (0.50, 0.09, 'α', 'black', 40),
        (0.40, 0.14, 'β', 'black', 40),
        (0.60, 0.19, 'λ', 'black', 40),
        (0.47, 0.24, 'π', 'green', 40),

        (0.53, 0.74, 'P', 'black', 35),
        (0.47, 0.64, '5', 'red', 35),
        (0.50, 0.55, 'R', 'black', 35),

        (0.31, 0.41, 'Δ', 'black', 40),
        (0.36, 0.29, 'Σ', 'black', 40),
        (0.26, 0.34, 'Ξ', 'red', 40),

        (0.69, 0.42, 'θ', 'black', 40),
        (0.62, 0.29, 'ρ', 'red', 40),
        (0.76, 0.36, 'ο', 'green', 40),

        (0.50, 0.45, '!', 'black', 45)
    ]

    for x, y, char, color, size in text_elements:
        ax.text(
            x, y, char,
            color=color,
            fontsize=size,
            ha='center',
            va='center',
            fontfamily='serif',
            fontweight='bold'
        )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    create_hickory_venn_diagram()
