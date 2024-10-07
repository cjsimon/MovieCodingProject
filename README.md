# Movie Manager

A movie management webapp—Search and view details on movies, and save your favorites!

## Development

### Requirements

#### OS Level Requirements

All development has been done on a Linux machine using a relatively modern version of bash. Bash is required.

If working on Windows, you need to be using [Git for Windows's GitBash](https://git-scm.com/downloads/win). Cmd Prompt and PowerShell are not directly supported; Windows is a second-class support platform for this project.

#### Project Level Requirements

- [Git](https://git-scm.com/downloads/) for version control
- [OpenTofu](https://opentofu.org/docs/intro/install/) for managing and deploying server infustructure locally
- [Podman](https://podman.io/docs/installation) for local development using containers
  - Currently, development on the bare host is not yet supported
- [Python](https://www.python.org/downloads/) >=3.8 on the host machine, for running tests and PipEnv on the host
  - [PipEnv](https://pipenv.pypa.io/en/latest/installation.html) for optionally relocking updated dependencies on the host instead of the container, using `pipenv lock`.

##### Optional Requirements

- [asdf](https://asdf-vm.com/guide/getting-started.html#getting-started) Makes it easy to manage varying versions of various OS Level binaries. You can use it to install the specific Podman, OpenTofu, DirEnv, Python and PipEnv versions that maybe required for this project alongside other versions of those tools for other projects.
- [DirEnv](https://direnv.net/docs/installation.html) is supported for optional, convenient, pre-defined directory-level bash functions and aliases, to further simplify project level tasks and processes. (*Note: You may replace all `./Taskfile` calls with the `task` or `run` project-level aliases if DirEnv is activated in the projet directory*)
- [Podman Desktop](https://podman-desktop.io/downloads) for container management from a GUI if preferred over using a CLI
- [Visual Studio Code](https://code.visualstudio.com/Download) with code formatting and debugging pre-setup, so long as [the recommended extensions](.vscode/extensions.json) are installed. See: `.vscode/extensions.json`. ***Note:** Recommended extensions yet to be added*

### Building the Project

***WIP:** Private container registry yet to be deployed. Resort to building and running locally for now*

First, you
'll need to authenticate to the project's private container registry:  
`podman login registry.digitalocean.com`

#### Building and Running Locally

From the root project directory, make a working copy of the template compose stack to use for local development:

```bash
cp compose.template.yml compose.yml
```

***NOTE:** Only the template compose stack is checked into git*

In your working compose stack, set the `APPLICATION_OMDBAPI_KEY` for the api service to use, under the envvar. :  

```yml
serivces:
  api:
    env_file: ./env/api.env
      environment: # Overrides env_file defaults
        
        # NOTE: If this is your first run of the service stack,
        #       you may also want to temporarily set the below
        #       APPLICATION_INIT_DATABASE envvar flag to 'true'
        #       to generate the sql tables from the app models
        APPLICATION_INIT_DATABASE: true
        
        # Set this envvar with your OMDb API Key
        APPLICATION_OMDBAPI_KEY: <YOUR_KEY_HERE>
```

For local development, you have the option of building the service containers on your host, or using the prebuilt development image variants. By default, the prebuilt development image variants are fetched from the project's private container registry.

If you would like to build a container locally using the Containerfile instead of pulling down a prebuilt image, you will need to edit the `compose.yml` stack located in the root project directory.

Comment-out the `image` block, and uncomment the `build` block of the service container you want to build:  

```yml
app:
    container_name: app
    #
    #image: 
    # or
    build:
        context: ./app/
        dockerfile: Containerfile
        args:
            image_variant: development
    #
```

Next, to build all service containers in the stack, in the root project directory, run:  

```bash
./Taskfile build
```

***Note**: Use `rebuild` instead to build an image from scrach without layer cache*

You may also build a specific container instead of all containers in the compose stack:  

```bash
CONTAINER='app' # or: 'api', or: 'database', etc

./Taskfile build "$CONTAINER"
```

***Note:** You may also run the appropriate GitHub Action to trigger a build for one of the services. Each service has four different image variants corresponding to the environment the container is intended to run on: `testing`, `development`, `staging` and `production`.*

Next, start the compose stack, which spins up the container services on your host:  

```bash
./Taskfile restart
```
***Note:** The `restart` task attempts to compose-`stop` and `down` the existing stack, then `up`s the compose stack.*

The WebApp should now be accessible on [`http://localhost:80`](http://localhost:80), or [`127.0.0.1:80`](127.0.0.1:80), and the WebApi on port `4321`. See the [Internal API docs](./api/README.md) in the api service README for available endpoints

##### Local Troubleshooting

###### Troubleshooting Container Prematurley Crashing

To troubleshoot a container that's exiting prematurely on, or close after startup, you may override a its command and entrypoint in the `compose.yml` stack:  

```yml
database:
    container_name: database
    image: mariadb:lts
    restart: "no"
    #
    # Uncomment to override the service container's
    # default command and entrypoint for debugging
    command: ""
    entrypoint: /bin/bash # podman exec -i
    tty: true             # podman exec -t
    #
    environment:
        ...
    ...
```

You can then attach into that conainer to troubleshoot it:  

```bash
CONTAINER='database' # or: 'api', or: 'app', etc

./Taskfile attach "$CONTAINER"
```

When finished, you can use the `down` task to compose-`down` the stack, which will stop and remove the containers in the stack. Then revert the changes to the entrypoint in the `compose.yml` stack used for troubleshooting:  

```bash
./Taskfile down
```

In the `compose.yml` stack, recomment the uncommented lines:  
```yml
database:
    container_name: database
    image: mariadb:lts
    restart: "no"
    #
    # Uncomment to override the service container's
    # default command and entrypoint for debugging
    #command: ""
    #entrypoint: /bin/bash # podman exec -i
    #tty: true             # podman exec -t
    #
    environment:
        ...
    ...
```

###### Working with Project-Level Dependencies

Note that for project-level dependencies, only the lockfile is `COPY`ed into the container. For a given python service, you may run `pipenv lock` in the service-level `src/` directory to relock dependencies on the host, or preferably on the container if the `src/` code is appropriately volumed-in as it is by default:

Attach into the target service container, then run `pipenv lock`:  

```bash
CONTAINER='app' # or 'api', etc

./Taskfile attach "$CONTAINER"
```
```bash
pipenv lock
exit # Exit the container terminal session
```

##### Running Tests Locally

***WIP:** This has yet to be implemented! Currently, all the test task would need to do to run tests is running something along the lines of: `python run $SERVICE_NAME/tests/*`*

To run each type of tests (unit, feature) for all services, run `test` without any parameters:  

```bash
./Taskfile test # To run tests for all services
```

To run each type of tests for a list of given services, pass those service names in as parameters:  
```bash
SERVICES='app api'

./Taskfile test "$SERVICES"
```

To run a given list of test types for a list of given services, pass in the services like before, then pass `--` and then the list of test types, so the command can distinguish the two sets of args:  
```bash
SERVICES='app api'
TEST_TYPES='feature unit'

./Taskfile test "$SERVICES" -- "$TEST_TYPES"
```

To run a given list of test types for all services, do not pass in a list of services, then pass `--` and then the list of test types:  
```bash
SERVICES='app api'
TEST_TYPES='feature unit'

./Taskfile test -- "$TEST_TYPES"
```

***TODO:** Eventually, determine and document functionality for running particular test suites/groups of tests for a given test type*

###### Running Functional Tests Locally

***WIP:** Tests yet to be written using pytest*

###### Running Unit Tests Locally

***WIP:** Tests yet to be written using pytest*

###### Running Integration Tests Locally

***WIP:** Integration test runner yet to be implemented*

***NOTE:** The mechanism for running app scenarios across services hasn't been fleshed out yet. The testing image-variants need to be implemented first, then either a library used or developed to setup running the testing scenarios with mock data.*

###### Running Feature Tests Locally

***WIP:** Yet to be implemented using Playwright python bindings*

#### Running Tests on GitHub Actions

##### Running Functional Tests on GitHub Actions

Functional tests run as a prerequisite job before a container service is able to be pushed. This job becomes available for a given commit artifact upon pushing to the repo.

##### Running Unit Tests on GitHub Actions

Unit tests also run as a prerequisite job before a container service is able to be pushed, after the functional tests are successful.

##### Running Integration Tests on GitHub Actions

***WIP:** Yet to be implemented in the pipeline and IaC*

***NOTE:** Integration tests will run on the testing environment after a workflow targeting that environmet successfully builds and pushes all service images, and then deploys those updated images to that environment via IaC. Additional IaC will be created to deploy an additional temporary service container to the testing cluster to run integration tests off of.*

##### Running Feature Tests on GitHub Actions

***WIP:** Action invoking python test runner yet to be implemented*

***NOTE:** Just like integration tests, feature tests will run on the testing environment as well, after integration tests on there are successful. This could potentially occur on the same type of temporary service container that the integration tests would be ran on.*

## Deployment

### Deployment using GitHub Actions

The more appropriate and safe way to kick-off a deploy is to trigger the GitHub Workflows for `build`ing, `test`ing, and `push`ing the service containers to the container registry, and then `deploy`ing the Infustructure as Code (IaC) for the target environment.

### Deployment using OpenTofu Locally

***CAUTION:** Deploying to an environment using OpenTofu locally may bypass the typical prerequisite pipeline checks and safeguards, such as circumventing the need for tests to pass before being able to push a built image, or deploying before pushing a new image tag to the container registry, for example.*

As a fallback for taking care of plumbing not directly addressable by the GitHub Actions, you can trigger and manage a deploy for a given environment by using OpenTofu locally on the CLI.

***TODO:** Write tasks for `plan`ing, and `apply`ing (`deploy`ing)*

Use `tofu plan` with an environment file to stage and preview infustructure changes for a corresponding target environment, then `tofu apply` to commit and publish those changes for that environment:  

```bash
TF_ENV_FILE=development.tfvars

tofu plan -var-file="$TF_ENV_FILE"
```
```
OpenTofu used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
...
```

Then, if everything is as expected, apply the changes to that pre-planned environment:  

```bash
# The var-file passed into tofu plan was set to 'development.tfvars', so these changes will be applied to the development environment
tofu apply
```
