#!/bin/env python3
from importlib.metadata import version, PackageNotFoundError


def print_package_info(package: str, desc: str) -> None:
    try:
        pck_version = version(package)
        print(f"[OK] {package} ({pck_version}) - {desc} ready")
    except PackageNotFoundError:
        raise Exception(f"[!] The package '{package}' is NOT installed.")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")
    loading_err: bool = False
    try:
        print_package_info("pandas", "Data manipulation")
    except Exception as error:
        print(error)
        loading_err = True
    try:
        print_package_info("numpy", "Numerical computation")
    except Exception as error:
        print(error)
        loading_err = True
    try:
        print_package_info("requests", "Network access")
    except Exception as error:
        print(error)
        loading_err = True
    try:
        print_package_info("matplotlib", "Visualization")
    except Exception as error:
        print(error)
        loading_err = True
    if loading_err:
        print("Package/s not installed, use the following methods to install:")
        print("For pip use: pip install -r requirements.txt")
        print("For poetry use: poetry install")
    else:
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        print("Analyzing Matrix data...")
        np.random.seed(42)
        matrix_data = np.random.randn(250, 4)

        print(f"Processing {matrix_data.size} data points...")
        df = pd.DataFrame(matrix_data, columns=[
                          'Sensor_A', 'Sensor_B', 'Sensor_C', 'Sensor_D'])

        df_smooth = df.rolling(window=20).mean()

        print("Generating visualization...")
        plt.figure(figsize=(10, 6))
        plt.plot(df_smooth)
        plt.title('Processed Sensor Signals (Rolling Mean)')
        plt.legend(df_smooth.columns)
        plt.grid(True, alpha=0.3)

        output_file = "matrix_analysis.png"
        plt.savefig(output_file)

        print("Analysis complete!")
        print(f"Results saved to: {output_file}")


if __name__ == "__main__":
    main()
