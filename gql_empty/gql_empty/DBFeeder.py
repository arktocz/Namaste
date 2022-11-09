from doctest import master
from functools import cache
from gql_empty.DBDefinitions import BaseModel, FacilityModel, UserModel #GroupModel, RoleTypeModel

import random
import itertools
from functools import cache


from sqlalchemy.future import select

def singleCall(asyncFunc):
    """Dekorator, ktery dovoli, aby dekorovana funkce byla volana (vycislena) jen jednou. Navratova hodnota je zapamatovana a pri dalsich volanich vracena.
       Dekorovana funkce je asynchronni.
    """
    resultCache = {}
    async def result():
        if resultCache.get('result', None) is None:
            resultCache['result'] = await asyncFunc()
        return resultCache['result']
    return result

###########################################################################################################################
#
# zde definujte sve funkce, ktere naplni random data do vasich tabulek
#

@cache
def determineFacilityTypes():
    """Definuje zakladni typy facility a udrzuje je v pameti (campus/building/floor/room)"""
    facilityTypes = [
        {'name':'campus'},
        {'name':'building'},
        {'name':'floor'},
        {'name':'room'}
    ]
    return facilityTypes


##vymyslet struct která doplni id podle typu facility



def randomFacility(name):
    """Genreruje strukturu facility a jejich hlavního fukcionáře ve formě JSON"""
    result={
        'name':f'{name}',
        'adress':'RandAdress'+str(random.randint(1,10)),
        'valid':'True',



    }




###########################################################################################################################