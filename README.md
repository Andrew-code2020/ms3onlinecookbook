# Temple Lean Recipes

## Executive Summary 
The Temple Lean Recipe website is designed for people who are members of the Temple Lean Gym who are looking to eat the right type of food to back up their fitness routine in the Temple Lean gym

The recipe categories on offer are below ;

1. Breakfast 
2. Lunch 
3. Dinner
4. Snacks


The problem that we are trying to solve is that current Temple Lean members are trying to eat the right food and drink to back up their work in the gym but they get conflicting advice on when they do research onlinen or when chatting with friends.
They also lack a social support network to encourage them to eat the best quality food. 
We set out to bring Temple Lean gym members into a community of their peers that contained the best advice on food and drink to help them get the most quality from of their gym membership at Temple Lean gym. 
The above named meal types are four strategically valuable markets. They are how people understand food at a glance. We have designed the website to offer bitesize information on the best quality recipes in these four categories. 
The success of this website is that the user is able to locate the type of recipe they want quickly and easily without having to sift through the large amount conflicting information in other areas fo the web. 

Further success will be measured by the number of Temple Lean members who sign up to the Temple Lean Recipes website.   

### UX

The key reasons for producing the website were to;

- help current gym members get the best quality recipes from their trusted Health professionals at Temple Lean Gym
- help members easily access 4 common recipe categories
- help integrate new and current members into a community where they
  - support each other on their nutritional journey
  - add recipes they have used themselves
- help members share recipes they find useful and over time let them build an environment that they feel they have all the nutitional information they need in one place. 
- In the future help Temple Lean attract and retain online subscription members 

At the outset the minimum viable product was determined to be a community platform whereby the operator(s) of the Temple Lean and Temple Lean Recipe website add a source of basic information about healthy food recipes and begin to build a social support amongst members in a nutritional setting.
It was an objective of this project to include an intuitive design which would allow new and current clients to navigate and enagage with the website without any prior experience of Temple Lean the gym facility or even a high level of knowledge about healthy food recipes. 
Current and potential client surveys were conducted to assess the minumim effective information required to illicit a positive emotional response from users.
This information was incredibly valuable during the construction of wireframes for the website. 

At the outset conventional web design features were favoured because we wanted everyone from the novice to the accompolished web user to feel like they were still in a familiar place on the web. 
The vision for the project was to have a website that;

- create basic information that the user could read about healthy food recipes 
- Allow users to add recipes they feel have benefitted them for others to use
- Allow users to modify the recipes they created they feel have benefitted them for others in case they discover new information about a recipe
- Allow users to delete recipes they created should they feel that they are no longer useful
- Offer a route to finding out more about Temple Lean the fitness facility

Further objectives included;
- implementing interactive features on the Temple Lean Recipes website to help the user feel they were unlocking short manageable amounts of information about healthy food recipes.


##### Strategy Plane - Business Strategy

What are you aiming to achieve? 
Users are looking for; 
- A place to find guidance on the Nutrition programme they received at the gym
- A clear set of instructions to make the recipes
- A place for users to create, read, update and delete their recipes they have found useful and want to share with others. This based on research will help the user/client feel at home in the Temple Lean community.

Business wants the client to;
- Find recipes that support their Health, Lifestyle and Fitness Goals so they stay within the Health and Fitness community

Review the competition - Is someone else already doing it?
- a review of the market suggested that this was a new or under developed idea offering Gym members a place to go to for Nutrition Advice and recipes. A review of the businesses below showed little or no area for members to find the correct recipe advice from their trusted health and fitness provider
 Businesses reviewed
 - https://www.mardykearena.com/
 - https://www.dennehys.ie/
 - https://www.energiefitness.com/midleton
 - https://onelifefitness.ie/

Stakeholder interviews
- conversations with Health and Fitness Club owners and Health and Fitness clients suggested that joining the exercise and nutrition component in an easy to use platform was the correct approach to take.

Who else is doing this?
- Very few providers are known to be providing an area that

What are the pros of what they're doing
- Client benefit  

What are the cons?
- Unknown how to monetize this area of the business. What do we charge for this service? Market research suggested that we should build this into membership in some way.

What are the competition missing?
- The connection this area offers

What are they doing, but they could be doing better?
- they providing the facility and knowledge to  particpate in regular exercise

User interviews (What a user thinks they need may not be exactly what they need?)
- User interviews suggested they wanted a lot more focused recipe suggestions like muscle building recipes or endurance programme recipes
- In tihe same interviews the user would often sight struggling with what they should eat for breakfast or dinner.
- Also the first time user was very unlikely to join the Temple Lean community if the recipes weren't accessible on a basic level. The user understood that recipes were for breakfast in the breakfast section but when presented with a Muscle Building recipe section most users were unsure if they could use these recipes or they felt this was too advanced for them.
- The conclusion the developer drew from these interviews was that we should start basic and progress to more advanced recipe recommendations if a clearer market emerged. 

Would you use this and why? 
- I would use the recipe website because I like the idea of my Health and Wellness resources being in one place provided by people I trust.

Who is our target audience? 
- This project is primarily a consumer business to customer servcie (B2C) 
- We noted the potential for business to business B2B partnerships later but accepted that this was not within the current scope of the business strategy plan because we need a viable product before opening discussions with another business.
- Our aim was to access easier clients we already have but leave the door open for other clients to join us 
- Out thoughts were that our currents wouldn't need much justifcation to purchase a new offering from us given our existing relationship and the trust we have built up over many years.

What makes a good recipe website experience?
Following reserach we settled on the points below as a good recipe website experience
- Intuitive design (Simple Navigation)
- Clean, attractive layout with point and clicks revealing information slowly in an easy to understand readable format
- Blog (Users liked to read about recipe experiences or other health and fitness related experiences)
- Users can create, read, update and delete their own recipes and interact with other members(future development) 
- Pictures
- Videos (This was placed in future development plans)
- Pricing transparent (3 step purchase - This was placed in future development plans) 


##### Scope Plane 
Features we wanted to include in our design

- Colour light background generally white then strong font and color
Basic Observations
 - Navbar 
   - Two tiers
   - Includes Navigation for following items
   - Breakfast (Left revealed after log in)
   - Lunch (Left revealed after log in)
   - Dinner (Left revealed after log in)
   - Snacks (Left revealed after log in)
   - Search (Right revealed after log in)
   - Testimonials (Opportunity to Card Flip js)
   - Register/Login (Right and collapsible) then reveals, profile and log out and recipe navbar

Section

- Home/Landing Page Body (Hero image photo options))
- CRUD Functionality to be available in 
  - Profile
  - Breakfast 
  - Lunch 
  - Dinner 
  - Snacks

Cards with Photo Gallery
  - Breakfast 
  - Lunch 
  - Dinner 
  - Snacks

Card flip - Testimonials

Footer    
 - Social Media Icons wired up Facebook. Instagram, Twitter(my ones) (Left) 
 - Gap in Center
 - Blog entries (Right)

Data Schema - Database Mongo DB

User information
- Object Id
- Username
- Name
- Email 
- Password Werkzeug 

Lean Recipes
- Object Id
- Meal Type
- Meal Name
- Meal Image
- Instructions 
- Ingredients
- Method
- Required Tools
- Nutritional information (Format opportunity to display creativity - Traffic light healthy range of macronutrients)
  - Kcals
  - Carbs
  - Protein
  - Fats

Recipe types
- Object Id
- Breakfast 
- Lunch 
- Dinner 
- Snacks


###### User Story 1 (Registeration)

I am a currently a member of Temple Lean Gym. Following a conversation with a friend about diet and exercise my friend recommends that I check out a new website named "Temple Lean Recipes". I search the web find the Temple Lean Recipes website. 
I register and I click on the option 'Dinner' because I have always had trouble cooking healthy dinner recipes. I click on a recipe I am interested in through the collapsible buttons on the page and the collapsible feature reveals information in a
step wise manner that allows me to learn what I need to know about how to make the recipe as well as other information.

###### User Story 2 (Editing my profile)

I have regsitered for Temple Lean Recipes. My email provider has decided to charge me a monthly fee to continue using my email address. I have gone ahead and changed to a new email provider. I want to update my email on the Temple Lean Website. I log in to the Temple Lean Website. I am brought directly to my profile page. I click on the update profile section. I make my updates to the email section and then click update profile. The screen flashes a message updated successfully. I can also see the updates rendered on the form in front of me. I then click profile on the top left of the screen to bring me back to my profile page where I can also review the update I have put in place.
 

###### User Story 3 (Creating Recipes - Flash message please send recipe image suggestion to email address)

I am registered and logged in at Temple Lean Recipes. I have use a recipe that I wish to add to the community. I select the category (Breakfast, Lunch, Dinner or Snacks) I click the add recipe button and enter the form details siting Breakfast as my recipe category. When I click the add recipe button I see a flash message stating "Recipe added to Temple Lean Recipes Successful!". I am redirected to my profile where I click on Breakfast and scroll down to see my recipe and the information I put input on the form earlier. I spot and error so click edit recipe. I notice that I can edit this recipe but not any other recipes. I make my edits hit update and then review my updates as before on the breakfast page.

###### User Story 4 (Log out)

##### Structure Plane
In development we set out to make sure that our site would be consistent. We used the categories below to describe our efforts
 - Predictable
   - To make the website predictable we used the same materialize cards for Breakfast, Lunch, Dinner and Snacks
   - We used similar forms to register,, to log in, create profile information, create recipe information, update profile information and update recipe information.  
 - Learnable
   - We used collapsible 
 - visible 
 - Clear and intuitive feedback

###### User Questions

- Where am I?
  - On each page the Navbar highlights that page in golden rod yellow. This helps you locate where you are on the  site

- How did I get here?
  - Clicking on certain icons opens up new Tabs so the user does not forget which website they accessed the content from such as  social media platforms. The platforms are currently connected to the developers account because the  social media accounts do not exist 
  - The navbar and footer are the exact same on each page and with the current page highlighted in golden rod yellow in the navbar so that the user may easily identify where they are and where they came from
  - The alert bar on the FAQ page has a COVID-19 alert providing users with the most to up to date travel information from the Government of Ireland. It opens into a new tab such that the user knows which website they came from

- What can I do here?
  - The user is invited clearly to click on and then access various features of the  website. 
  - This occurs in the following places;
     - Navbar with the hover feature
     - Footer via the social media icons
     - The contact us page Submit your  form button
     - The buttons under the flip cards toggle to reveal basic information 
     - The user can also click on the bottom left footer icons which directs the user to resources that helped make the website
     - The FAQ button contains a button to the left of the text which toggles to reveal more text content on the chosen subject area
  - The user may hover the cursor over the pictures on the Learn about Ireland and Explore Ireland page to reveal options which present themselves as buttons which then toggle to reveal further text content.
 -
- Where can I go from here?
  - The navbar and footer are the exact same on each page (except the FAQ page where an alert bar offers a link to further information on travel advice) and with the current page highlighted in golden rod yellow. In the navbar the user is able to easily identify where they are and where they can go from here. 
  - The blue hover feature is also designed to indicate to the user that they can click on this icon/button/word in the navbar and access further content.
  - On the home page the cards (under the main hero image) when you hover the cursor over the grid panels the panel will turn green indicating that you may click here to reveal content. When the content is revealed the current panel which the content refers to is in golden rod yellow to help the user easily identify where they are on the page and which destination the infomration they are looking at is referring back too.

###### Skeleton Plane

Wireframe Pictures 

Route to wireframe pics in github repository https://marvelapp.com/67bec93

Desktop wireframes

- readmedocs/desktopwireframe/basetemplate.jpg
- readmedocs/desktopwireframe/landingpage.jpg
- readmedocs/desktopwireframe/loginpage.jpg
- readmedocs/desktopwireframe/paintlandingpage.jpg
- readmedocs/desktopwireframe/recipelooppage.jpg
- readmedocs/desktopwireframe/registerpage.jpg

Mobile/Tablet Device wireframe
- readmedocs/mobilewireframe/recipeloopmobile.jpg
- readmedocs/mobilewireframe/loginmobile.jpg
- readmedocs/mobilewireframe/profilemobile.jpg
- readmedocs/mobilewireframe/registertemplatemobile.jpg
- readmedocs/mobilewireframe/editrecipemobile.jpg

### Features

##### Summary

- Internal links
- External links
- Header
- Navbar
- Footer
- Section
- Dropdown Menu
- Collapsible
- Hover
- Flask
- Integrated with MongoDB
- Icons
- Jquery 
    - Collapsible
    - Sidenav 
    - Form Select



##### Existing Features

- Internal links to different parts of the Temple Lean Recipe website
- External links that open a new to different platforms such as social media, the developers Milestone 1 project website and the developers private blog. The social media accounts the developers Milestone 1 project website and the developers private blog are linked to the developers social media accounts to demonstrate the skill of adding external links.
- Header - Contains the Navbar design for desktop and mobile devices 
- Easy navigation - The Navbar at the top of each page is similar to conventional navbars of other recipe pages allowing the user an intuitive experience on a perhaps unfamiliar website. We maintained this navbar across each page using a base template for ease of navigation. The top part of the navbar including log in and registeration collapse on a mobile devices to a single apple icon which the user can click on. The navbar items Breakfast, Lunch, Dinner and Snacks appear after you register or log in. This was done to avoid overhwleming the user when they land on the page and guide them to log in or regsiter and then more content will be revealed. 
- Footer - Linked to some pages we used to develop the website and contains direct links to the developers Social Media platforms, Milestone 1 project and private blog. Temple Lean recipes social media specific to this site does not exist but is in future plans.
- Section - The middle section is where the block content Jinja template is injected. The content changes on each page and gives basic information on aspects of the Temple Lean Recipes site.
- Hero Image - The eye catching landing/homepage page is designed to convey to the user that they have arrived on a Temple Lean Recipes site as distinct from the gym site. 
- Select - We tried to use select options to allow a better visual experience for the user and to avoid long typed responses on the forms through out the website. 
- Hover 
   - social media icons all turn blue when the cursor hovers over them
   - internal links turn light black when the cursor hovers over them except for the homepage. 
   - external links do not have a hover
   - This lets the user know that there is more information they can access here if they click. It draws attention to options which keep the user on the Temple Lean Recipe page. 
- Icons - font awesome icons were used to add style and an intuitive feel to the user experience. 
- jQuery & JavaScript 
    - collapsible - On each recipes page clicking the on the Ingredients, Method, Tools or Nutitrional Information will open the collapsible revealing more content  
    - Sidenav - On Mobile devices the Navbar containing Login, Register and Logout collapses to an apple icon
    - Form Select - Forms are used throughout the page to allow users to register, login, update profiles, create recipes and update recipes
- CRUD Functionality
    - Create - Users can create a profile and create recipes on the Temple Lean Recipe website
    - Read - Logged in users can read recipes and their profile information on the Temple Lean Recipe site 
    - Update - Logged in users can update recipes they created and their profile information only on the Temple Lean Recipe site
    - Delete - Logged in users can delete recipes they created and their profile information only on the Temple Lean Recipe site


##### Features Left to Implement
- Search function
- Automatic image upload and rednering to the website
- Book and pay for a private Nutrition Consultation
- Analytics that show user traffic flow
- Testimonials from Users

### Technologies Used

- HTML5 - Used for structure and content of website
- CSS3 - Used for personalised custom built styling of website
- JavaScript - Used for email JS, Google Maps API and JS Tabs
- jQuery 
    - Used to deliver interactive features such as toggle and show and hide 
    - Website https://jquery.com/
- Materialize
  - Website https://materializecss.com/
  - Used to import generic styling
- Github and Gitpod
  - Website of Github repository https://github.com/Andrew-code2020/ms3onlinecookbook
  - Used to construct host and deploy the website
- Font Awesome
  - Website https://fontawesome.com/
  - Used to import icons
- Google Font
  - Website https://fontawesome.com/
  - Used to import font
- Code Validators
 - HTML - https://validator.w3.org/
 - CSS Validator - https://jigsaw.w3.org/css-validator/#validate_by_input
    - Result visible in readmedocs/testing/codevalidators/cssvalidatorresult.jpg
 - JavaScript and JQuery validator https://jshint.com/
    - Result visible in  readmedocs/testing/codevalidators/shintcheckresult.jpg
 - Python Validator http://pep8online.com/
    - Result visible readmedocs/testing/codevalidators/pep8vaildatorresult.jpg
-Flask
-Python
-MongoDB
 -Clusters
 -Collections to hold data input by the user and pass data to the appropriate page on the Temple Lean Recipe site
-Heroku for deployment
  - Website link to Heroku app https://lean-temple-recipes.herokuapp.com/ 
  - Used to deploy the website
-Dependencies (Also listed in requirements.txt file)
  -click==7.1.2
  -dnspython==2.0.0
  -Flask==1.1.2
  -Flask-PyMongo==2.3.0
  -itsdangerous==1.1.0
  -pymongo==3.11.1
  -Werkzeug==1.0.1


### Testing

Template
- Name of Test
- outline of Testing 
-test planning 
-implementation
-fix (if applicable)
-results
-outcomes

Template
- Name of Test JS File
- outline of Testing
  - The objective of the test was to check if the directory to the js file was working 
-test planning
  - Input code into recipe.js and check the developer tools specifically the console tab to check if the js file is rednering effects across the Temple Lean Recipes  
-implementation
  - In the recipe.js file we input the code  console.log('linked properly');
-fix (if applicable)
  - A fix was not necessary because the code worked 
-results
  - The results are available to view 
  - readmedocs/testing/jsfiletest/jsfiletestresult.jpg
-outcomes
 - Test successful. the words 'linked properly' appeared into console


- Name of Test JS file functionality
- Outline of Testing
  - Check that js code is producing functionality on the Temple Lean Recipe Website
- Test planning
  - Check the following js functionality
  - Collapsible - On each recipes page clicking the on the Ingredients, Method, Tools or Nutitrional Information will open the collapsible revealing more content. Does this happen?  
  - Sidenav - On Mobile devices the Navbar containing Login, Register and Logout collapses to an apple icon. Does this happen?
  - Form Select - The form select option is used across the site does the menu work and the options appear. Does this happen? 
- Implementation
  - Collapsible
    - collapsible class added to brekfast, lunch, dinner and snacks html pages
    - pertinent initialisation code added to recipe.js
  - Sidenav
    - check collapse to an apple on the right in Mobile device
    - Open deployed site https://lean-temple-recipes.herokuapp.com/
    - Ctrl+Shift+I on the keyboard
    - Select mobile device from responsive dropdown menu 
  - Form Select
    - Open deployed site https://lean-temple-recipes.herokuapp.com/
    - Go to the Register page
    - Check the Preferred Recipe Category
    - Click the dropdown carrot
    - See if options come up
     
- Fix (if applicable)
  - Collapsible
    - no fix neccessary
    - code was copied and extended to add more collapsible sections on the page
  -Form Select
   - We added disabled and selected attributes to ensure the register form was blank at first
   - We added the relevant for example value = "breakfast" to each option to ensure the that the option was passed and documented in MongoDB. 
  - Sidenav
    - To render the sidenav bar on the right of the page we added {edge: "right"} to the js code

- Results
 - Collapsible
   - Breakfast result image start readmedocs/testing/jsfiletest/jscollapsibleresult1.jpg
   - Click on Collapsible result image start readmedocs/testing/jsfiletest/jscollapsibleresult2.jpg  
 - Sidenav
   - Sidenav result image readmedocs/testing/jsfiletest/jssidenavresult1.jpg
   - Clicked through sidenav apple readmedocs/testing/jsfiletest/jssidenavresult2.jpg
 - Form Select   
   - Register page results readmedocs/testing/jsfiletest/jsselectformresult.jpg
   - Edit profile page resultss readmedocs/testing/jsfiletest/jsselectformresult.jpg
   - Edit recipe page results readmedocs/testing/jsfiletest/jsselectformupdatereciperesult.jpg
- Outcomes
   - Form Select
     - The tests lead to bug fixes and helped ad functionality without errors on the site
   - Collapsible
     - Checked collapsible  across breakfast, lunch, dinner and snacks and it worked
   - Sidenav
     - Side nav functionality worked and revealed sidenav elements

Template
- Name of Test Placeholder removed test
- outline of Testing 
 - The placeholder gave the site an unclear orange placeholder
 - Despite our attempts to modify the color we were unsuccessful so we removed the placeholder code across the site.
 - This had a minimum effect on the site style 
- test planning 
- implementation
- fix (if applicable)
- results
- outcomes

##### Performance Testing 
-Name of Test 
  - Lighthouse Test
-test planning 
  - Check the Temple Lean site for performance, best practices and accessibility. 
-implementation
  - access the deployed site via https://lean-temple-recipes.herokuapp.com/
  - Use Ctrl+Shift+I on your keyboard to access the developer tools
  - Click genereate report refer to image for visual detail readmedocs/testing/lighthouse/generatereportlighthouse.jpg
  - 
-fix (if applicable)
  - no obvious performance issues on mobile or desktop device according to the lighthouse test
-results
  - The lighthouse test results are documented in the images below 
    - readmedocs/testing/lighthouse/mobilelighthousetest.jpg
    - readmedocs/testing/lighthouse/desktoplighthouseresults.jpg
-outcomes
 - performance was optimum

Outline of Testing
 -Name of Test - Testing Base html 
-test planning
  -remove landing page code from base template
  -ensure Temple Lean site opens on homepage and base template is not rendered directly anywhere on the site  
-implementation
-fix (if applicable)
-results
  - 
-outcomes



-test planning 
    - Premise is our custom css file talks to our html files through python 
-implementation
    - At the beginning of the project we checked to see if the background color red appeared when we added background color red to style.css
-fix (if applicable)
    - not applicable code worked
-results
 - readmedocs/testing/testinglinkbetweenbasetemplateandcustomcss.jpg
-outcomes
 - test was successful



Testing Initial Python functionality 
- Subject Test app.py inital ran 
   - used python3 app.py to run the app.py file from gitpod
   - screenshots in readmedocs/testing/initalapppyrun.jpg
- Result
   - Hello World of Temple Lean Again appeared in the browser as expected
- Conclusion
  - initial set up worked well"

 Testing 
-test planning
   - Registeration form check the content renders on our app 
-implementation
   -used python3 app.py to run the app.py file from gitpod to visualise our registeration file
-fix (if applicable)
    - icons render on top of label text
    - to fix we placed the icons within the label element
-results
 -visually the icon and the label are no longer over lapping
-outcomes
  - Fixed a visual bug

##### Testing Browsers screens you tested it on

###### Chrome Browser
- I tested the website by copying and pasting the Heroku pages link https://lean-temple-recipes.herokuapp.com/ into Chrome Browsers
- I pressed control+shift+I to access developer tools in the Chrome Browser and checked the web pages responsiveness

###### Edge Browser
- I tested the website by copying and pasting the Heroku pages link https://lean-temple-recipes.herokuapp.com/ into Edge Browser
- I pressed control+shift+I to access developer tools in the Edge Browser and checked the web pages responsiveness


##### Testing Device screens
- I used the chrome developer tools to test that the websites appearance and functionality was available across multiple devices listed below;
  - Moto G4
  - Galaxy S5
  - Pixel 2
  - Pixel 2 XL
  - iPhone 5/SE
  - iPhone 6/7/8
  - iPhone 6/7/8 Plus
  - iPhone X
  - iPad
  - iPad Pro
- I checked the console in developer tools showed no errors on each page as I went through each page

##### Header

Navbar

- Go to the Temple Lean Recipe "Home/Landing" page or any other  page
- Verify that the home bar is highlighted in golden rod yellow.
- Verify that this current page feature of highlight in in golden rod yellow occurs across all pages in our navbar by clicking each one in turn

##### Footer

Social Media

- Go to the "Home/Landing" or any other page on the Temple Lean Recipe website
- Scroll down to the Footer
- Click on any social media icon
- Verify that a new tab opens on the correct (ie Facebook opens on Facebook) social media site
- The social media sites are the developers sites because the Temple Lean Recipe website doe not have stand alone social media

Developed with

- Go to the "Home/Landing" page
- Scroll down to the Footer
- Click on the bootstrap, jQuery or Code institute icons
- Verify that a new tab opens and the appropriate website opens

##### Header and Footer

- Across each of the  web pages you may verify that the Header and the Footer have the same features outlined above
- There is only one exception and that is the FAQ page where an alert bar is added above the main navigation bar to provide users with government of Ireland travel advice.

##### Section

- The section element changes it's content depending on which page you are on
- Below I have outlined briefly the testing on each section

#### Home/Landing page

Go to the "Home" page
- Verify that when you hover the cursor over any destination in the grid that the grid turns light green
- Click on any destination in the grid and verify that content pertinent to that destination appear below in a box with the destination turning golden rod yellow so the user knows which destination the content is referring too.  
- Click on each destination in the grid and verify that the exact same thing happens for each of the topics below;

#### Learn about Ireland page

Learn about Ireland

- Go to the "Learn about Ireland" page
- Verify that when you  hover over each picture the picture flips over and content buttons appear 
- Click  on each button to toggle the appearance of further information on each of the following topics
  

#### Explore Ireland page:

Explore Ireland page

- Go to the "Explore Ireland" page
- Verify that when you hover the cursor over the cards on the left hand side that cards turn over and reveal which location is matched to the google map markers visible on the map on the right hand side of the page
- You may verify that the information is different on each card

- Go to the "Explore Ireland" page
- Verify that when you hover the cursor over the cards on the left hand side that cards turn over and reveal which location is matched to the google map markers visible on the map on right hand side
- You may verify the marker by clicking on the appropriate section of the map. By clicking on the map you will zoom in on the location you are looking for.

#### FAQ page

FAQ 

- Go to the "FAQ" page
- Verify that when you click on the toggle button on the left next to the text that more content appears.
- The information is almost entirely fictional. The place names are real but the prices and activites are made up.

#### Contact Us

Contact us

- Go to the "Home/Landing" page.
- Click on the "Contact Us" section of the Navbar.
- Verify that we are directed to the contact us page which opens with a form to fill out.
- When you fill out the form and hit the "Submit your " button the form when a message "please fill out this field appears" if you do not submit a first name.
- The contact us form is functional at this time and completed forms will be sent to burnsad@tcd.ie.
    - a photo is available of a test email sent from the form is available in the following directory assets/readmedocs/emailjs/emailjs.jpg
    - the {{from_email}} is set up in the cc of emailjs so the user gets a copy of the submitted form such that they know that the form has gone through to the  team. 
- The form is coded such that it will empty when the "Submit your " button is pressed. 

#### Appearance differences on other devices

- On small mobile devices such as phones the navbar will collapse into a black cog wheel icon.
- The programming of the website allows it to adjust column widths on smaller devices and stack elements in a display to fit different browsers mentioned earlier and different devices mentioned earlier. The most obvious examples are the navbar which becomes a drop down menu and stacks on top of itself and the footer which stacks on top of itself and allows the user to scroll down. 
- The Project was built with mobile first design principles

#### Code Validation
I used the following code validators to help me debug my code

- Code Validators
 - HTML - https://validator.w3.org/
 - CSS Validator - https://jigsaw.w3.org/css-validator/#validate_by_input
 - JavaScript and JQuery valiadtor https://jshint.com/

I also used following website to help me correct any formatting anomalies in my code
- https://codebeautify.org/ 

#### Bugs

Change Go to Recipes to Breakfast recipes and Renders better on Mobile device

- Bug  Placeholder  
 - The placeholder gave the site an unclear orange placeholder where the placeholder should be
 - Despite our attempts to modify the color we were unsuccessful so we removed the placeholder code across the site.
 - This had a minimum effect on the site style
 - In future development I would like to reintroduce placeholders with a color that reflects the style of the site. 

Active Class in Navbar
- We tried to introduce the active class to help user navigate our page 
- As you can see if you click on Breakfast, Lunch, Dinner and Snacks, log in or register the background color changes to a light blue letting the user know where they are on the website
- This was not as intuitive to code as in bootstrap.
- A combination of if and else from jinja, a variable in our python code and then some custom css to render the active class.


Base template code
- Homepage was base.html whiched to create a home page then removed base.html code
- was confused about base template. Thought it has to be the homepage

Heading Bugs in Navbar
- On the base.html page on a medium size screen you will see Temple Lean Recipes in the top left of the screen. During development I noticed on a small screen that 
this text would wrap around the other navigation list items Breakfast, Lunch, Dinner and Snacks. The words 'Temple Lean' part would sit on top of the list items and Recipes would sit below the 
the list items. I input the class of hide-on-small-only class to avoid heading Temple Lean Recipes rendering above and below the recipe navigation list items. In future development I would like to contain the words Temple Lean Recipes adjust them to the mobie device rather than remove them for small devices and bring them back on larger ones.   

JS Tabs
- converted to materialize collapsible due to JS tabs rendering same information on each loop and because it cut down the amount of code we need.


Pictures 
-height in form that led to height styling versus height in recipes that need to be added to make pictures look uniform
-could find answer for this one

Delete profile (Not logging out)
-During the development of the delete functionality a bug was recognised whereby a profile could be deleted but the user was not logged out
-The user could then click the profile button and then get a jinja error message
-to eradicate this bug we input the pop method into the delete function and redirected the usier back to register page
-this solved the bug and kept the user away from unwanted error screens  


Breakfast page

-JS Tabs overflow on right handside light blue
-Tried div tab overflow hidden in custom css didn't work
-Tried container in French Toast
-solved with css display property

Profile page
-Email for profile directory @ symbol caused a root error

Gitpod 
-Code beautifer stopped working

Container class in materialise (Be careful !!!)
-If included in base html and code extended to other html then if class container present appears to wrap content twice and shrink size noticeably. Removed container from register html to solve this. 

Future Development
- Recipe Videos
- E-Commerce subscription Business Model 
- Comments so users can interact with other users
- reset your password function


### Deployment

Basic information 

- Deployment project on Github
- This project is hosted in github repository. It was developed using Gitpod. Link to the repository https://github.com/Andrew-code2020/MS2
- Open link to project website https://andrew-code2020.github.io/MS2/

Creating the repository

- cloned the repository from milestone project 2
- To make the project in my github repository I went to the code institute recommended repository via this link https://github.com/Code-Institute-Org/gitpod-full-template
- I then clicked on use this template and created a new repository in my github account
- The screenshots of this process are available by following the directories below
    - assets/readmedocs/creatingrepo/step1copyrepotemplate.png
    - assets/readmedocs/creatingrepo/step2creatingreponame.png

Deploying the project to Github

- To deploy the project I went into the repository on this link https://github.com/Andrew-code2020/MS2
- Clicked on the settings button
- Scrolled down to the Github pages section
- clicked the dropdown menu marked none then selected master
- clicked save
- The following link to the live site then appears in the Github Pages section https://andrew-code2020.github.io/MS2/
- The screenshots of this process are available by following the directories below
    - assets/readmedocs/deploytheproject/step1deployment.png
    - assets/readmedocs/deploytheproject/step2deploymentselectnone.png
    - assets/readmedocs/deploytheproject/step3deploymentselectsave.png
    - assets/readmedocs/deploytheproject/step4deployedsite.png

Deploying the project to Heroku

- creating app in Heroku
- automatic deployment enabled
- readmedocs/deploytheproject/deployonheroku .jpg


### Credits

- I consulted the folowing websites to learn about Recipe Websites and to help construct meaningful content for this web page
   - Recipe Websites
     - http://www.eatingwell.com/
     - https://www.safefood.net/recipes
     - https://thehappypear.ie/recipes/#gs.Wsw8FZU
     - https://littlegreenspoon.ie/
     - https://minimalistbaker.com/  

- I consulted the following websites for inspiration and to learn how to implement certain features into my project;
    - https://stackoverflow.com/
        - Features influenced
        - Background images
        - height and view port of map
    - https://www.w3schools.com/default.asp
         - Features influenced
            - Border
            - Hover
            - overflow
            - card flip
- I used Materialize through out the project to deploy a mobile first design principle.
  - Website https://getbootstrap.com/
  - Features influenced
    - Header
    - Footer
    - Section
    - Navbar
    - Alert Bar
    - Form
    - Dropdown menu
    - Buttons

- Google Fonts I imported the text font Recursive from Google Fonts website https://fonts.google.com/

- I copied the hero image idea in a similar way to the Jumbtron idea from our code along whiskey drop project with the code institute. I used Boostrap to copy the code and then modified it to fit the style of this project. Reference to Github repository from code along project https://andrew-code2020.github.io/whiskeydrop/

- I copied the icons from Font awesome https://fontawesome.com/ and used the CDN to implement them in the project. I then wrote custom code to style the icons and make them more responsive. The icon next to the code institute is not the true code institute icon it is a freely available icon in font awesome. I put that icon because I felt it accurately described the code institute in an icon.

- I copied the card flip code from W3schools.com https://www.w3schools.com/howto/howto_css_flip_card.asp. I then customised it's functionality in my project.

- I copied the toggle, show and hide, mouseenter, mouseleave code from jQuery https://jquery.com/. I reviewed the lessons on jQuery in the Interactive Front Development Module to help me implement the features in this project. 

- I copied the footer design from https://dermomurphy.github.io/Dublin-360-CI/index.html and then customised it to fit my project.

- I frequently referred back to the following code institute modules to research how to construct certain features

  - HTML Fundamentals
  - CSS Fundamentals
  - User Centric Front End Development
  - JavaScript Fundamentals
  - Interactive Front End Development
  - Data Centric Development Milestone Project 

- I copied the knowledge of how to implement Materialize CDN and Font awesome CDN links from my previous milestone project. Link here https://andrew-code2020.github.io/CI-MS-1-Lean-Temple/

- I copied the idea of the class custom navbar from  https://www.geeksforgeeks.org/. This did not make the final project cut but never the less helped me shape my understanding of the navbar from bootstrap. 

##### Content

- The content was constructed by the student with inspiration from their experience as an Irish citizen for the past 31 years. 
- The destinations and the markers they hold on the map are real. The price to stay there is completely made up as are the activities.
-  is designed to be fictional and the business does not exist. 

##### Media

- The photos used in this site were obtained from pexels.com
  - These photos are placed in the website on the following pages;
- The photos used in this site were obtained from https://unsplash.com/
    These photos are placed in the website on the following pages;
    -index page
    -Registeration page
    -Lunch page


##### Acknowledgements

- I received inspiration for this project from the Code Institute Tutorial videos and my mentor Mr. Adegbenga Adeye.
- I would also like thank the following members of the Tutor Assistance Team Tim Nelson, Anna, Xavier, Igor, Miklos, Cormac, Kevin, Johann and Haley (apologies that I could not find all your surnames). I spent many hours trying to work through problems I encountered with them.