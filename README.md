# NumPy Data Explorer

A hands-on project exploring the core features of NumPy, Python's fundamental library for numerical computing.

## What This Project Covers

1. **Array Creation** – Creating arrays using `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`, and `np.eye()`
2. **Indexing and Slicing** – Accessing single elements, ranges, 2D indexing, and boolean indexing
3. **Mathematical, Axis-wise, and Statistical Operations** – Element-wise math, sum/mean/std/max/min along different axes
4. **Reshaping and Broadcasting** – Changing array shapes with `reshape()` and `flatten()`, and combining arrays of different shapes using broadcasting
5. **Save/Load Operations** – Saving and loading arrays using `.npy`, `.npz`, and `.csv` formats
6. **NumPy vs Standard Python Performance** – Comparing execution speed between a Python loop and a vectorized NumPy operation

## Tools Used

- Python 3
- NumPy
- Google Colab

## How to Run

1. Open `NumPy_Data_Explorer.ipynb` in Google Colab or Jupyter Notebook
2. Run each cell in order (Shift + Enter)
3. NumPy comes pre-installed in Colab; if running locally, install it with:
   typing this in your terminal:

pip install numpy

## Key Takeaway

NumPy operations are significantly faster than standard Python loops because they run as vectorized, pre-compiled C code under the hood — making it the foundation for data science, machine learning, and scientific computing in Python.
