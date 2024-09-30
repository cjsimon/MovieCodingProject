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

- [asdf](https://asdf-vm.com/guide/getting-started.html#getting-started) Makes it easy to manage varying versions of various OS Level binaries. You can use it to install the specific Podman, OpenTofu, DirEnv and Python versions that maybe required for this project alongside other versions of those tools for other projects.
- [DirEnv](https://direnv.net/docs/installation.html) is supported for optional, convenient, pre-defined directory-level bash functions and aliases, to further simplify project level tasks and processes.
- [Podman Desktop](https://podman-desktop.io/downloads) for container management from a GUI if preferred over using a CLI
- [Python](https://www.python.org/downloads/) >=3.8 on the host machine, for potential IDE integration
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

Note: You may also run the appropriate GitHub action to trigger a build for one of the services. Each service has four different image variants corresponding to the environment the container is intended to run on: `testing`, `development`, `staging` and `production`

Next, start the compose stack, which spins up the container services on your host:  

```bash
./Taskfile restart
```
*Note: The `restart` task attempts to compose-`stop` and `down` the existing stack, then `up`s the compose stack

The WebApp should now be accessible on [http://localhost:80](http://localhost:80)`, or [127.0.0.1:80](127.0.0.1:80)

### Running Tests

- Functional Tests
- Unit Tests
- Integration Tests
- Feature Tests
