from django.db import models
from django.db.models import Case, When, Count, IntegerField, F, Value, CharField


class Department(models.Model):

    """
    Model class representing `Department` Table
    """

    department_id = models.CharField(max_length=15, default=None, blank=True, primary_key=True)
    name = models.CharField(max_length=15, default=None, blank=True)
    location = models.CharField(max_length=20, default=None, blank=True)
    date_of_innaugration = models.DateField(default=None)

    class Meta:
        db_table = 'department'

    def __str__(self):
        return str(self.name)

    @staticmethod
    def annotate_total_no_of_employees(query):

        """
        annotates total_no_of_employees to the queryset
        :param query:
        :return: queryset
        """

        query = query.annotate(total_no_of_employees=models.Count('teams__users'))

        return query

    @staticmethod
    def annotate_total_no_of_objectives(query):

        """
        annotates total_no_of_employees to the query
        :param query:
        :return: queryset
        """

        query = query.annotate(total_no_of_objectives=models.Count('teams__users__objectives'))

        return query


class Teams(models.Model):

    """
    Model class representing `Teams` Table
    """

    team_id = models.CharField(max_length=15, default=None, blank=True, primary_key=True)
    team_lead_id = models.CharField(max_length=12, default=None)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='teams')
    average_pay = models.CharField(max_length=10)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return str(self.team_id)

    @property
    def team_lead(self):

        """
        Property to get team lead user object
        :return: Team lead <User object>
        """

        return Users.objects.filter(user_id=self.team_lead_id).first()


class Users(models.Model):

    """
    Model class representing `Users` Table
    """

    user_id = models.CharField(max_length=15, default=None, blank=True, primary_key=True)
    first_name = models.CharField(max_length=25, default=None)
    last_name = models.CharField(max_length=25, default=None)
    team = models.ForeignKey(Teams, on_delete=models.PROTECT, related_name='users')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return str(self.full_name)

    @property
    def full_name(self):

        """
        Property to get the user's full name.
        :return: User's full name <str>
        """

        return '{} {}'.format(self.first_name, self.last_name)


class Objectives(models.Model):

    """
    Model class representing `Objectives` Table
    """

    objective_id = models.CharField(max_length=15, default=None, blank=True, primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.PROTECT, related_name='objectives')
    objective_text = models.CharField(max_length=100, default=None, blank=True)

    class Meta:
        db_table = 'objectives'

    def __str__(self):
        return str(self.objective_id)

    @staticmethod
    def annotate_status(query):

        """
        annotates status to the query

        Assumption Taken:
        If there are no keyResults present for a particular objective,
        then the objective's status is assumed to be Complete.

        we can change the above consideration with a small check in the case when below
        i.e
        Case(
                When(Q(total_key_results=F('completed_key_results'), total_key_results__gt=0), then=Value(KeyResults.status_choices[1])),
                default=Value(KeyResults.status_choices[0]),
                output_field=CharField()
        )

        :param query:
        :return: queryset
        """

        query = query.annotate(
            total_key_results=models.Count('key_results'),
            completed_key_results=models.Count(
                Case(
                    When(key_results__status=KeyResults.status_choices[1], then=1),
                    output_field=IntegerField()
                )
            )
        )

        query = query.annotate(
            status=Case(
                When(total_key_results=F('completed_key_results'), then=Value(KeyResults.status_choices[1])),
                default=Value(KeyResults.status_choices[0]),
                output_field=CharField()
            )
        )

        return query

    @staticmethod
    def total_completed_objectives():

        """
        calculates total_completed_objectives
        :return: total_completed_objectives <int>
        """

        query = Objectives.objects.all()

        query = Objectives.annotate_status(query)

        query = query.filter(status=KeyResults.status_choices[1])

        return query.count()


class KeyResults(models.Model):

    """
    Model class representing `KeyResults` Table
    """

    status_choices = ('Pending', 'Complete')

    keyresult_id = models.CharField(max_length=15, default=None, blank=True, primary_key=True)
    objective = models.ForeignKey(Objectives, on_delete=models.PROTECT, related_name='key_results')
    status = models.CharField(max_length=12, default=None)

    due_date = models.DateField(default=None)

    class Meta:
        db_table = 'keyresults'

    def __str__(self):
        return str(self.keyresult_id)



