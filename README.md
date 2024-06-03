# 3D-to-FloorPlan-Converter
A Python program to convert 3D images into 2D floor plans using image processing techniques.

## Problem Statement

The goal is to develop a Python program that can convert 3D images into floor plans. This involves extracting meaningful information from the 3D images to generate a 2D representation of the floor layout. The challenge includes handling image processing, edge detection, and contour extraction to produce accurate floor plans.

## Approach

To address this problem, we will use the following approach:
1. **Image Loading:** Load the 3D image from the specified path.
2. **Grayscale Conversion:** Convert the loaded image to grayscale to simplify processing.
3. **Gaussian Blur:** Apply Gaussian blur to the grayscale image to reduce noise and enhance edge detection.
4. **Edge Detection:** Use the Canny edge detection algorithm to find edges in the image.
5. **Contour Detection:** Find contours in the edge-detected image to outline the shapes present.
6. **Contour Drawing:** Draw the detected contours on the original image to visualize the floor plan.
7. **Display Results:** Display the original image, edge-detected image, and image with contours side by side for comparison.

## Solution

The solution involves implementing the approach using Python and the OpenCV library for image processing. The program includes the following steps:

1. **Loading the Image:** The program loads an image from a specified path. It includes error handling to ensure the image file is found and loaded correctly.
2. **Converting to Grayscale:** The loaded image is converted to a grayscale image, which simplifies subsequent processing steps.
3. **Applying Gaussian Blur:** A Gaussian blur is applied to the grayscale image to reduce noise and improve the accuracy of edge detection.
4. **Edge Detection:** The Canny edge detection algorithm is used to identify edges in the blurred grayscale image.
5. **Finding Contours:** Contours are detected in the edge-detected image, outlining the significant shapes.
6. **Drawing Contours:** The detected contours are drawn on the original image to visualize the detected shapes.
7. **Displaying Images:** The original image, edge-detected image, and image with contours are displayed side by side for comparison.

## Instructions for Running

1. **Install Required Libraries:**
   Ensure you have Python installed on your system along with the necessary libraries. You can install the required libraries using pip:

   ```bash
   pip install opencv-python numpy matplotlib
   ```

2. **Prepare Images:**
   Save the 3D images you want to process in the same directory as the script or provide the correct path to the images.

3. **Run the Script:**
   Execute the script using a Python interpreter. For example, run the following command in your command line or terminal:

   ```bash
   python script_name.py
   ```

   Make sure to replace `script_name.py` with the actual name of your Python script file.

4. **Modify Image Path:**
   If your images are not named `3d_interior.jpg`, update the `image_path` variable in the `process_image` function with the correct path to your image file.

## Enhancements

To further improve the solution, consider the following enhancements:
- **Perspective Correction:** Implement techniques to correct perspective distortion in 3D images.
- **Feature Detection:** Use machine learning models to detect and label specific architectural features (walls, doors, windows) to improve floor plan accuracy.
- **Plan Generation:** Generate a vector-based floor plan from the detected contours using libraries like `svgwrite` for scalable vector graphics.

By following these steps, you can create a more robust and complex program for converting 3D images into floor plans.
