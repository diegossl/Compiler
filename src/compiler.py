from .util.file_manager import FileManager

class Compiler:

  def __init__(self):
    pass
  
  def run(self):
    result = FileManager.readFiles()
    print(result)

