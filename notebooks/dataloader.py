from abc import ABC, abstractmethod
from datetime import datetime


class DataLoader(ABC):
    
    def __init__(self):
        self.json = None
        self.df = None
        
    @abstractmethod
    def load_data_from_range(self, t0=None, tf=None):
        """Main pipeline. Must return self"""
        ...
        return self
        
    @abstractmethod
    def _download_series(self, t0: datetime, tf: datetime):
        """Must set self.json. Returns None"""
        ...
        return
    
    @abstractmethod
    def _json_to_dataframe(self):
        ...
        """Must set self.df to actual value as pd.DataFrame. Returns None"""
        return
    
    def get_pandas(self):
        if self.df is None:
            raise Exception("Data not downloaded yet; run load_data_from_range before")
            
        return self.df

    @staticmethod
    def _two_digits(n: int):
        return str(n).zfill(2)