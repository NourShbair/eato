# [eato](https://eato-15691513b61b.herokuapp.com)

Developer: Nour Shbair ([NourShbair](https://www.github.com/NourShbair))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/NourShbair/eato)](https://www.github.com/NourShbair/eato/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/NourShbair/eato)](https://www.github.com/NourShbair/eato/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/NourShbair/eato)](https://www.github.com/NourShbair/eato)

Whether you’re a casual cook or a passionate foodie, Eato helps you **discover, create, and organize recipes** that suit your taste, dietary needs, and cultural preferences. With smart filtering by ingredients, meal type, and allergies, Eato ensures every user can cook with confidence — and without compromise.

![screenshot](documentation/mockup.png)

source: [eato amiresponsive](https://ui.dev/amiresponsive?url=https://eato-15691513b61b.herokuapp.com)

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide users with an intuitive and flexible platform to create, edit, and manage their own recipes.
- Help users discover new meal ideas that align with their dietary needs, cuisine preferences, and ingredient availability.

**Primary User Needs**
- Home cooks and food enthusiasts need an easy way to document their personal recipes, complete with ingredients, instructions, and images.
- Users need the ability to filter, organize, and retrieve recipes based on cuisine type, meal category (e.g., breakfast, dinner), and allergy information.
- Users want to quickly add or update recipes with dynamic ingredient entry and rich instructions.

**Business Goals**
- Deliver a seamless user experience that encourages ongoing use and recipe contribution.
- Build a trusted, community-driven hub for personalized cooking content.
- Provide a scalable and feature-rich platform that could evolve into a social, collaborative, or commercial cooking app in the future.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Recipe management (create, update, delete, and view).
- Ingredient entry with dynamic fields for name, quantity, and unit.
- Cuisine, meal type, and allergy tag assignment for each recipe.
- User account features (register, log in, log out, and manage personal recipes).
- Upload and preview recipe images.
- Step-by-step cooking instructions with rich text input.
- 404 error page for invalid or broken URLs.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, My Recipes, Add Recipe, Login/Register, and Logout.
- **Hierarchy**:
- Recipe cards displayed prominently on the homepage for easy browsing.
- Clear call-to-action buttons for adding new recipes, editing existing ones, and managing user accounts.
- Ingredient and allergy filters placed for quick recipe discovery.

**User Flow**
1. Guest users browse publicly available recipes → view titles, images, and basic details.
2. Guest users register for an account → log in to create and manage their own recipes.
3. Registered users add a new recipe → input title, description, ingredients, cuisine, and instructions.
4. Users upload an image → preview it before submitting the recipe.
5. ßUsers edit or delete existing recipes → manage their personal recipe collection.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

I used [coolors.co](https://coolors.co/080708-3772ff-df2935-fdca40-e6e8e6) to generate my color palette.

- `#000000` primary text.
- `#b90049` primary highlights.
- `#27ae60` button highlights.
- `#ffc107` secondary button highlights.

![screenshot](documentation/coolors.png)

### Typography

- [Merriweather](https://fonts.google.com/?query=Merriweather) was used for the primary headers and titles.
- [Quicksand](https://fonts.google.com/?query=Quicksand) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Home | ![screenshot](documentation/wireframes/mobile-home.png) | ![screenshot](documentation/wireframes/tablet-home.png) | ![screenshot](documentation/wireframes/desktop-home.png) |
| Add Blog | ![screenshot](documentation/wireframes/mobile-add-blog.png) | ![screenshot](documentation/wireframes/tablet-add-blog.png) | ![screenshot](documentation/wireframes/desktop-add-blog.png) |
| Edit Blog | ![screenshot](documentation/wireframes/mobile-edit-blog.png) | ![screenshot](documentation/wireframes/tablet-edit-blog.png) | ![screenshot](documentation/wireframes/desktop-edit-blog.png) |
| Blog Post | ![screenshot](documentation/wireframes/mobile-blog-post.png) | ![screenshot](documentation/wireframes/tablet-blog-post.png) | ![screenshot](documentation/wireframes/desktop-blog-post.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a Admin | I would like to manage all users, recipes, and tags | so that I can maintain the integrity of the system. |
| As a developer | I would like to deploy the app on Heroku | so that users can access it online. |
| As a user | I would like to browse recipes | so that I will be able to see all created recipes. |
| As a registered user | I would like to add a recipe | so that I can share my culinary creations. |
| As a user | I would like to see allergy tags associated with recipes | so that I can ensure the recipe is safe for me. |
| As a user | I would like to see recipes tags with meal types (e.g., breakfast, lunch, dinner) | so that others can find them easily |
| As a new user | I would like to create an account | so that I can save and manage my recipes. |
| As a registered user | I would like to log in and out | so that I can access my personal recipe collection. |
| As a user | I would like to filter recipes by category | so that I can find recipes that match my preferences. |
| As a user | I would like to see categorized recipes and personal statistics on the home page | so that I can explore content easily and feel engaged with my activity. |
| As a user | I would like to search for recipes by keyword | so that I can quickly find a specific dish. |
| As a user | I would like to navigate large lists efficiently | so that I can find content easily. |
| As a user | I would like to see a fully styled and user-friendly interface | so that I can easily navigate and interact with the app. |
| As a user | I would like access the website from any device | so that browse and save recipes easily. |
| As a registered user | I would like to like recipes | so that users can easily access number of likes on each recipes. |
| As a registered user | I would like save recipes to my favorites | so that I easily find them later. |
| As a user | I would like to switch to dark mode | so that I can use the app comfortably at night. |
| As a user | I would like to select ingredients from a pre-approved list | so that I ensure data consistency. |
| As a registered user | I would like to delete a recipe | so that I can remove unwanted recipes. |
| As a registered user | I would like to update my recipes | so that I can make changes if needed. |


## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Users can register securely to create and manage their personal recipes. | ![screenshot](documentation/features/register.png) |
| Login | Registered users can log in to access their dashboard and recipe content. | ![screenshot](documentation/features/login.png) |
| Logout | Users can safely log out of their session. | ![screenshot](documentation/features/logout.png) |
| Add Recipe | Authenticated users can add a new recipe with title, description, cuisine, image, meal type, and allergy tags. | ![screenshot](documentation/features/.png) |
| Edit Recipe | Users can update their existing recipes, including ingredients and images. | ![screenshot](documentation/features/.png) |
| Delete Recipe | Users can delete any of their own recipes. | ![screenshot](documentation/features/.png) |
| Pagination | Recipes list are displayed in pages, with six recipes per page. This provides better navigation for users through the recipes list. | ![screenshot](documentation/features/pagination.png) |
| Add Ingredients | Ingredients can be added dynamically with fields for name, quantity, and unit. | ![screenshot](documentation/features/.png) |
| Instructions Input | Recipes support rich, step-by-step instructions. | ![screenshot](documentation/features/.png) |
| Cuisine & Meal Type Filters | Recipes can be tagged with cuisines and meal types for better categorization. | ![screenshot](documentation/features/.png) |
| Allergy Tags | Recipes can be tagged with common allergens to help users avoid specific ingredients. | ![screenshot](documentation/features/-st.png) |
| Save Recipe | Logged-in users can bookmark recipes to their profile for future use. | ![screenshot](documentation/features/.png) |
| Like Recipe | Users can like recipes to show appreciation and see popularity. | ![screenshot](documentation/features/.png) |
| User Profiles | Each user has a profile displaying their saved, liked and submitted recipes. | ![screenshot](documentation/features/.png) |
| Image Upload & Preview | Users can upload an image and preview it before submitting a recipe. | ![screenshot](documentation/features/update-post.png) |
| Responsive Design  | The site is fully responsive and optimized for mobile, tablet, and desktop use. | ![screenshot](documentation/features/.png) |
| 404 Page | A custom 404 error page is displayed when a user visits a non-existent route. | ![screenshot](documentation/features/.png) |
| 500 Page | A custom 500 error page is displayed when a user visits a crash-exist route. | ![screenshot](documentation/features/.png) |

### Future Features

- **Public/Private Recipes:** Add privacy settings to let users mark recipes as private or public.
- **Recipe Sharing:** Enable users to generate shareable recipe links.
- **Ratings & Reviews:** Allow users to rate and leave feedback on recipes.
- **Step Media Uploads:** Let users attach images or videos to each instruction step.
- **Print View:** Provide printer-friendly formatting for recipes.
- **Social Sharing:** Share recipes directly on platforms like Instagram, Facebook, or Pinterest.
- **Tag-Based Filtering:** Combine tags like “vegan” + “breakfast” for precise filtering.
- **Multilingual Support:** Support creating and browsing recipes in multiple languages.
- **Ingredient Substitutions:** Suggest alternatives based on allergies or availability.
- **Voice-Guided Cooking:** Read recipe steps aloud for hands-free cooking.
- **Dark Mode:** Offer a toggleable dark theme for better accessibility and user comfort.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Jest-grey?logo=jest&logoColor=c21325)](https://jestjs.io) | Automated JavaScript testing. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/Figma-grey?logo=figma&logoColor=F24E1E)](https://www.figma.com) | Creating wireframes. |
| [![badge](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) | Icons. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |
| [![badge](https://img.shields.io/badge/StackOverflow-grey?logo=stackoverflow&logoColor=F58025)](https://stackoverflow.com) | Troubleshooting and Debugging |


## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](documentation/erd.png)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    User ||--o{ Recipe : creates
    User ||--o{ SavedRecipe : saves
    User ||--o{ RecipeLike : likes
    Recipe ||--o{ Ingredient : contains
    Recipe ||--o{ SavedRecipe : is_saved_by
    Recipe ||--o{ RecipeLike : is_liked_by
    Recipe ||--o{ RecipeAllergyTag : has_allergy_tag
    Recipe ||--o{ RecipeMealType : has_meal_type
    Recipe ||--o{ RecipeCuisine : has_cuisine
    AllergyTag ||--o{ RecipeAllergyTag : maps_to
    MealType ||--o{ RecipeMealType : maps_to
    Cuisine ||--o{ RecipeCuisine : maps_to

    User {
        string username
        string email
        string password
    }

    Recipe {
        string title
        text description
        image image
        text instructions
        datetime created_at
        datetime updated_at
    }

    Ingredient {
        string name
        float quantity
        string unit
    }

    SavedRecipe {
        datetime saved_at
    }

    RecipeLike {
        datetime liked_at
    }

    AllergyTag {
        string name
    }

    MealType {
        string name
    }

    Cuisine {
        string name
    }

    RecipeAllergyTag {
        int recipe_id
        int allergy_tag_id
    }

    RecipeMealType {
        int recipe_id
        int meal_type_id
    }

    RecipeCuisine {
        int recipe_id
        int cuisine_id
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqNVMGOmzAU_BXkczYCkpCE22p7WWl76W4vVST0il-IVbCpbdqlbP69BhMCAaIlUsLzm5k3mHEqEguKJCQovzBIJGQH7pjru0LpfHw8PIjK-YYxy9EJnVgiaFRjxCv8QdrBlKnUnMwL-1VjUvPTYlpei3rmiUTKkOt6oOAaGJ8EDmcyFdVjafSznAIPZhtsPf4-9jFNUSblGySGcQIVgV2INCTzrK8I6VvZOKo5mSkjbep5xlPBFOMXQmwrC-9ZmLeWQa4iLSyjGz9naoC-jJ7x02F7r7Ky9_WltGQ8cQqzzCHDUQMzYOloNQel_gpJbeN8EW93ZiyvmU572hrftUNRxZLlmgl-7bAMErTfN3CTHy2LuIara4uaJGuWYRtqGoGeaBY5HTQ7w72Yjk0P9-OYCtDO7wK4eZhyvIGc3Yr3o11NuLJJH3nqhXyKZTM_YvXSdO9JOnyXpk-hL3H6FHgU7x6LmZ2WTT9idLjcO5ld70ZzyvQdxe7czulNPNYdufZUX8XIgiSSURKaYOKCZCjNYTElafQORJ_QbA4JzS3FIxSpPpADr2k58B9CZBemFEVyIuERUmUqm9b2f7xblcgpyidRcE1C3280SFiRdxJ6wX65dv3V2nO3wW7je9sFKUkYbJa7YBV4rr_Z-CvX984L8q-Z6i63-83afIK9F7j71W61IFBo8Vry2Ho6_wefHQQL)


## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/NourShbair/eato/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/project-milestones.png)
![screenshot](documentation/project-board.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/NourShbair/eato/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/NourShbair/eato)](https://www.github.com/NourShbair/eato/issues) | ![screenshot](documentation/project-open-issues.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/NourShbair/eato)](https://www.github.com/NourShbair/eato/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/project-closed-issues.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://eato-15691513b61b.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), then finally, click **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables to match your private `env.py` file.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | in env.py |
| `DATABASE_URL` | in env.py |
| `DISABLE_COLLECTSTATIC` | 0 |
| `SECRET_KEY` | eatosecretkey |

Heroku needs some additional files in order to deploy properly.

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

You can install this project's **[requirements.txt](requirements.txt)** (*where applicable*) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **[Procfile](Procfile)** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace `app_name` with the name of your primary Django app name; the folder where `settings.py` is located*

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either (*recommended*):

- Select **Automatic Deployment** from the Heroku app.

Or:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a eato`
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The project should now be connected and deployed to Heroku!

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django; simply paste it into your `env.py` file and Heroku Config Vars as `DATABASE_URL`.


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the [requirements.txt](requirements.txt) file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level, and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ.setdefault("SECRET_KEY", "any-random-secret-key")
os.environ.setdefault("DATABASE_URL", "user-inserts-own-postgres-database-url")
os.environ.setdefault("CLOUDINARY_URL", "user-inserts-own-cloudinary-url")  # only if using Cloudinary

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` (*Windows/Linux*) or `⌘+C` (*Mac*)
- Make any necessary migrations: `python3 manage.py makemigrations --dry-run` then `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate --plan` then `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Load fixtures (*if applicable*): `python3 manage.py loaddata file-name.json` (*repeat for each file*)
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/NourShbair/eato).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/NourShbair/eato.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/NourShbair/eato)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/NourShbair/eato).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Markdown Builder](https://markdown.2bn.dev) | Help generating Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [I Think Therefore I Blog](https://codeinstitute.net) | Code Institute walkthrough project inspiration |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [Cloudinary API](https://cloudinary.com) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Emojipedia](https://emojipedia.org) | Emoji used throughout the site |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [Dribbble](https://dribbble.com/shots/3809698-Pumpkin-Spice-Up-Your-Life) | Error page image
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements
- I would like to thank my husband [Ahmad ElShareif](https://www.linkedin.com/in/ahmah2009/), for always believing in me, and encouraging me to make this 'transition' into web development.
- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and impostor syndrome.