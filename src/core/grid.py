import numpy as np

class ReservoirGrid:
    def __init__(self, Nx, Ny, dx, dy):
        """
        Initializes the spatial dimensions and physical properties of the reservoir.
        Use SI Units: meters, Pascals, Kelvin.
        """
        self.Nx = Nx
        self.Ny = Ny
        self.dx = dx
        self.dy = dy

        self.num_cells = Nx * Ny

        self.permeability =  np.ones(self.num_cells , dtype = np.float64 ) * 1e-14 # default permeability = 1e-14
        self.porosity = np.ones(self.num_cells , dtype = np.float64 ) * 0.20 # default porosity = 0.20
        self.pressure = np.ones(self.num_cells , dtype = np.float64 ) * 1e7 # default pressure = 1e7
        self.temperature = np.ones(self.num_cells , dtype = np.float64 ) * 350.0 # default temperature = 350.0

        if self.dx <= 0 or self.dy <= 0:
            raise ValueError("Grid spacing must be positive")
        if Nx <= 0 or Ny <= 0:
            raise ValueError("Grid dimensions must be positive")

        
    def get_1d_index(self, i, j):
        """
        Converts a 2D (i, j) coordinate to a 1D index k.
        Must include a safety check to ensure i and j are within grid boundaries.
        Returns: integer k, or raises ValueError if out of bounds.
        """
        if i < 0 or i >= self.Nx:
            raise ValueError(f"Column index i={i} out of bounds (0 to {self.Nx - 1})")
    
        if j < 0 or j >= self.Ny:
            raise ValueError(f"Row index j={j} out of bounds (0 to {self.Ny - 1})")
        
        k = j * self.Nx + i 
        return k 

    def get_2d_coord(self, k):
        """
        Converts a 1D index k back to a 2D (i, j) coordinate.
        Returns: tuple (i, j)
        """
        if k < 0 or k >= self.num_cells:
            raise ValueError(f"Index k={k} out of bounds (0 to {self.num_cells - 1})")
    
        i = k % self.Nx
        j = k // self.Nx

        return (i,j)
    
    def get_neighbors(self, i, j):
        """
        Returns valid neighboring grid coordinates (4-connectivity).
        """
        neighbors = []
        
        if i > 0:
            neighbors.append((i-1, j))
        if i < self.Nx - 1:
            neighbors.append((i+1, j))
        if j > 0:
            neighbors.append((i, j-1))
        if j < self.Ny - 1:
            neighbors.append((i, j+1))
        
        return neighbors
    