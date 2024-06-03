import open3d as o3d
import numpy as np
import matplotlib.pyplot as plt

def load_point_cloud(file_path):
    point_cloud = o3d.io.read_point_cloud(file_path)
    return point_cloud

def segment_floor(point_cloud, height_threshold=0.1):
    # Extract points within the height threshold from the ground
    points = np.asarray(point_cloud.points)
    mask = np.abs(points[:, 2]) < height_threshold
    floor_points = points[mask]
    return floor_points

def project_to_2d(floor_points):
    # Project floor points to 2D (ignoring Z coordinate)
    floor_2d = floor_points[:, :2]
    return floor_2d

def create_floor_plan(floor_2d, resolution=0.05):
    # Create a 2D histogram to represent the floor plan
    min_coords = np.min(floor_2d, axis=0)
    max_coords = np.max(floor_2d, axis=0)
    grid_size = ((max_coords - min_coords) / resolution).astype(int) + 1
    
    floor_plan = np.zeros(grid_size, dtype=int)
    
    for point in floor_2d:
        grid_coords = ((point - min_coords) / resolution).astype(int)
        floor_plan[grid_coords[1], grid_coords[0]] += 1
    
    return floor_plan

def plot_floor_plan(floor_plan):
    plt.imshow(floor_plan, cmap='gray', origin='lower')
    plt.title('Floor Plan')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.show()

# Load and process the point cloud
point_cloud = load_point_cloud('path_to_your_point_cloud_file.ply')
floor_points = segment_floor(point_cloud)
floor_2d = project_to_2d(floor_points)
floor_plan = create_floor_plan(floor_2d)

# Plot the floor plan
plot_floor_plan(floor_plan) 
