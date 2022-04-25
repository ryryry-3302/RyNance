# ​RyNance

## ​Intro 
  
Hi my name is Ryan and welcome to my first project, [RyNance](https://rynance.herokuapp.com/). RyNance is a web application aimed at helping Singaporean youth gain interest in Financial Planning and Financial literacy. RyNance is also my final project for CS50x 2022 :D [Demo](https://www.youtube.com/watch?v=oRNyVDiBEtg)


![screencapture-rynance-herokuapp-2022-04-06-16_24_25](https://user-images.githubusercontent.com/80184478/161930335-1aa2ef49-fba0-4937-942d-6e99e1d1495c.png)

![screencapture-rynance-herokuapp-2022-04-06-16_23_51](https://user-images.githubusercontent.com/80184478/161930347-8b24c149-05d0-46ba-9e69-def539e6881a.png)


## Overview

- ### The Code
  - RyNance is a web application designed using Python for the backend and HTML,
CSS and JavaScript for the frontend. I've also implemented the Flask and Bootstap
Frameworks for the frontend and backend respectively 


  - The application is comprised of a little over 1000 code with the vast majority
Being made up of HTML

 - ### The Features

   1. #### Login / Register / Change Password
      ![register](https://user-images.githubusercontent.com/80184478/161922643-6317a9a8-c511-4533-842f-e77df1bd6a6a.png)
    - The account registration and login functionality is made using the Flask and Flask Sessions library
using the skills taught in PSet 09 of CS50x 2022 Finance. 
    - I also used the werkzurg library to hash passwords and check passwords to save in the project database. Ontop of having prechecks for malicious inputs in account registration and login, the backend 
is also written to prevent any SQL injection attacks making use of lessons taught in CS50.



   2. #### Calculate
      - The first feature available to the user is calculate which comprises of 3 different calculators

        - [x] planning for Retirement
        - [ ] Mortgage 
        - [ ] Vacation trip. 

      ![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/80184478/161925384-d65db675-9bf6-4788-b78e-583fc2e1a8a3.gif)




      - The page is stylised using a carousel from the bootstrap framework.
And the calculators are made dynamically to automatically update with user input through using JavaScript and the JQuery library.

      - In the future I could probably implement a chart to illustrate the growth of the retirement portfolio
through use of the Chart.js library which I learned to use for a later function, Budget

   3. #### Budget
      - Budget is a simple tool to help the user have a quick visualisation of how much money they spend in each category, designed for Singaporean university students
in mind.

      ![ezgif com-gif-maker (2)](https://user-images.githubusercontent.com/80184478/161924929-c0e418ed-c4c7-405c-b5c1-2ab9ecfed0af.gif)

      - The app is made dynamically using JavaScript, Jquery and Chart.js to automatically
update a piechart that moves automatically as the user inputs their data to the form.

   4. #### Learn
      - Learn is a hub of information for the user to explore extensive resources on 
improving personal finance and financial literacy. 
      ![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/80184478/161925698-9c81da16-f406-44b7-bd08-89f2fb88c6c9.gif)
      - In learn I make use of various features from BootStrap to present the resources in 
aan aesthetic manner using the components navbar, tabs and lists
      - I also make use of `<iframe>` to embed external sources from the r/singaporeFI subreddit.
      - Lastly, I also used JavaScript to include a searchbar to query for the definition
of financial terms/ jargon on Investopedia directly from my website.

   5. #### Compare
       - Lastly, Compare (a function probably most appealing to my target users) is a function
which helps users search for undergraduates salaries in different courses across the top universities in Singapore, and
Ccompile a list of undergraduate programs of their interest for easy comparison.

       ![ezgif com-gif-maker (5)](https://user-images.githubusercontent.com/80184478/161926536-29e589e3-6acd-4352-9f9b-4cf170975b6f.gif)

       - Compare uses a search bar to collect the users input. Afterwards, this information is sent to the backend using POST.
In the backend in `helpers.py` I added a function which sends the query to Data.gov.sg (The local government API which hosts a large amount 
of data for free), before filtering out the resultant JSON for the relavant data I need and only collecting the most recent
salary data.

## Deployment
- After completing the code, I deployed my project onto Heroku and it can be accessed here rynance.herokuapp.com on both mobile and desktops as
the website is made responsive through use of Bootstrap. I'd like to extend my gratitude to the CS50 staffs help through the CS50 guide to using Heroku on the Docs as well the r/CS50
subreddit for being a great help to troubleshooting deploying. Find it here https://rynance.herokuapp.com/

- ### Some of the things I had to learn for successful deployment
     - Changing my project.db to use postgress
     - Adding a Procefile (and the fact that it's case sensitive) to force heroku to run gunicorn

## Conclusion
- With the app complete and fully functional and hosted on Heroku (Finally). I am happy albeit sad to say this marks the end of my CS50x project as well
as time doing the course.

## Acknowledgements
- I'd like to take the time to extend my gratitude to all the people who helped make this project possible.
  - David J Malan for his amazing lectures for CS50x 2022
  - The CS50 staff for their invaluable resources like the seminars for using git, setting up vscode and help in the discord server especially staff CuriousKiwi 
  - w3schools
  - http://fireagecalc.com/ for the inspiration for the design of my own calculator
  - The open source community with the invaluable libraries of Bootstrap 5 and Chart.Js
  - and lastly the r/CS50 community
  - -hi :D

