# Problem: Planetary Weight Calculator

import string


def mars_weight():
  user_input = float(input("Input your Earth weight: "))
  mars_weight : float = user_input * 0.378
  rounded_weight: float = round(mars_weight, 2)


#-------------------------------


plantery_weight_constant ={
    "mercury": 37.6,
    "venus": 88.9,
    "earth": 1.00,
    "mars": 37.8,
    "jupiter": 236.0,
    "saturn": 108.1,
    "uranus": 81.5,
    "neptune": 114.0
}
def plantery_weight():
  earth_weight = float(input("Enter your Earth weight please: "))
  planet_of_choices = str(input("Enter the name of the planet you are going to visit: ")).lower()


  if planet_of_choices in plantery_weight_constant:
    plantery_weight = earth_weight * plantery_weight_constant[planet_of_choices] /100
    print(f"Your weight on {planet_of_choices} is {plantery_weight}kg")
  else: 
     print("Please enter a valid planet name")
plantery_weight()