# Implementation Notes

Brief explanations on work done, and choices and assumptions made.

These are just notes for extra info; this stuff wouldn't typically exist in the repo, but could exist on a wiki with other formal project docs.

## Project

### Repo Management

The project could've, and should eventually, be split up into seperate repos, one for each service, and one for the infustructure as code (IaC). This project is simple, and a lot of the web and container code between the app and api happens to be identical, so maybe it just isn't the right time to do so. Of note, one could also use git submodules to still keep the project under one parent directory.

### Project-level Build Tooling

I wanted to try out using plain bash functions to automate build tasks rather than having to bend a Makefile to get it to fit the needs of the project. I've been working on a taskrunner lib that I wanted to try out; it just runs bash functions. Luckly, there isn't any service-level building required, as everything's currently managed and covered in the compose stack, and so I just have a single root-level Taskfile; otherwise, as it is now, I haven't tested nor thought about the feasability of using multiple dependant Taskfiles to expose and chain running a project-level tasks from the root Taskfile. I had considered using gulp, which can chain gulp files like that, if that were to be an issue.

I've could've also tried porting the Taskfile to python since most of the project happens to be using that language anyways; although, the bash Taskfile shouldn't get much more complicated than it already is, and so it'll possibly be sufficient for the project's needs for each service long-term.

## CI/CD

I found [this list of CI tools](https://github.com/ligurio/awesome-ci) and narrowed down to open source ones. I've used Jenkins in the past at a previous job, and I wanted to try a different one to compare it against. I was going to deploy an loadbalanced autoscale GitLab runner cluster to run jobs on, but I decided it might be easier in the short-term to try and learn how GitHub actions worked. I've actually used GitLab runners before, so it was nice getting to try a new tool to compare both Jenkins and GitLab against.

I originally wrote my pipelines as GitLab Workflows, but after I decided to switch to GitHub Actions, instead of porting the workflow from scratch without any knowledge of GitHub Actions, where I would have to potentially sift through docs trying to satisfy functionality with equivalent mechanisms for whole use cases implemented in the Gitab Workflows, I decided to test ChatGPT's capabilities, or if it could at least point me in the right direction. Lo and behold, it was able to convert the Workflow to an Action upfront. Very cool! It definetly made learning how to use Actions faster and easier. After studying the generated file, I used the docs to implement more feature requirements on top of it.

## Testing

### E2E

I've used Selenium in the past, and, as with the CI tool, I wanted to try something new to compare it against. I decided to give Microsoft's [Playwright](https://playwright.dev/) a try since it seems to support the three major browser engines I'm most interested in, which are the engine runtimes I have picked to target and supprt for this application: Firefox's, Chrome's (and Edge's), and Safari's. It also has many different language bindings, including Python.

## Services

### App

#### Frontend

I decided to keep this part of the project simple due to time constraints; although, at first, I wanted to try to use react and a few simple components, just to try out [Material UI](https://github.com/mui/material-ui) again. If I remember correctly, I haven't used Material UI since working with React Native around 2016-2018. I stumbled upon the library again while researching for this project, and wanted to try it out with just plain React.

### API

#### Models

The models should probably eventually inherit a base model class, which contains the work for establishing the late class binding, loads the common imports(if possible?), and defines the common serialization methods.

### Database

#### Database Schema

##### User

I had considered making the email the primary key in the User table, but we'd have to cascade a user changing their email to all other tables that reference it. Having the id as the primary key instead, allows the email to be more flexible with less reprecussions or work required.

##### Users_Movies

###### `ondelete='CASCADE'`

It could be argued as preemptive to outright delete, in this case, all, of a user's data after they close their account, but for the purposes of this demo, that's what would occur; a user's movie data is deleted once their user is removed from the system database.
