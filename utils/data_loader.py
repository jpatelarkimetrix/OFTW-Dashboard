import polars as pl

from pathlib import Path
import os
import threading

DATA_DIR = (Path(__file__)/'..'/'..'/'data').resolve()

class DataLoader:
    _instance = None
    _lock = threading.Lock()    # Thread-safe singleton lock

    def __new__(cls, file_names):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, file_names):
        if not hasattr(self, 'dir_name'):  # Ensure attributes are initialized only once
            self.dir_name = DATA_DIR
            self.dataframes = {}
            self.schema = {}
            if file_names:
                self._load_all(file_names)

    def _load_all(self, file_names):
        """
        Load multiple files (CSV and Parquet) into lazy Polars DataFrames.
        """
        for name, path in file_names.items():
            full_path = os.path.join(self.dir_name, path)
            self.dataframes[name] = self._load_file(full_path)

    def _load_file(self, path):
        """
        Detects the file type (CSV or Parquet) and loads it lazily.
        """
        if path.endswith('.csv'):
            return pl.scan_csv(path)  # Lazy CSV loading
        elif path.endswith('.parquet'):
            return pl.scan_parquet(path)  # Lazy Parquet loading
        else:
            raise ValueError(f"Unsupported file format: {path}")

    def get_data(self, dataset_name):
        if dataset_name not in self.dataframes:
            raise ValueError(f"Dataset '{dataset_name}' not found.")
        return self.dataframes[dataset_name]

parquet_files = {
    "merged": "merged.parquet",
    "pledges": "pledges.parquet",
    "payments": "payments.parquet",
    "pledge_active_arr": "pledge_active_arr.parquet",
}

data_loader = DataLoader(parquet_files)