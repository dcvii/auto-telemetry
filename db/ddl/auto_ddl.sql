

create schema if not exists auto;

CREATE TABLE auto.vehicle_data (
        vehicle_id varchar(50) ,
        auto_name VARCHAR(50),
        auto_registration_ts timestamp
    );

    CREATE TABLE auto.engine_data (
        Vehicle_ID VARCHAR(50) ,
        engine_ts TIMESTAMP ,
        engine_rpm numeric ,
        engine_temperature numeric ,
        fuel_consumption numeric
    );

    CREATE TABLE auto.location_data (
        Vehicle_ID VARCHAR(50) ,
        location_ts TIMESTAMP ,
        GPS_Location varchar(50) ,
        Odometer_Reading numeric
    );


    CREATE TABLE auto.tire_battery_data (
        vehicle_id VARCHAR(50) ,
        tire_battery_ts timestamp ,
        tire_pressure varchar(250) ,
        battery_voltage numeric
    );

    CREATE TABLE auto.Brake_Diagnostics_Data (
        Vehicle_ID VARCHAR(50) ,
        brake_ts TIMESTAMP ,
        Brake_Status BOOLEAN ,
        DTCs varchar(1000)
    );

    CREATE TABLE auto.Crash_Data (
        Vehicle_ID VARCHAR(50) ,
        crash_ts TIMESTAMP ,
        Crash_Impact_Data varchar(1000)
    );


    create table auto.ev_registration (
        state varchar(50),
        reg_count_2020 int,
        pct_reg_count_2020 numeric,
        re_count_2021 int,
        pct_reg_count_2021 numeric,
        you_growth numeric
    );


    CREATE TABLE auto.ev_registration_src
(
    state varchar(50),
    reg_count_2020 varchar(50),
    pct_reg_count_2020 varchar(50),
    re_count_2021 varchar(50),
    pct_reg_count_2021 varchar(50),
    you_growth varchar(50)
);