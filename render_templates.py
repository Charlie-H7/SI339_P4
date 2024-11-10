import csv
import os
import json

# Read from the csv files (all??) in directory
male_athelete_dir = "drive_download/athletes/mens_team"
female_athelete_dir = "drive_download/athletes/womens_team"

count = 0
male_athletes_table = ""
female_athletes_table = ""

# Data required to render templates
athlete_data_male = []
athlete_data_female = []


# load data requires a directory and an athlete list that will be modified to hold dictionaries where every dictionary is the data of a student in the directory
def load_data(directory, athlete_list):
    # Read csv files for files in directory
    for filename in os.listdir(directory):

        with open(directory + "/" + filename, 'r') as fh:
            
            table = csv.reader(fh)
            
            # Want reset for every new athlete
            athlete_dict = {}
            season_list = []
            career_list = []

            #Store the id and name
            athlete_dict['name'] = next(table)
            athlete_dict['id'] = next(table)

            for row in table:

                # grab data only if a row is not empty nor a header
                if len(row) != 0 and row != ['Name', 'Overall Place', 'Grade', 'Time', 'Date', 'Meet', 'Comments', 'Photo']:


                    # Check if the row is season record row (denoted by having a value in the grade column)
                    if row[2] != '':
                        season_list.append(row)
                    else: # Append all other races to their total career
                        career_list.append(row)
            
            athlete_dict["season_record"] = season_list
            athlete_dict["career"] = career_list

            # Append completed student dictionary into athlete_list
            athlete_list.append(athlete_dict)

            # pretty_print = json.dumps(athlete_dict, indent=2)
            # print(pretty_print)
    
#athlete list is data structure returned from load_data
def template_table(athlete_list):
    template_html = ""

    for athlete_dict in athlete_list:

        # pretty_print = json.dumps(athlete_dict, indent=2)
        # print(pretty_print)
        # For every athlete we want to add in a new row within our table


        template_html += f"""
        <tr>
            <td>
                <div>
                    <!-- not all the images we require exists in the folders provided to us, but we have realized that there should exists profile pictures of athletes (there is a column in meet csv) that uses their id and .jpg extension to navigate and call them -->
                    
                    <a href="athlete_pages/{athlete_dict['id'][0]}.html"> <img src="images/AthleteImages/{athlete_dict['id'][0]}.jpg" alt="img of {athlete_dict['name'][0]}, id: {athlete_dict['id']}" width="100" height="100"> </a>
                    
                    <a href="athlete_pages/{athlete_dict['id'][0]}.html"> {athlete_dict['name'][0]} </a>
        
                    {athlete_dict['id'][0]}
                </div>
            </td>
        </tr>
        """
    
    return template_html



load_data(male_athelete_dir,athlete_data_male)
load_data(female_athelete_dir,athlete_data_female)
male_athletes_table = template_table(athlete_data_male)
female_athletes_table = template_table(athlete_data_female)
# print(athlete_data_male)
# with open('output.txt', 'w') as file:
#     file.write(str(athlete_data_male))

index_html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Deliverable</title> <!--Title TK-->
    <link rel="stylesheet" type="text/css" href="css/reset.css">
    <link rel="stylesheet" type="text/css" href="css/style.css">
    <link rel="icon" type="images/icon.png" href="images/icon.png">

</head>
<body>
    <main>
    <!--nav bar-->
    <div id="nav-bar">
        <nav>
            <ul class="nav-list">
                <li>
                    <a href="https://www.athletic.net/">
                        <img src="images/site_logo.jpeg" alt="site logo" width="175" height="26" tabindex="0"> <!-- IMG TK-->
                    </a>
                </li>
                <li><a href="https://www.google.com/" tabindex="0">login</a></li>
            </ul>
        </nav>
    </div>

    <!--Main box-->
    <div>
     <!--Main box 1-->
        <div id="box1">
            <img src="images/aa_skyline.jpg" alt="Team logo" width="175" height="175" tabindex="0">
            <h1><a href="index.html">Ann Arbor Skyline</a></h1>
            <h3> 48104, MI </h3>
        </div>

        <!--Main box 2 Comments-->
        <div id="box2">
            <h2>Comments:</h2>
            <div>
                Team Comments and Announcements goes here. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer ac risus id sem egestas mattis. Proin pellentesque diam eu orci tincidunt, sit amet congue quam tempor. Donec vulputate ligula eu eleifend viverra. Aenean congue aliquet dui et accumsan. Proin vulputate nisi et dolor convallis aliquam.
            </div>
        </div>

        <!--Main box 3-->
        <div id="athletes">
 

            <!-- Make individual tables for males and female runners-->

            <details>
                <summary><h3>Men's Team</h3></summary>
                <table>
                    <tr>
                        <th>Mens</th>
                    </tr>
                    <tbody>
                        {male_athletes_table}
                    </tbody>
                </table>
            </details>


            <details>
                <summary><h3>Women's Team</h3></summary>
                <table>
                    <tr>
                        <th>Womens</th>
                    </tr>
                    <tbody>
                        {female_athletes_table}
                    </tbody>
                </table>
            </details>

        </div>

        <!--Main box 4-->
        </main>
        <footer id="footer">
            <nav>
                <ul class="nav-list">
                    <li><a href="https://www.google.com/" tabindex="0">Credidentials</a></li> 
                    <li><a href="https://www.google.com/" tabindex="0">For Coaches</a></li> 
                    <li><a href="" tabindex="0">Charlie H</a></li>
                </ul> 
            </nav>
        </footer>
    </div>
    <script src="js/image.js"></script>
</body>
</html>
"""
# print(index_html_template)

with open("index.html", 'w') as file:
    file.write(index_html_template)

#Overall Place, Grade, Time
def season_record(athletic_dict):
    temp_html = ""
    # Loop over the season record for current athlete
    for record in athletic_dict['season_record']:
        temp_html += f"""
            <tr>
                <td>{record[1]}</td>
                <td>{record[2]}</td>
                <td>{record[3]}</td>
            </tr>
        """
    
    return temp_html

#Overall Place, Time, Date, Meet, Comments
def career_record(athletic_dict):
    temp_html = ""
    # Loop over all the races an athlete has done
    for record in athletic_dict['career']:
        temp_html += f"""
            <tr>
                <td class="place">{record[1]}</td>
                <td class="time">{record[3]}</td>
                <td class="date">{record[4]}</td>
                <td class="meet">{record[5]}</td>
                <td class="comments" class="comment-segment">{record[6]}</td>
            </tr>
        """
    return temp_html

# print(athlete_data_male[0]['name'])
# print(season_record(athlete_data_male[0]))

# print(career_record(athlete_data_male[0]))

def render_student_html(athlete_dict, template_html):
    temp_html = ""
    # Everything after title
    temp_html = f"""
    <div class="athlete-info">
        <a href="../images/AthleteImages/{athlete_dict['id'][0]}.jpg" data-lightbox="athlete" data-title="Athlete: {athlete_dict['name'][0]}">
            <img 
                src="../images/AthleteImages/{athlete_dict['id'][0]}.jpg" 
                alt="img of {athlete_dict['name'][0]}, id: {athlete_dict['id']}" 
                width="150" height="150" 
                class="athlete-photo"
                tabindex="0"
            >
        </a>
        <h2>{athlete_dict['name'][0]}</h2>
        {athlete_dict['id'][0]}

        <div class="progress-container">
            <div class="progress-bar"></div>
        </div>
        <div id="goal">Personal mile goal met</div>
    </div>

    
    <h3>Season Record</h3>
    <div class="sr-container">
        <table class="sr-table" tabindex="0">
            <thead>
                <tr>
                    <th class="table-header">Overall Place 🥇</th>
                    <th class="table-header">Grade 🎓</th>
                    <th class="table-header">Time 🕕</th>
                </tr>
            </thead>
            <tbody>
                {season_record(athlete_dict)}
            </tbody>
        </table>
    </div>

    
    <h3>Career Record</h3>
    <div class=cr-container>
        <table class="cr-table" tabindex="0">
            <thead>
                <tr>
                    <th class="table-header">Overall Place 🥇</th>
                    <th class="table-header">Time 🕕</th>
                    <th class="table-header date">Date 📅</th>
                    <th class="table-header">Meet 🏃‍♀️</th>
                    <th class="table-header comments">Comments 💬</th>
                </tr>
            </thead>
            <tbody>
                {career_record(athlete_dict)}
            </tbody>
        </table>
    </div>
        
        <footer>
            <nav>
                <ul class="nav-list">
                    <!-- Added button functionality to return to home page -->
                    <li><a id="home-button" href="/">Go Home</a></li>
                </ul> 
            </nav>
        </footer>
        <a id="fab" href="#nav-bar" class="fab" tabindex="0">↑</a>

        <script src="../js/func.js"></script>
        <script src="../dist/js/lightbox-plus-jquery.js"></script>


    </body>
</html>
    """
    template_html += temp_html
    return template_html
        
def render_html(athlete_list, student_html_template):
    # Loop over every student in athlete list
    for athlete_dict in athlete_list:
        with open(f"athlete_pages/{athlete_dict['id'][0]}.html", 'w') as file:
            file.write(render_student_html(athlete_dict, student_html_template))


student_html_template = f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="../css/reset.css">
        <link rel="stylesheet" href="../dist/css/lightbox.css">
        <link rel="stylesheet" type="text/css" href="../css/student_style.css">
        <link rel="stylesheet" type="text/css" href="../css/tablet_view.css">
        <link rel="stylesheet" type="text/css" href="../css/desktop_view.css">
        <title>Deliverable 3</title> <!--Title TK-->

        <link rel="icon" type="/images/icon.png" href="/images/icon.png">
    </head>
    <body>
        
    
        <!--nav bar-->
        <div id="nav-bar">
            <nav>
                <ul class="nav-list">
                    <li>            
                        <a href="https://www.athletic.net/" tabindex="0"><img id="site-logo" src="../images/site_logo.svg" alt="site logo" width="175" height="26"></a>
                    </li>
                    <li><a href="https://www.google.com/" tabindex="0">login</a></li>
                    <li>
                        <label for="theme-switch">Choose a theme:</label>
                            <select id="theme-switch" class="theme">
                                    <option value="" selected disabled>Select Theme</option>
                                    <option value="dark-mode">Dark Mode</option>
                                    <option value="light-mode">Light Mode</option>
                                    <option value="high-contrast">High Contrast</option>
                                </select>
                            </select>
                    </li>

                </ul>
            </nav>
        </div>

        
        <!--Main box-->
            <!--Main box 1-->
        <div class="team-info">
            <a href="../images/aa_skyline.jpg" data-lightbox="team-logo" data-title="Team Logo">
                <img src="../images/aa_skyline.jpg" class="team-logo" alt="team insert name logo" width="175" height="175" tabindex="0">
            </a>
            <h1>Ann Arbor Skyline</h1>
            <div> 48104, MI </div>
        </div>


"""

render_html(athlete_data_male, student_html_template)
render_html(athlete_data_female, student_html_template)