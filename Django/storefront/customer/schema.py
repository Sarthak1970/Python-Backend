import graphene
from graphene_django import DjangoObjectType
from .models import Client

class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = ("id","first_name","last_name","city")

class Query(graphene.ObjectType):

    all_clients = graphene.List(ClientType)

    def resolve_all_clients(root,info):
        return Client.objects.all()

schema = graphene.Schema(query=Query)
