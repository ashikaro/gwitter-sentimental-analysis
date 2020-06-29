from city_light_manager import CityLightManager


class City:
    def __init__(self, name, red, green, yellow, geo_code):
        self.name = name # name of the city
        self.green = green # GPIO pin for the green led light
        self.red = red # GPIO pin for red led light
        self.yellow = yellow # GPIO pin for yellow led light
        self.geo_code = geo_code # Geocode for the city to be sent to the Twitter's search API
        self.cityLightManager =  CityLightManager(self.red, self.green, self.yellow)

    def glow_led_light(self, sentimentAnalysis):

        finalResult = sentimentAnalysis.classify(self.sentimentResult.mean)

        if finalResult == self.sentimentResult.POSITIVE:
            print("turning on green for {}".format(self.name))
            self.cityLightManager.turnOnGreen()
        elif finalResult == self.sentimentResult.NEGATIVE:
            print("turning on red for {}".format(self.name))
            self.cityLightManager.turnOnRed()
        else:
            print("turning on yellow for {}".format(self.name))
            self.cityLightManager.turnOnYellow()







