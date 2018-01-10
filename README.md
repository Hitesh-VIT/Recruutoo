##INTRODUCTION
#Recruutoo- 
A job CMS maintained for creating beautiful job profile pages for different organizations. The application have multiple modules and features which could a help a non-tech person to beautifully design his/her organization job careers page using the tools and formatting available. The application also involves a feature where candidates can register for a job and provides a dashboard for organizations to keep track of the candidates and fix meetings and send email. The login process involves normal login module with email verification  as well as Google O-auth for ease of usage. The web application have built in support for sending SMS using sendgrid account for email verification and sending information to candidates applying for job.The application have been created to provide an easy support mechanism to small organization to create beautifully designed web pages for their careers portal as well as access control and dashboard giving flexibility and maintenance simultaneously.
# The modules in the application could be
1. Login
2. Sign-Up using email Verification
3. Google O-Auth
4. Dashboard 
5. Candidates Form6. Adding a Job form
7. Fixing meetings
8. Adding feedback for a candidate
#The application uses the following technology:
- Django -Python for backend
- AngularJS for front-end rendering
- Sqllite(Could be modified for MySQL or Postgres )
- Google-Outh-SDK
- Sendgrid Python SDK
- DRF
###Methodology:
The application for backend uses Django-a python based framework  and Angular JS for connectivity. A rendering language like AngularJS is important to provide a bridge between back-end and HTML.Django following  ORM queries can support multiple database for same code, hence sqlite,MySQL,postgres could be used.The Google O-Auth and sendgrid python API is used to integrate them with the django framework in the backend. HTML5 and Bootstrap is used in front-end to provide a responsive layout for the in-general user.
