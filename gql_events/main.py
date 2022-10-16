from typing import List
from urllib.request import Request

import typing
import strawberry as strawberryB

def randomEvent(id = 1):
    return {'id': id, 'name': f'Event({id})'}

def randomUser(id = 1):
    return {'id': id, 'name': 'John', 'surname': 'Leon', 'groups': [{'id': 1}]}

def resolveDictField(self, info: strawberryB.types.Info) -> str:
    return self[info.field_name]



def randomCampus(id=1):
    return{'id':id, 'name':'Campus_one','adress':'CampusOne_adress','managerID':'1'} 
 


@strawberryB.federation.type(extend=True, keys=["id"])
class UserGQLModel:

    id: strawberryB.ID = strawberryB.federation.field(external=True)

    @strawberryB.field
    def events(self) -> typing.List['EventGQLModel']:
        return [randomEvent(id) for id in range(10)]

    @classmethod
    def resolve_reference(cls, id: strawberryB.ID):
        # here we could fetch the book from the database
        # or even from an API
        return UserGQLModel(id=id)

@strawberryB.federation.type(keys=["id"])
class EventGQLModel:

    @strawberryB.field
    def id(self) -> str:
        return self['id']

    @strawberryB.field
    def name(self) -> str:
        return self['name']

    @strawberryB.field
    def users(self) -> typing.List['UserGQLModel']:
        return [randomUser(user['id']) for user in self['users']]


""" return{'id':id, 'name':'Campus_one','adress':'CampusOne_adress','managerID':'1'} """
@strawberryB.federation.type(keys=["id"])
class CampusGQLModel:

    @strawberryB.field
    def id(self) -> str:
        return self['id']

    @strawberryB.field
    def name(self) -> str:
        return self['name']

    @strawberryB.field
    def adress(self) -> str:
        return self['adress']
    
    @strawberryB.field
    def managerID(self) -> str:
        return self['managerID']

   







@strawberryB.type
class Query:
    _service: typing.Optional[str]
    
    @strawberryB.field
    def event_by_id(self, id: str) -> 'EventGQLModel':
        return randomEvent(id)

    @strawberryB.field
    def campus_by_id(self, id: str) -> 'CampusGQLModel':
        return randomCampus(id)



from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

def myContext():
    return {'session': None}

graphql_app = GraphQLRouter(
    strawberryB.federation.Schema(query=Query, types=[UserGQLModel, EventGQLModel, CampusGQLModel]), 
    graphiql = True,
    allow_queries_via_get = True,
    root_value_getter = None,
    context_getter = myContext#None #https://strawberry.rocks/docs/integrations/fastapi#context_getter
)

app = FastAPI()
#app.add_middleware(MyMiddleware)
app.include_router(graphql_app, prefix="/gql")

print('All initialization is done')

@app.get('api/ug_gql')
def hello():
    return {'hello': 'world'}


