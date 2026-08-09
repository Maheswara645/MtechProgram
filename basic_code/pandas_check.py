try:
    import numpy as np
    print("✅ NumPy is installed.")
    print("NumPy version:", np.__version__)
except ImportError:
    print("❌ NumPy is NOT installed.")

print("-" * 40)

try:
    import pandas as pd
    print("✅ Pandas is installed.")
    print("Pandas version:", pd.__version__)
except ImportError:
    print("❌ Pandas is NOT installed.")