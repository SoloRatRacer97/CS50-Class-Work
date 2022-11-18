-- Keep a log of any SQL queries you execute as you solve the mystery.

-- See what I'm up aginst:
SELECT * FROM crime_scene_reports;


-- Theft took place on July 28th
-- Took place on Humphrey Street

-- Identify: Who they were, where they went, and whos the accomplice

-- See what crime report was on the 28th
SELECT description FROM crime_scene_reports WHERE street = 'Humphrey Street' AND day = 28 AND month = 7;
-- Theft of the duck happened at 10:15AM at the bakery. All three witnesses mention the bakery

-- See what happened at the bakery at that time
SELECT activity FROM bakery_security_logs WHERE day = 28 AND month = 7;
-- Thought these might have video descriptions, they do not...

-- See what each person said
-- Dont know the year, but it looks like the person we are after will be reffered to as "thief" so we can search on that to narrow things down.
SELECT transcript, name FROM interviews WHERE day = 28 AND month = 7 AND transcript LIKE "%thief%";
-- Eugene saw the theif at the ATM earlier that morning on Leggett Street
-- Raymond heard the theif was going to take the ealiest flight out tomrrow, the 29th. Talking on the phone at that time too
-- Ruth thinks we should check the security footage.

SELECT license_plate FROM bakery_security_logs WHERE day = 28 AND hour = 10 AND minute < 25 AND minute > 15;


