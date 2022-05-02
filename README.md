# Dodgy Dealership Application

- This Application allows people to list their car and buyers can show their interest.

- To Build the docker container run:
    * `make build`
        * This makes the docker cotainer and created dummy data and creates an admin account for Iron Mike
        * username: mike@example.com
        * password: mikeymike123
- If you don't have the make command you can check the commands that used with build
- To start the application 
    * `make run`
    * If you don't have the make command you have to run.
        * `docker-compose up`
    
- To stop the application
    * `make kill`

- To delete and clean the container
    * `make clean`

- To run the test cases
    * `make test`

- To check the coverage
    * `make coverage`

- To check the code quality
    * `make code_quality`
