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
   
    @strawberryA.field(description="""Finds an workflow by their id""")
    async def id(self, info: strawberryA.types.Info) -> Union[str, None]:
        result = self.id
        return result

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