import numpy as np

class ReservoirGrid:
    def __init__(self, nx, ny, dx, dy):
        """
        Initializes the spatial dimensions and physical properties of the reservoir.
        Use SI Units: meters, Pascals, Kelvin.
        """
        self.nx = nx
        self.ny = ny
        self.dx = dx
        self.dy = dy

        self.num_cells = nx*ny

        self.permeability =  np.ones(self.num_cells)*1e-14 # default permeability = 1e-14
        self.porosity = np.ones(self.num_cells)*0.20 # default porosity = 0.20
        self.pressure = np.ones(self.num_cells)*1e7 # default pressure = 1e7
        self.temperature = np.ones(self.num_cells)*350.0 # default temperature = 350.0
        
    def get_1d_index(self, i, j):
        """
        Converts a 2D (i, j) coordinate to a 1D index k.
        Must include a safety check to ensure i and j are within grid boundaries.
        Returns: integer k, or raises ValueError if out of bounds.
        """
        if i < 0 or i >= self.nx:
            raise ValueError(f"Column index i={i} out of bounds (0 to {self.nx - 1})")
    
        if j < 0 or j >= self.ny:
            raise ValueError(f"Row index j={j} out of bounds (0 to {self.ny - 1})")
        
        k = j * self.nx + i 
        return k 

    def get_2d_coord(self, k):
        """
        Converts a 1D index k back to a 2D (i, j) coordinate.
        Returns: tuple (i, j)
        """
        if k < 0 or k >= self.num_cells:
            raise ValueError(f"Index k={k} out of bounds (0 to {self.num_cells - 1})")
    
        i = k % self.nx
        j = k // self.nx

        return (i,j)