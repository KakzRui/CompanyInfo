# CompanyInfo
CompanyInfo is developed using Python, django REST Framework on server side and client side as AngularJs, Backend is Mysql.

What exactly this project is?
It allows the user to add Company and company details.
User can update the company information.
User can delete a company and its details.
It displays the list of Companies and its details.

Below are the steps to run curl

For GET
curl -i -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/api/companylist/

For POST
curl -i -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/api/companylist/ -d '{"company_id":106,"name":"EuroCouriers","address":"5th Street","city":"Oslo","country":"Norway","email":"eurocouriers@mail.com","phone":5133232323454}'

For PUT
curl -i -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/api/companylist/1/ -d '{"id":1,"company_id":100,"name":"SeasonTravels","address":"8th Street","city":"Stockholm","country":"Sweden","email":"seasontravels@mail.com","phone":62332323454}'

For DELETE
curl -i -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/api/companylist/15/

Below are the applications installed for this project.

Python 2.7.6
django version - 1.7.5
djangorestframework - 3.0.5
Mysql 5.6.2
