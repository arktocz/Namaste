from typing import List, Union
import typing
import strawberry as strawberryA
import uuid

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
    #id
    @strawberryA.field(description="""Finds an facility by their id""")
    async def id(self, info: strawberryA.types.Info) -> Union[str, None]:#je jedno jestli async, když je to součástí entity
        result = self.id
        return result
    # @strawberryA.field(description="""Entity primary key""")
    # def id(self, info: strawberryA.types.Info) -> strawberryA.ID:
    #     return self.id

    #name
    # @strawberryA.field(description="""Facility's name""")
    # def name(self) -> str:
    #     return self.name
    #address
    # @strawberryA.field(description="""Facility's name""")
    # def address(self) -> str:
    #     return self.address
    #valid
    # @strawberryA.field(description="""is the membership is still valid""")
    # def valid(self) -> bool:
    #     return self.valid
    #startdate-?????bool je špatně
    #enddate
    #facilitytype_id

    #capacity
    # @strawberryA.field(description="""Facility's name""")
    # def capacity(self) -> int:
    #     return self.capacity
    #manager_id

    #master_facility_id
    #external_id

###########################################################################################################################
#
# zde definujte svuj Query model
#
###########################################################################################################################
from gql_empty.GraphResolvers import resolveFacilityById
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