import pkg_resources
import subprocess

# List of dependencies to check for
dependencies = ["ipywidgets", "IPython"]

# Function to check if a package is installed
def is_installed(package_name):
    try:
        pkg_resources.get_distribution(package_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False

# Function to install a package
def install_package(package_name):
    subprocess.check_call(['python', '-m', 'pip', 'install', package_name])

# Main function to check and install dependencies
def main():
    print("Checking dependencies...")
    # Check each dependency and install if not found
    for package in dependencies:
        if not is_installed(package):
            print(f"{package} not found. Installing...")
            install_package(package)
        else:
            print(f"{package} is already installed.")

# Check if the script is being run as the main module
if __name__ == "__main__":
    main()