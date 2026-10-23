# Image Color Extractor

A graphical desktop application built with Python, **Tkinter**, **Pillow**, and **scikit-learn** that extracts and displays the top dominant colors from any given image using K-Means clustering.

---

## 🎨 Features

* **Image File Support**: Accepts common image formats including `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.webp`.
* **Visual Preview**: Displays a resized thumbnail preview of the selected image in the main window.
* **K-Means Color Extraction**: Uses machine learning (`scikit-learn`) to cluster image pixels into 5 dominant colors.
* **Color Details**: Displays for each dominant color:
  * Colored preview box
  * Hexadecimal code (e.g., `#FF5733`)
  * RGB value format (e.g., `RGB(255, 87, 51)`)
  * Percentage coverage in the image
* **Optimized Performance**: Automatically resizes images before applying K-Means clustering to ensure quick processing times without sacrificing accuracy.

---

## 🛠️ Prerequisites

Ensure you have Python **3.8+** installed on your system. 

### Dependencies

Install the required Python packages using `pip`:

```bash
pip install pillow numpy scikit-learn
```

> **Note:** `tkinter` comes pre-installed with standard Python distributions on Windows and macOS. Linux users may need to install it separately:
> ```bash
> sudo apt-get install python3-tk
> ```

---

## 🚀 Usage

1. Save the Python script (e.g., `color_extractor.py`).
2. Run the script from your terminal or command prompt:

   ```bash
   python color_extractor.py
   ```

3. Click the **"Select Image"** button.
4. Choose an image file from your system.
5. View the thumbnail preview and the top 5 dominant colors sorted by frequency!

---

## ⚙️ How It Works

1. **Image Loading & Downscaling**: The uploaded image is downsampled to a maximum resolution of $200 \times 200$ pixels using PIL thumbnail processing. This significantly lowers computational load while preserving the overall color profile.
2. **Pixel Flattening**: Image data is reshaped into a 2D array of RGB values ($N \times 3$).
3. **K-Means Clustering**: `KMeans(n_clusters=5)` clusters similar colors together in RGB color space.
4. **Color Distribution Calculation**: Cluster sizes are evaluated via `np.bincount` to determine the percentage share of each dominant color.
5. **UI Rendering**: Color boxes and hex codes are dynamically generated and populated inside the Tkinter frame.

---

## 🛠️ Customization

If you want to extract more or fewer colors, locate line 38 in the script and update the `number_of_colors` variable:

```python
# Change 5 to any number of dominant colors you'd like to extract
number_of_colors = 8
```
