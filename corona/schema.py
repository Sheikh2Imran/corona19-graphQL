import graphene
from graphene_django import DjangoObjectType

from . models import District, SubmittedCoronaCase


class DistrictType(DjangoObjectType):
    class Meta:
        model = District


class Query(graphene.ObjectType):
    districts = graphene.List(DistrictType)

    def resolve_districts(self, info, **kwargs):
        return District.objects.all()


class CreateSubmittedCoronaCase(graphene.Mutation):
    id = graphene.Int()
    person_name = graphene.String()
    email = graphene.String()
    fb_link = graphene.String()
    total_corona_case = graphene.Int()
    district = graphene.String()
    source = graphene.String()
    status = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()

    class Arguments:
        person_name = graphene.String()
        email = graphene.String()
        fb_link = graphene.String()
        total_corona_case = graphene.Int()
        district = graphene.String()
        source = graphene.String()

    def mutate(self, info, *args, **kwargs):
        corona_case = SubmittedCoronaCase.objects.create(
            person_name=kwargs['person_name'],
            email=kwargs['email'],
            fb_link=kwargs['fb_link'],
            total_corona_case=kwargs['total_corona_case'],
            district=kwargs['district'],
            source=kwargs['source']
        )

        return CreateSubmittedCoronaCase(
            id=corona_case.id,
            person_name=corona_case.person_name,
            email=corona_case.email,
            fb_link=corona_case.fb_link,
            total_corona_case=corona_case.total_corona_case,
            district=corona_case.district,
            source=corona_case.source,
            status=corona_case.status,
            created_at=corona_case.created_at,
            updated_at=corona_case.created_at,
        )


class UpdateSubmittedCoronaCase(graphene.Mutation):
    id = graphene.Int()
    person_name = graphene.String()
    email = graphene.String()
    fb_link = graphene.String()
    total_corona_case = graphene.Int()
    district = graphene.String()
    source = graphene.String()
    status = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()

    class Arguments:
        person_name = graphene.String()
        email = graphene.String()
        fb_link = graphene.String()
        total_corona_case = graphene.Int()
        district = graphene.String()
        source = graphene.String()

    def mutate(self, info, *args, **kwargs):
        corona_case = SubmittedCoronaCase.objects.create(
            person_name=kwargs['person_name'],
            email=kwargs['email'],
            fb_link=kwargs['fb_link'],
            total_corona_case=kwargs['total_corona_case'],
            district=kwargs['district'],
            source=kwargs['source']
        )

        return UpdateSubmittedCoronaCase(
            id=corona_case.id,
            person_name=corona_case.person_name,
            email=corona_case.email,
            fb_link=corona_case.fb_link,
            total_corona_case=corona_case.total_corona_case,
            district=corona_case.district,
            source=corona_case.source,
            status=corona_case.status,
            created_at=corona_case.created_at,
            updated_at=corona_case.created_at,
        )


class Mutation(graphene.ObjectType):
    create_submitted_corona_case = CreateSubmittedCoronaCase.Field()