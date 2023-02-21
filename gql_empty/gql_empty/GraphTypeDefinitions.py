from typing import List, Union, Optional
import typing
from unittest import result
import strawberry as strawberryA
import uuid
import datetime
from contextlib import asynccontextmanager

@asynccontextmanager
async def withInfo(info):
    asyncSessionMaker = info.context['asyncSessionMaker']
    async with asyncSessionMaker() as session:
        try:
            yield session
        finally:
            pass

def AsyncSessionFromInfo(info):
    return info.context['session'] 

def AsyncSessionMakerFromInfo(info):
    return info.context['asyncSessionMaker']

###########################################################################################################################
#
# zde definujte sve GQL modely
# - nove, kde mate zodpovednost
# - rozsirene, ktere existuji nekde jinde a vy jim pridavate dalsi atributy
#
###########################################################################################################################
#FACILITIES
from gql_empty.GraphResolvers import resolveFacilityById, resolveFacilityPage, resolveInsertFacility, resolveUpdateFacility
@strawberryA.federation.type(description="""Type for query root""")
class FacilityGQLModel:

    # @classmethod
    # async def resolve_reference(cls, info: strawberryA.types.Info, id: strawberryA.ID):
    #     result = await resolveWorkflowById(AsyncSessionFromInfo(info), id)
    #     result._type_definition = cls._type_definition # little hack :)
    #     return result

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
    #facilitytype_id->facilitytype table
    @strawberryA.field(description="""Project type of project""")
    async def facilityType(self, info: strawberryA.types.Info) -> 'FacilityTypeGQLModel':
        async with withInfo(info) as session:
            result = await resolveFacilityTypeById(session, self.facilityType_id)
            return result
    #manager_id->user table  ????je správně
    @strawberryA.field(description="""user model from ug_container""")
    async def manager_id(self) -> 'UserGQLModel':
        return UserGQLModel(id=self.user_id)
    #master_facility_id->??správně když foreign
    @strawberryA.field(description="""master-facility id""")
    def master_facility_id(self) -> strawberryA.ID:
        return self.master_facility_id
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
#FACILITY UPDATE
@strawberryA.input(description="""Entity representing a facility update""")
class FacilityUpdateGQLModel:
    lastchange: datetime.datetime
    name:  Optional[str] = None
    address:  Optional[str] = None
    label:  Optional[str] = None
    capacity:  Optional[int] = None
    geometry:  Optional[str] = None
    geolocation:  Optional[str] = None
    facilitytype_id: Optional[uuid.UUID] = None
    manager_id: Optional[uuid.UUID] = None
    valid: Optional[bool] = None
    start_date: Optional[datetime.date] = None 
    end_date: Optional[datetime.date] = None 
    master_facility_id: Optional[uuid.UUID] = None

#FACILITY EDITOR
@strawberryA.federation.type(keys=["id"], description="""Entity representing an editable facility""")
class FacilityEditorGQLModel:
    id: strawberryA.ID = None
    result: str = None

    @classmethod
    async def resolve_reference(cls, info: strawberryA.types.Info, id: strawberryA.ID):
        async with withInfo(info) as session:
            result = await resolveFacilityById(session, id)
            result._type_definition = cls._type_definition # little hack :)
            return result

    @strawberryA.field(description="""Entity primary key""")
    def id(self) -> strawberryA.ID:
        return self.id

    @strawberryA.field(description="""Result status of update operation""")
    def result(self) -> str:
        return self.result 

    @strawberryA.field(description="""Result of update operation""")
    async def facility(self, info: strawberryA.types.Info) -> FacilityGQLModel:
        async with withInfo(info) as session:
            result = await resolveFacilityById(session, id)
            return result

    @strawberryA.field(description="""Updates the facility data""")
    async def update(self, info: strawberryA.types.Info, data: FacilityUpdateGQLModel) -> 'FacilityEditorGQLModel':
        lastchange = data.lastchange
        async with withInfo(info) as session:
            await resolveUpdateFacility(session, id=self.id, data=data)
            if lastchange == data.lastchange:
                # no change
                resultMsg = "fail"
            else:
                resultMsg = "ok"
            result = FacilityEditorGQLModel()
            result.id = self.id
            result.result = resultMsg
            return result    

    @strawberryA.field(description="""Invalidate facility""")
    async def invalidate_facility(self, info: strawberryA.types.Info) -> 'FacilityGQLModel':
        async with withInfo(info) as session:
            facility = await resolveFacilityById(session, self.id)
            facility.valid = False
            await session.commit()
            return facility
        
   
###END EDITOR
   
#FACILITY TYPE    
from gql_empty.GraphResolvers import resolveFacilityTypeById, resolveFacilityTypeAll, resolveInsertFacilityType, resolveUpdateFacilityType
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

#USER
@strawberryA.federation.type(extend=True, keys=["id"])
class UserGQLModel:

    id: strawberryA.ID = strawberryA.federation.field(external=True)

    @classmethod
    def resolve_reference(cls, id: strawberryA.ID):
        return UserGQLModel(id=id)
    


###########################################################################################################################
#
# zde definujte svuj Query model
#
###########################################################################################################################
#from gql_empty.GraphResolvers import resolveFacilityById, resolveFacilityPage
from gql_empty.DBFeeder import randomDataStructure
@strawberryA.type(description="""Type for query root""")
class Query:
   
    @strawberryA.field(description="""Finds an workflow by their id""")
    async def say_hello(self, info: strawberryA.types.Info, id: uuid.UUID) -> Union[str, None]:
        result = f'Hello {id}'
        return result

    @strawberryA.field(description="""Finds an facility by id""")
    async def facility_by_id(self, info: strawberryA.types.Info, id: uuid.UUID) -> FacilityGQLModel:
        result = await resolveFacilityById(AsyncSessionFromInfo(info), id )
        return result

    @strawberryA.field(description="""List of facilities""")
    async def facility_page(self, info: strawberryA.types.Info) -> List[FacilityGQLModel]:
        result = await resolveFacilityPage(AsyncSessionFromInfo(info),0,1000)
        return result

    @strawberryA.field(description="""List of facility types""")
    async def facility_type_page(self, info: strawberryA.types.Info, skip: int = 0, limit: int = 10) -> List[FacilityTypeGQLModel]:
        async with withInfo(info) as session:
            result = await resolveFacilityTypeAll(session, skip, limit)
            return result

    @strawberryA.field(description="""Random facility""")
    async def randomFacility(self, name: str, info: strawberryA.types.Info) -> str:
        newId = await randomDataStructure(AsyncSessionFromInfo(info))#tady druhy arg name
        # print('random facility id', newId)
        # result = await resolveFacilityById(AsyncSessionFromInfo(info), newId)
        # print('db response', result.name)
        return "ok"