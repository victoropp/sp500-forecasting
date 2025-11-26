"""
S&P 500 Intelligent Forecasting Platform
Entry point for Streamlit Cloud deployment.

Author: Victor Collins Oppon
Role: Data Scientist
"""

import os
import sys
from pathlib import Path

# Get project root directory
PROJECT_ROOT = Path(__file__).resolve().parent

# Change working directory to project root
os.chdir(PROJECT_ROOT)

# Add project root to path for imports
sys.path.insert(0, str(PROJECT_ROOT))

# Execute the main app
exec(compile(open(PROJECT_ROOT / "deployment" / "app.py").read(), str(PROJECT_ROOT / "deployment" / "app.py"), "exec"))
