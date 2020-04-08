import graphene

import corona.schema


class Query(corona.schema.SubmittedQuery, corona.schema.CoronaQuery, graphene.ObjectType):
    pass


class Mutation(corona.schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)