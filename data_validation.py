class DataValidation:
  def __init__(self, data):
    self.data = data
  def get_missing_values(self,column: str):
    return self.data[column].isna().sum()
  def get_unique_values(self,column: str):
    return len(self.data[column].unique())
  

