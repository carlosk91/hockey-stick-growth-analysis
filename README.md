# Google Trends Analysis of Startup Growth Patterns

This project analyzes the 'hockey stick' growth pattern of various startups using Google Trends data. It focuses on companies like Groupon, Uber, Airbnb, and WeWork, providing insights into their growth trajectories over time.

This project focuses on analyzing trends in 'hockey stick' growth patterns within various companies. It's important to note that while this analysis provides insights into past trends, it is not intended to forecast future outcomes.


## Project Description

This script fetches Google Trends data for selected startups and uses Piecewise Regression with Dynamic Change Point Detection to identify significant shifts in their growth trajectories. The analysis aims to visualize and understand the 'hockey stick' growth phase commonly observed in successful startups.

## Key Features

- Fetches Google Trends data for specified companies.
- Identifies significant growth change points using Piecewise Regression.
- Generates and saves visual plots illustrating these growth patterns.
- Compares multiple companies in a composite graph.

## Getting Started

### Prerequisites

- Python 3.x
- Required Python libraries: `pandas`, `matplotlib`, `numpy`, `ruptures`, `statsmodels`, `pytrends`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/carlosk91/hockey-stick-growth-analysis.git
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the script using Python:

   ```bash
   python hockey-stick-growth-analysis.py
   ```

The script will generate plots in the graphs directory, illustrating the growth patterns of the selected companies.

### Dependencies

This project relies on several open-source libraries:

* Pandas: Data manipulation and analysis (BSD-3-Clause License)
* Matplotlib: Plotting library (Matplotlib License)
* Pytrends: Unofficial Google Trends API (Apache 2.0 License)
* Statsmodels: Statistical modeling and econometrics (Modified BSD License)
* Ruptures: Change point detection in time series (BSD-2-Clause License)
* NumPy: Fundamental package for scientific computing (BSD-3-Clause License)

### Contributing

Contributions to enhance the functionality or efficiency of this script are welcome. Please adhere to standard coding practices and provide clear documentation with your pull requests.

### Aknowledgments

Special thanks to the investors, finance professionals, and product leaders whose queries and insights inspired the creation of this project. Their perspectives on growth patterns and business development have been invaluable in shaping the analysis and approach taken in this work.

### License

This project is licensed under the MIT License - see the LICENSE.txt file for details.

### Contact

You can contact me on https://www.linkedin.com/in/carlosk91/

----
For more details on the licenses of the dependencies used in this project, please refer to their respective official documentation or source code repositories.



