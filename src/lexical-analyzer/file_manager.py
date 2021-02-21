from os.path import isfile, join, abspath
from os import listdir

class FileManager:

  def __init__(self):
    pass

  def readFiles(self):
    path = abspath('src/input')
    data = []

    for file in listdir(path):
      if isfile(join(path, file)):
        with open(join(path, file), 'r') as content:
          text = content.read()
          data.append({
            'fileName': file,
            'content': text
          })
          
    return data

  def writeFiles(self, data):
    pass  