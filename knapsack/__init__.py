# knapsack/__init__.py

# Import statements
from .fitness import fitness, final_values
from .initial_population import initial_population
from .crossover import crossover
from .generate_data import generate_data
from .main import knapsack_algo, read_data


# Package-level configuration
PACKAGE_VERSION = '0.0.42'
PACKAGE_AUTHOR = 'cleanupDev'

# Specify exported components
__all__ = [
    'fitness',
    'final_values',
    'initial_population',
    'crossover',
    'knapsack_algo',
    'read_data',
    'generate_data',
]
