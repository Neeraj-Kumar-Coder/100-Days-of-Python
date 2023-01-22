# Virtual Environment is a seperate python environment on the same system
# This is used to work on different projects that are using different versions of multiple packages without conflict

# STEPS:

# To create a virtual environment: python -m venv python_virtual_environment

# To activate the created virtual environment: python_virtual_environment\Scripts\activate

# Now we can install the required packages with different versions on this virtual environment without conflict with the global one

# To create a requirements.txt file for the list of install packages with there versions: pip freeze > requirements.txt

# To install from requirements.txt: pip install -r requirements.txt

# To deactivate the virtual enivronment: deactivate
