import datetime
from django.db.models import Sum

import graphene
from graphene_django import DjangoObjectType
from graphql import GraphQLError

from . models import SubmittedCoronaCase, CoronaCase
from common.status_code_list import *


class SubmittedCoronaCaseType(DjangoObjectType):
    class Meta:
        model = SubmittedCoronaCase


class SubmittedQuery(graphene.ObjectType):
    submitted_corona_cases_list = graphene.List(SubmittedCoronaCaseType)

    def resolve_submitted_corona_cases_list(self, info, **kwargs):
        return SubmittedCoronaCase.objects.all()


class CoronaCaseType(DjangoObjectType):
    class Meta:
        model = CoronaCase


class CoronaQuery(graphene.ObjectType):
    corona_cases_list = graphene.List(CoronaCaseType)

    def resolve_corona_cases_list(self, info, **kwargs):
        return CoronaCase.objects.all()


class CreateSubmittedCoronaCase(graphene.Mutation):
    id = graphene.Int()
    person_name = graphene.String()
    email = graphene.String()
    fb_link = graphene.String()
    affected = graphene.Int()
    death = graphene.Int()
    recovered = graphene.Int()
    district = graphene.String()
    source = graphene.String()
    status = graphene.String()
    created_at = graphene.DateTime()
    updated_at = graphene.DateTime()
    status_code = graphene.String()

    class Arguments:
        person_name = graphene.String()
        email = graphene.String()
        fb_link = graphene.String()
        affected = graphene.Int()
        death = graphene.Int()
        recovered = graphene.Int()
        district = graphene.String()
        source = graphene.String()

    def mutate(self, info, *args, **kwargs):
        corona_case = SubmittedCoronaCase.objects.create(
            person_name=kwargs['person_name'],
            email=kwargs['email'],
            fb_link=kwargs['fb_link'],
            affected=kwargs['affected'],
            death=kwargs['death'],
            recovered=kwargs['recovered'],
            district=kwargs['district'],
            source=kwargs['source']
        )
        if corona_case:
            status_code = CREATED_SUCCESS_CODE
        else:
            status_code = CREATED_ERROR_CODE

        return CreateSubmittedCoronaCase(
            id=corona_case.id,
            person_name=corona_case.person_name,
            email=corona_case.email,
            fb_link=corona_case.fb_link,
            affected=corona_case.affected,
            death=corona_case.death,
            recovered=corona_case.recovered,
            district=corona_case.district,
            source=corona_case.source,
            status=corona_case.status,
            created_at=corona_case.created_at,
            updated_at=corona_case.created_at,
            status_code=status_code,
        )


class UpdateSubmittedCoronaCase(graphene.Mutation):
    status_code = graphene.String()

    class Arguments:
        id = graphene.Int()
        status = graphene.String()

    def mutate(self, info, *args, **kwargs):
        if str(kwargs['status']) == '0':
            updated_status = SubmittedCoronaCase.objects.filter(id=kwargs['id']).update(status=kwargs['status'])
            if updated_status:
                return UpdateSubmittedCoronaCase(status_code=UPDATED_SUCCESS_CODE,)
        elif str(kwargs['status']) == '1':
            updated_status = SubmittedCoronaCase.objects.filter(id=kwargs['id']).update(status=kwargs['status'])
            submitted_corona_object = SubmittedCoronaCase.objects.filter(id=kwargs['id']).first()
            if submitted_corona_object:
                try:
                    corona_object = CoronaCase.objects.create(
                        affected=submitted_corona_object.affected,
                        death=submitted_corona_object.death,
                        recovered=submitted_corona_object.recovered,
                        district=submitted_corona_object.district,
                    )
                    return UpdateSubmittedCoronaCase(status_code=UPDATED_SUCCESS_CODE,)
                except Exception as e:
                    return UpdateSubmittedCoronaCase(status_code=UPDATED_ERROR_CODE,)


class TodayTotalCoronaCase(graphene.Mutation):
    affected = graphene.Int()
    death = graphene.Int()
    recovered = graphene.Int()
    status_code = graphene.String()

    class Arguments:
        test = graphene.String()

    def mutate(self, info, *args, **kwargs):
        today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
        today_total_corona_case = CoronaCase.objects.filter(updated_at__range=(today_min, today_max)).aggregate(Sum('affected'), Sum('death'), Sum('recovered'))

        return TodayTotalCoronaCase(
            affected=today_total_corona_case['affected__sum'],
            death=today_total_corona_case['death__sum'],
            recovered=today_total_corona_case['recovered__sum'],
            status_code=FOUNDED_SUCCESS_CODE,
        )


class TotalCoronaCase(graphene.Mutation):
    affected = graphene.Int()
    death = graphene.Int()
    recovered = graphene.Int()
    status_code = graphene.String()

    class Arguments:
        test = graphene.String()

    def mutate(self, info, *args, **kwargs):
        total_corona_case = CoronaCase.objects.aggregate(Sum('affected'), Sum('death'), Sum('recovered'))

        return TotalCoronaCase(
            affected=total_corona_case['affected__sum'],
            death=total_corona_case['death__sum'],
            recovered=total_corona_case['recovered__sum'],
            status_code=FOUNDED_SUCCESS_CODE,
        )


class Mutation(graphene.ObjectType):
    create_submitted_corona_case = CreateSubmittedCoronaCase.Field()
    update_submitted_corona_case = UpdateSubmittedCoronaCase.Field()
    today_total_corona_case = TodayTotalCoronaCase.Field()
    total_corona_case = TotalCoronaCase.Field()