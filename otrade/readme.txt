Automating Daily and Weekly Reports

Data

Data is currently produced by the daily-cases-export found in repository 
https://github.com/Twiage/daily-cases-export
This gets run once daily and sends a csv file to dailyreports@twiagemed.com
The csv file is produced by a ruby script that pulls the data from our production MongoDB database.

Currently the csv file is manually loaded into Excel by the Cursomer Success team and some further
manual processing is used to produce and send the daily reports.

Currently weekly reports use the same csv file using Tableau to produce the Weekly report.

Objective:  Eliminate the manual processing and produce all reports automatically.

To improve data querying we are loading the data into a Postgres relational database.
Initially we are just importing the daily CSV but eventually we wany the daily-cases-extract
to insert it directly or we can query the data directly from MongoDB.  
Eventulally we would prefer to have a relation database on our server to support reporting
needs.

To load data:
  1) Download CSV file from email into files_to_load directory.  Note: The email contains 
  files from production, demo, and staging environments all with the exact same filename.
  Be sure to only download the file from production, typically identified by it being the 
  largest one.
  2) Run  load_case_files.sh 

To run daily EMS reports:


To run Daily Hospital reports:

