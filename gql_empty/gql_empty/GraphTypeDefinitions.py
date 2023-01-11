from typing import List, Union
import typing
import strawberry as strawberryA
import uuid
import datetime

def AsyncSessionFromInfo(info):
    return info.context['session'] 

###########################################################################################################################
#
# zde definujte sve GQL modely
# - nove, kde mate zodpovednost
# - rozsirene, ktere existuji nekde jinde a vy jim pridavate dalsi atributy
#
###########################################################################################################################

@strawberryA.federation.type(description="""Type for query root""")
class FacilityGQLModel:

    # @classmethod
    # async def resolve_reference(cls, info: strawberryA.types.Info, id: strawberryA.ID):
    #     result = await resolveWorkflowById(AsyncSessionFromInfo(info), id)
    #     result._type_definition = cls._type_definition # little hack :)
    #     return result

    
    # facilitytype_id = Column(ForeignKey('facilitytypes.id'))
    # manager_id=Column(ForeignKey('users.id'), primary_key=True)

      

    # master_facility_id=Column(ForeignKey('facilities.id'), primary_key=True) 

    #id
    @strawberryA.field(description="""primary key/facility id""")
    def id(self) -> strawberryA.ID:
        return self.id
    #name
    @strawberryA.field(description="""Facility name""")
    def name(self) -> str:
        return self.name
    #address
    @strawberryA.field(description="""Facility address""")
    def address(self) -> str:
        return self.address
    #label
    @strawberryA.field(description="""Facility label""")
    def label(self) -> str:
        return self.label  
    #capacity
    @strawberryA.field(description="""Facility capacity""")
    def capacity(self) -> int:
        return self.capacity   
    #geometry
    @strawberryA.field(description="""Facility geometry""")
    def geometry(self) -> str:
        return self.geometry  
    #geolocation
    @strawberryA.field(description="""Facility geolocation""")
    def geolocation(self) -> str:
        return self.geolocation 
    #facilitytype_id
    @strawberryA.field(description="""Facility geolocation""")
    async def geolocation(self) -> FacilityTypeGQLModel:
        return resolve  self.facilitytype_id 
    #manager_id
    #master_facility_id


    #lastchange
    @strawberryA.field(description="""is the membership still valid""")
    def lastchange(self) -> datetime.datetime:
        return self.lastchange
    #valid
    @strawberryA.field(description="""is the facility still valid""")
    def valid(self) -> bool:
        return self.valid
    #startdate
    @strawberryA.field(description="""is the membership still valid""")
    def startdate(self) -> datetime.datetime:
        return self.startdate
    #enddate
    @strawberryA.field(description="""is the membership still valid""")
    def enddate(self) -> datetime.datetime:
        return self.enddate

   
    
   

    

@strawberryA.federation.type(keys=["id"], description="""Type for query root""")
class FacilityTypeGQLModel:
    # @classmethod
    # async def resolve_reference(cls, info: strawberryA.types.Info, id: strawberryA.ID):
    #     result = await resolveWorkflowById(AsyncSessionFromInfo(info), id)
    #     result._type_definition = cls._type_definition # little hack :)
    #     return result
    #id
    @strawberryA.field(description="""primary key/facility type id""")
    def id(self) -> strawberryA.ID:
        return self.id
    #type name
    @strawberryA.field(description="""Facility type name""")
    def name(self) -> str:
        return self.name
    


###########################################################################################################################
#
# zde definujte svuj Query model
#
###########################################################################################################################
from gql_empty.GraphResolvers import resolveFacilityById, resolveFacilityPage
@strawberryA.type(description="""Type for query root""")
class Query:
   
    @strawberryA.field(description="""Finds an workflow by their id""")
    async def say_hello(self, info: strawberryA.types.Info, id: uuid.UUID) -> Union[str, None]:
        result = f'Hello {id}'
        return result

    @strawberryA.field(description="""Finds an workflow by their id""")
    async def facility_by_id(self, info: strawberryA.types.Info, id: uuid.UUID) -> FacilityGQLModel:
        result = await resolveFacilityById(AsyncSessionFromInfo(info), id )
        return result

    @strawberryA.field(description="""Finds an workflow by their id""")
    async def facility_page(self, info: strawberryA.types.Info, id: uuid.UUID) -> FacilityGQLModel:
        result = await resolveFacilityPage(AsyncSessionFromInfo(info), id )
        return result