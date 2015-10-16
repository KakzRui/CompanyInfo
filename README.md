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
