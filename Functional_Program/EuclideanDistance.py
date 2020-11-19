"""
   * Author - danish
   * Date - 16/11/20
   * Time - 10:03 PM
   * Title - Find The distance of Euclidean Points
"""
import math
import sys
class EuclideanDistance:
  pointX=0
  pointY=0

  def __init__(self,pointX,pointY):
    """
       define Constructor
       Operation:To initialize Data Members And Instantiate Object
      """
    self.pointX=pointX
    self.pointY=pointY

  def calculateDistance(self):
    """ Definition of  Method
       Operation:To calculate Euclidean Distastance from origin
       return Type:Does not return any value
    """
    distance = math.sqrt(self.pointX * self.pointX + self.pointY * self.pointY)
    print("Euclidean Distastance from",self.pointX, self.pointY,"is= ",distance)

if __name__ == '__main__':
  """ Mai Method Definition 
      Operation:Call Class methods 
  """
  # Command Line Argument
  pointXValue=int(sys.argv[1])
  pointYValue=int(sys.argv[2])
  object1=EuclideanDistance(pointXValue,pointYValue)
  object1.calculateDistance()
