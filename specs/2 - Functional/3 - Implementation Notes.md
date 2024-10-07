# Implementation Notes

Brief explanations on work done, and choices and assumptions made.

These are just notes for extra info; this stuff wouldn't typically exist in the repo, but could potentially exist on a wiki with other formal, or informal, project docs.

I'm not really married to the choices I made, nor technologies I used; they were mainly chosen circumstantially. Most of my choices prioritized experimentation and learning since I had the opportunity to make my own personal decisions for this test-case project, with its few technology stack requirements. If I were to re-creating this project using a different set of required technologies, it would yield a very similar project structure, typically prioritizing extensibility, elegance (in use and readability), and efficiency, according to requirements.

Most of my development experience happens to consist of work done for large-scale, long-term, high maintenance clients, each with varying demands and security requirements and policies; the assumptions I made for this project might reflect some of that. I am not quick to necessarily use what I am comfortable with, but that which might be better suited for a project. Even for the multi-tenant workflows I've managed in the past for example, where all most all use cases are the same, there has existed a level where cookie-cutter templates haven't been able to cover the scope of the requirements. In those scenarios, we try to stick to standard best practices and known development and architecture paradigms as best we can. For that particular experience in the past, for example, we opted to write an internal API in our existing Laravel codebase that could manage the varying custom workflows and front-ends that more and more tenants began to require, instead of quickly building template, one-off front-ends in vue—we abstracted the manual cookie-cutter templating work to save longterm time rather than short-term time with potential added tech debt longterm.

For this project, it could have been beneficial to use more popular tools and technologies that I might've been slightly more comfortable and efficient in, but I decided to prioritize experimentation and learning over the arguably more fitting requirements of better delivery speed, better extensibility, better standardization, and even better security in some areas, since I'd be spending a lot of my personal time on it. This project was large in scope, not in depth; to me, that's where true complexity seems to lie.

## Project

### Repo Management

The project could've, and should eventually, be split up into separate repos, one for each service, and one for the infrastructure as code (IaC). This project is simple, and a lot of the web and container code between the app and api happens to be identical, so maybe it just isn't the right time to do so. Of note, one could also use git submodules to still keep the project under one parent directory.

### Project-level Build Tooling

I wanted to try out using plain bash functions to automate build tasks rather than having to bend a Makefile to get it to fit the needs of the project. I've been working on a taskrunner lib that I wanted to try out; it just runs bash functions. Luckily, there isn't any service-level building required, as everything's currently managed and covered in the compose stack, and so I just have a single root-level Taskfile; otherwise, as it is now, I haven't tested nor thought about the feasibility of using multiple dependant Taskfiles to expose and chain running a project-level tasks from the root Taskfile. I had considered using gulp, which can chain gulp files like that, if that were to be an issue.

I've could've also tried porting the Taskfile to python since most of the project happens to be using that language anyways; although, the bash Taskfile shouldn't get much more complicated than it already is, and so it'll possibly be sufficient for the project's needs for each service long-term.

## CI/CD

I found [this list of CI tools](https://github.com/ligurio/awesome-ci) and narrowed down to open source ones. I've used Jenkins in the past at a previous job, and I wanted to try a different one to compare it against. I was going to deploy an load-balanced auto-scale GitLab runner cluster to run jobs on, but I decided it might be easier in the short-term to try and learn how GitHub actions worked. I've actually used GitLab runners before, so it was nice getting to try a new tool to compare both Jenkins and GitLab against.

I originally wrote my pipelines as GitLab Workflows, but after I decided to switch to GitHub Actions, instead of porting the workflow from scratch without any knowledge of GitHub Actions, where I would have to potentially sift through docs trying to satisfy functionality with equivalent mechanisms for whole use cases implemented in the GitLab Workflows, I decided to test ChatGPT's capabilities, or if it could at least point me in the right direction. Lo and behold, it was able to convert the Workflow to an Action upfront. Very cool! It definitely made learning how to use Actions faster and easier. After studying the generated file, I used the docs to implement more feature requirements on top of it. So far, I haven't enjoyed working with GitHub Actions as much as I have GitLab Workflows and Jenkins; I don't think I would even prefer using Forgejo's open source github-like alternative actions runner. GitLab Workflows are simpler to use and implement in my opinion, and their UI for pipelines is excellent in it's simplicity without any learning curve. If I had to do it over, I would stick to using GitLab workflows, or better yet, get reaquainted with Jenkins or one of the other listed Free Open Source Software (FOSS) "Awesome CI" tools, compared to the GitLab's Freemium OSS model.

## Testing

### E2E

I've used Selenium in the past, and, as with the CI tool, I wanted to try something new to compare it against. I decided to give Microsoft's [Playwright](https://playwright.dev/) a try since it seems to support the three major browser engines I'm most interested in, which are the engine run-times I have picked to target and support for this application: Firefox's, Chrome's (and Edge's), and Safari's. It also has many different language bindings for its API, including Python bindings.

## Services

According to typical hardened image standards and best practices, you shouldn't be using the root user to install, manage and run project-level dependencies, but a project-level user, like Apache for php containers, or some python user for a python runtime, etc. I didn't have time to look into this. See the "User and group id", and "Running nginx as a non-root user" sections of the docs for the official [nginx docker image](https://hub.docker.com/_/nginx/), for example.

### App Dependencies

Both python images share the same flask_app library; it should be shared across apps instead of attempting to manage keeping both in sync by hand... Just like how a private container registry needs to be used to host custom images, and even private copies of the existing public images, a private package store should be used, not just for shared dependencies, but for all project-level dependencies, so there is another control layer on what gets pulled into the apps—Understandably, those who were victim to the [npm left-pad incident](https://en.wikipedia.org/wiki/Npm_left-pad_incident) were at fault for not doing exactly this, or potentially generally not monitoring and/or vetting pulled-in dependencies well enough.

### App Service

#### Frontend

I decided to keep this part of the project simple due to time constraints; although, at first, I wanted to try to use React and make a few simple components just to try out [Material UI](https://github.com/mui/material-ui) again. I haven't used Material UI since working with React Native around 2016-2018. I had stumbled upon the library again while researching for this project, and had wanted to try it out with just plain React this time.

Before starting this project, I had recently been playing with [EJS templates](https://ejs.co/) (the same ones [Express](https://expressjs.com/en/api.html#app.engine) makes use of) and a modern, custom [HTML Imports](https://www.w3.org/standards/history/html-imports.html/) shim in an attempt to conjure up a simple client-side component/templating library for fun. Since this was a simple test-case project, instead of relying on a more robust, standardized, and cookie-cutter framework, like React, I decided to rope in my alpha framework instead to see how well it'd currently fair against a real-world project. As it stands now, I'm not certain that the way the EJS templates and html imports are fetched is CSP Compliant; for that endeavor, I will be looking into how React and Angular deal with seemingly dynamic html and js content rendering. (Early on, AngularJS and 2 used to use ajax under the hood—I'm not sure if that's still the case). But, yes, under normal circumstances, React could be preferable, even for a simple project such as this one. The ES6 JS modules aren't currently working, due to some requests getting blocked (see: Troubleshooting the Development Server). I tried EJS on a test apache server and it was pretty interesting.

#### Troubleshooting the Development Server

Loading module from “http://127.0.0.1/static/libraries/JSTemplates/JSTemplates.js” was blocked because of a disallowed MIME type (“text/html”).

I tried disabling flask's CSRF mode to see if that was the culprit, but maybe it's just the development server itself. I figured this would work as expected if hosting with a reverse proxy such as NGINX, instead of hosting with the development server. The development server pointing to the reverse-proxy didn't seem to make a difference. I just switched to using a production-ready wsgi python server to try with the reverse-proxy, and I'm still seeing the same issue. Might need more investigation before I can work on the frontend.

### API Service

#### Internal API, and OMdb Endpoint Test Suite

Probably the next step before writing `fetch` requests and submitting POST forms from the frontend to invoke the api would be to create an endpoint test suite. I've used Postman Collections in the past with parameters and secrets for different environments, and had the suite run as a prerequisite test job on CI. I would've liked to try something new, and open source. [Hurl](https://hurl.dev/) seems like a great option, with [CI support](https://hurl.dev/docs/tutorial/ci-cd-integration.html#cicd-integration).

#### Models

The models should probably eventually inherit a base model class, which can contain the work for establishing the late class binding, loading the common imports(if possible? Seems like it), and defining the common serialization methods.

### Database

#### Database Schema

There seems to be a general issue with the SQLAlchemy ORM Models not correctly representing the expected schema. I might've made an implementation mistake with the library. I could've resorted to bare sql to create the table structure, with the cascades and all, but it wouldn't be as portable, and it would've been redundant since I'm already using the models anyways. It's easier to maintain migrations using an ORM.

##### User

I had considered making the email the primary key in the User table, but we'd have to cascade a user changing their email to all other tables that reference it. Having the id as the primary key instead, allows the email to be more flexible with less repercussions or work required.

##### Users_Movies

###### `ondelete='CASCADE'`

It could be argued as preemptive to outright delete, in this case, all, of a user's data after they close their account, but for the purposes of this demo, that's what would occur; a user's movie data is deleted once their user is removed from the system database.

## Deployment

It might make sense to explore including a single `volume`-in of the source code for each cluster, rather than having each container carry a `COPY`of it.
