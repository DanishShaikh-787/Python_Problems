"""
   * Author - danish
   * Date - 17/11/20
   * Time - 9:49 AM
   * Title - calculating weather condition from temp and wind speed
"""
import math
import sys

class WindChill:

    def findWeatherCondition(self):
        """Method Definition
        Operation:calculating weather condition from temp and wind speed
        :return: Weather condition value as per formula
        """
        weather = 35.74+(0.6215*self.temp)+(0.4275*self.temp-35.75)*math.pow(self.windSpeed, 0.16)
        return weather

    def commandLineInputTempAndWindSpeed(self):
        """Method Definition
         Operation:Taking input from user for temp and wind speed
        :return: Does Not return any value
        """
        while True:
            try:
                self.temp = float(sys.argv[1])
                self.windSpeed = float(sys.argv[2])
                if self.temp > 50:
                    print("Temperature should be less then 50 fahrenheit")
                    continue
                if  self.windSpeed > 3:
                      if self.windSpeed > 120:
                       print("Wind speed should be between 3 to 120")
                       continue
                else:
                  print("Wind speed should be between 3 to 120")
                  continue
                break
            except ValueError:
                print("Opps not valid float type")

if __name__ == "__main__":
   # Main Method input from user
  windchill = WindChill()
  windchill.commandLineInputTempAndWindSpeed()
  weather = windchill.findWeatherCondition()
  print("Weather condition value is: ", weather)
