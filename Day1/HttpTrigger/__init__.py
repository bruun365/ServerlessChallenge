import logging
import random
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    List = ["Nun", "Gimmel", "Hay"]
    RandomItem = random.choice(List)
    #The f or F in front of strings tell Python to look at the values inside {} and substitute them with the variables values if exists
    return func.HttpResponse(f"the dreidel has spinned and returned {RandomItem}")
