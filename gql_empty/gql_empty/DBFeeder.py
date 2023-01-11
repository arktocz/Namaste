from doctest import master
from functools import cache
from gql_empty.DBDefinitions import BaseModel, FacilityModel, FacilityTypeModel, UserModel

import uuid
import random
import itertools

from functools import cache
from sqlalchemy.future import select
from datetime import date, timedelta

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
###########################################################################################################################

def randomUUID(limit):
    random_uuid = [uuid.uuid4() for _ in range(limit)]
    return random_uuid

def randomFacilityName():
    names = ["Rohlik", "Kounicovka", "Zeme Oz", "Zemeplocha", "Mordor"]
    return random.choice(names)

def randomFacilityAddress():
    names = ["Adresa1", "Adresa2", "Adresa3", "Adresa4", "Adresa5"]
    return random.choice(names)

def randomFacilityLabel():
    names = ["Label1", "Label2", "Label3", "Label4", "Label5"]
    return random.choice(names)

def randomCapacity():
    capacity=random.randint(1,100)
    return capacity

def randomFacilityGeometry():
    names = ["Geometry1", "Geometry2", "Geometry3", "Geometry4", "Geometry5"]
    return random.choice(names)

def randomFacilityGeolocation():
    names = ["Geolocation1", "Geolocation2", "Geolocation3", "Geolocation4", "Geolocation5"]
    return random.choice(names)

def randomLastChange():
    base = date(2025, 1, 1)
    return base + timedelta(days=random.randint(1,30))

def randomStartDate():
    base = date(2023, 1, 1)
    return base + timedelta(days=random.randint(1,30))

def randomEndDate():
    base = date(2024, 1, 1)
    return base + timedelta(days=random.randint(1,30))

def randomManagerID():
    managerUUID=uuid.uuid4()
    return managerUUID

facilitytypesIDs = randomUUID(4)
def determineFacilityTypes():
    """Definuje typy facilities"""
    facilityTypes = [ 
        {'id': facilitytypesIDs[0], 'name':'Areal', },
        {'id': facilitytypesIDs[1], 'name':'Budova'},
        {'id': facilitytypesIDs[2], 'name':'Patro'},
        {'id': facilitytypesIDs[3], 'name':'Mistnost'},
    ]
    return facilityTypes

areaUUIDs= randomUUID(4)
budovaUUIDs=randomUUID(8)
patroUUIDs=randomUUID(16)
mistnostUUID=randomUUID(32)


def randomArea(id):
    """nahodna facility"""
    return {
        'id':id,
        'name':randomFacilityName(),
        'address':randomFacilityAddress(),
        'label':randomFacilityLabel(),
        'capacity':randomCapacity(),
        'geometry':randomFacilityGeometry(),
        'geolocation':randomFacilityGeolocation(),
        # 'facilitytype_id':,
        'manager_id':randomManagerID(),
        'lastchange':randomLastChange(),
        'valid': True,
        'startdate':randomStartDate(),
        'enddate':randomEndDate(),
        'master_facility_id':
        }



def createDataStructureFacilityTypes():
    facilityTypes=determineFacilityTypes()
    return facilityTypes