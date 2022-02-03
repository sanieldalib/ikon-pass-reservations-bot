# Ikon Pass Reservations Bot
This bot was written to make reservations for various Ikon Pass ski resorts during the 2020-2021 season. Many resorts required ski and parking reservations at that time due to COVID.

## Resorts Supported
* Winter Park
* Copper
* Eldora
* A-Basin

Parking is also supported at all of these resorts.

Other Ikon Resorts can be added trivially, and parking can be added for any resort utilizing Parkwhiz.

## Feature List
* Colorado Resorts
    * Ski Reservations
    * Parking Reservations
* Twilio SMS Notifications
* Dockerize Chrome Driver

## Running
* Create a `.secrets` file with the following variables:
    ```
    export IKON_EMAIL=<ikon_email>
    export IKON_PASSWORD=<ikon_password>
    export TWILIO_SID=<twilio_sid>
    export TWILIO_TOKEN=<twilio_token>
    export TWILIO_PHONE=<twilio_phone>
    ```
* Run `make install` to build locally or `make build` to build a docker container
* Run `make run` or `make run-docker`