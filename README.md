# Movie Manager

A movie management webapp—Search and view details on movies, and save your favorites!

Currently, the webapp is [temporarily hosted here]().

## Development

### Requirements

#### OS Level Requirements

All development has been done on a Linux machine using a relatively modern version of bash. Bash is required.

If working on Windows, you need to be using [Git for Windows's GitBash](https://git-scm.com/downloads/win). Cmd Prompt and PowerShell are not directly supported; Windows is a second-class support platform for this project.

#### Project Level Requirements

- [Git](https://git-scm.com/downloads/) for version control
- [Podman](https://podman.io/docs/installation) for local development using containers
  - Currently, development on the bare host is not yet supported
- [OpenTofu](https://opentofu.org/docs/intro/install/) for managing and deploying server infustructure

##### Optional Requirements

- [asdf](https://asdf-vm.com/guide/getting-started.html#getting-started) Makes it easy to manage varying versions of various OS Level binaries. You can use it to install the specific Podman, OpenTofu, DirEnv, Python and PipEnv versions that maybe required for this project alongside other versions of those tools for other projects.
- [DirEnv](https://direnv.net/docs/installation.html) is supported for optional, convenient, pre-defined directory-level bash functions and aliases, to further simplify project level tasks and processes.
- [Podman Desktop](https://podman-desktop.io/downloads) for container management from a GUI if preferred over using a CLI
- [Python](https://www.python.org/downloads/) >=3.8 on the host machine, for potential IDE integration
  - [PipEnv](https://pipenv.pypa.io/en/latest/installation.html) for if working with dependencies on the host
- [Visual Studio Code](https://code.visualstudio.com/Download) with code formatting and debugging pre-setup, so long as [the recommended extensions](.vscode/extensions.json) are installed. See: `.vscode/extensions.json`

### Building the Project

First, you'll need to authenticate to the project's private container registry:  
`podman login registry.digitalocean.com`

#### Building and Running Locally

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

You may also build a specific container instead of all containers in the compose stack:  

```bash
CONTAINER='app' # or: 'api', or: 'database', etc

./Taskfile build "$CONTAINER"
```

Note: You may also run the appropriate GitHub Action to trigger a build for one of the services. Each service has four different image variants corresponding to the environment the container is intended to run on: `testing`, `development`, `staging` and `production`.

Next, start the compose stack, which spins up the container services on your host:  

```bash
./Taskfile restart
```
*Note: The `restart` task attempts to compose-`stop` and `down` the existing stack, then `up`s the compose stack

The WebApp should now be accessible on [`http://localhost:80`](http://localhost:80), or [`127.0.0.1:80`](127.0.0.1:80)

##### Local Troubleshooting

To troubleshoot a container that's exiting prematurely on startup, you may override a its command and entrypoint in the `compose.yml` stack:  

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

When finished, you can use the `down` task to compose-`down` the stack, which will stop and remove the containers in the stack:  

```bash
./Taskfile down
```

##### Running Tests Locally

###### Running Functional Tests Locally

pytest: *Tests yet to be written*

###### Running Unit Tests Locally

pytest: *Tests yet to be written*

###### Running Integration Tests Locally

*Yet to be implemented*

The mechanism for running app scenarios across services hasn't been fleshed out yet. The testing image-variants need to be worked on first and then the library written or a library used to setup the testing scenarios and mock data.

###### Running Feature Tests Locally

Playwright: *Yet to be implemented*

#### Running Tests on GitHub Actions

##### Running Functional Tests on GitHub Actions

Functional tests run as a prerequisite job before a container service is able to be pushed. This job becomes available for a given commit artifact upon pushing to the repo.

##### Running Unit Tests on GitHub Actions

Unit tests also run as a prerequisite job before a container service is able to be pushed, after the functional tests are successful.

##### Running Integration Tests on GitHub Actions

*Yet to be implemented in the pipeline and IaC*

Integration tests will run on the testing environment after a workflow targeting that environmet successfully builds and pushes all service images, and then deploys those updated images to that environment via IaC. Additional IaC will be created to deploy an additional temporary service container to the testing cluster to run integration tests off of.

##### Running Feature Tests on GitHub Actions

*Yet to be implemented*

Just like integration tests, feature tests will run on the testing environment as well, after integration tests on there are successful. This could potentially occur on the same type of temporary service container that the integration tests would be ran on.

## Deployment

### Deployment using GitHub Actions

The more appropriate and safe way to kick-off a deploy is to trigger the GitHub Workflows for `build`ing, `test`ing, and `push`ing the service containers to the container registry, and then `deploy`ing the Infustructure as Code (IaC) for the target environment.

### Deployment using OpenTofu Locally

*Caution: Deploying to an environment using OpenTofu locally may bypass the typical prerequisite pipeline checks and safeguards, such as circumventing the need for tests to pass before being able to push a built image, or deploying before pushing a new image tag to the container registry, for example.*

As a fallback for taking care of plumbing not directly addressable by the GitHub Actions, you can trigger and manage a deploy for a given environment by using OpenTofu locally on the CLI.

Use `tofu plan` to stage and preview infustructure changes for a target environment, then tofu apply to commit and publish those changes for that environment:  

```bash
TF_ENV_FILE=development.tfvars

tofu plan -var-file="$TF_ENV_FILE"

OpenTofu used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
...
```

Then, if everything is as expected, apply the changes to that pre-planned environment:  

```bash
# The var-file passed into tofu plan was set to 'development.tfvars', so these changes will be applied to the development environment
tofu apply
```
