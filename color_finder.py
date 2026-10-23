import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
from sklearn.cluster import KMeans


def extract_colors():
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    try:
        # Open image
        image = Image.open(file_path).convert("RGB")

        # Display image
        preview = image.copy()
        preview.thumbnail((400, 300))

        photo = ImageTk.PhotoImage(preview)
        image_label.config(image=photo)
        image_label.image = photo

        # Resize image for faster processing
        small_image = image.copy()
        small_image.thumbnail((200, 200))

        # Convert image to NumPy array
        image_array = np.array(small_image)

        # Convert pixels into rows
        pixels = image_array.reshape(-1, 3)

        # Number of colors
        number_of_colors = 5

        # KMeans clustering
        kmeans = KMeans(
            n_clusters=number_of_colors,
            random_state=42,
            n_init=10
        )

        kmeans.fit(pixels)

        # Get dominant colors
        colors = kmeans.cluster_centers_.astype(int)

        # Count pixels in each cluster
        labels = kmeans.labels_
        counts = np.bincount(labels)

        # Sort colors by frequency
        sorted_indices = np.argsort(counts)[::-1]

        # Clear previous colors
        for widget in color_frame.winfo_children():
            widget.destroy()

        # Display colors
        for index in sorted_indices:
            color = colors[index]

            r, g, b = color

            hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)

            percentage = (counts[index] / len(labels)) * 100

            # Color preview
            color_box = tk.Label(
                color_frame,
                bg=hex_color,
                width=10,
                height=3
            )
            color_box.pack(side="left", padx=10)

            # Color information
            info = tk.Label(
                color_frame,
                text=f"{hex_color}\nRGB({r}, {g}, {b})\n{percentage:.1f}%",
                font=("Arial", 10)
            )
            info.pack(side="left", padx=(0, 15))

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Could not process image:\n{e}"
        )


# -----------------------------
# Tkinter Window
# -----------------------------

root = tk.Tk()
root.title("Image Color Extractor")
root.geometry("900x650")
root.configure(bg="#f2f2f2")

# Title
title = tk.Label(
    root,
    text="Image Color Extractor",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=20)

# Select image button
button = tk.Button(
    root,
    text="Select Image",
    command=extract_colors,
    font=("Arial", 14),
    bg="#2196F3",
    fg="white",
    padx=20,
    pady=10
)
button.pack(pady=10)

# Image preview
image_label = tk.Label(
    root,
    bg="white",
    width=400,
    height=300
)
image_label.pack(pady=20)

# Color results
color_title = tk.Label(
    root,
    text="Dominant Colors",
    font=("Arial", 18, "bold"),
    bg="#f2f2f2"
)
color_title.pack(pady=10)

color_frame = tk.Frame(
    root,
    bg="#f2f2f2"
)
color_frame.pack(pady=10)

# Start application
root.mainloop()
