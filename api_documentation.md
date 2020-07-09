# Documentation for APIs


1.  **API to fetch all and completed objectives.**

    End Point: /analytics/objectives/on-track/
    Method: GET

    Description:
    Gives count of total no of objectives till date and total no of completed objectives.

    Sample Response:

    {
        "total_objectives": 3,
        "total_completed_objectives": 2
    }



2.  **API to fetch all departments.**

    End Point: /analytics/departments/
    Method: GET

    Description:
    Gives list of departments with their details.
    THE RESPONSE IS PAGINATED.

    Sample Response:

    {

        "count": 3,
        "next": null,
        "previous": null,
        "results": [
            {
                "department_id": "1",
                "name": "Product",
                "location": "Bengaluru",
                "date_of_innaugration": "2019-07-01",
                "total_no_of_employees": 2,
                "total_no_of_objectives": 1
            },
            {
                "department_id": "2",
                "name": "Engineering",
                "location": "Redwood City",
                "date_of_innaugration": "2019-07-01",
                "total_no_of_employees": 2,
                "total_no_of_objectives": 2
            },
            {
                "department_id": "3",
                "name": "Marketing",
                "location": "New York",
                "date_of_innaugration": "2019-07-01",
                "total_no_of_employees": 0,
                "total_no_of_objectives": 0
            }
        ]
    }



3.  **API to fetch Department Details**

    End Point: /analytics/departments/<pk>/
    Method: GET

    Description:
    Gives details of a particular department requested.

    Sample Response:

    {

        "department_id": "1",
        "name": "Product",
        "location": "Bengaluru",
        "date_of_innaugration": "2019-07-01",
        "teams": [
            {
                "team_id": "3",
                "team_lead_id": "487",
                "department": "1",
                "team_lead": null
            },
            {
                "team_id": "1",
                "team_lead_id": "1",
                "department": "1",
                "team_lead": {
                    "user_id": "1",
                    "full_name": "Navneet Menon",
                    "first_name": "Navneet",
                    "last_name": "Menon",
                    "team": "1"
                }
            }
        ]
    }
