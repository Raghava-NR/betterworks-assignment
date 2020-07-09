# core imports
from rest_framework import viewsets
from django.db.models import Prefetch
from rest_framework.decorators import action
from rest_framework.response import Response

# project imports
from analytics.models import Department, Teams, Objectives
from analytics.serializers import DepartmentSerializer


class DepartmentViewSet(viewsets.ReadOnlyModelViewSet):

    """
    API endpoint that allows Departments to be viewed.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_queryset(self):

        """
        Overriding the default get_queryset to reduce unnecessary calculations.

        :return: queryset
        """

        if self.action == 'list':

            """
            If the action is list we need total_no_of_employees and total_no_of_objectives
            """

            query = self.queryset

            # annotating total_no_of_employees
            query = Department.annotate_total_no_of_employees(query)

            # annotating total_no_of_objectives
            query = Department.annotate_total_no_of_objectives(query)

            return query

        elif self.action == 'retrieve':

            """
            If the action is retrieve we need teams and their details
            """

            query = self.queryset

            # Pre-fetching teams to avoid multiple DB calls
            teams_q = Teams.objects.all()

            prefetch_obj = Prefetch('teams', queryset=teams_q)

            query = query.prefetch_related(
                prefetch_obj
            )

            return query

        return super().get_queryset()


class ObjectivesViewSet(viewsets.ViewSet):

    @action(detail=False, methods=["get"], url_path="on-track")
    def on_track(self, request):

        """
        To get details required for on-track objectives.
        :param request:
        :return:
        """

        total_objectives = Objectives.objects.all().count()

        total_completed_objectives = Objectives.total_completed_objectives()

        return Response({'total_objectives': total_objectives, 'total_completed_objectives': total_completed_objectives})


