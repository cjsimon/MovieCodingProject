# Project Requirements

This project is a movie search application that allows users to search for movies, view details, and save favorite movies to a PostgreSQL or MySQL database. The app supports pagination of search results, allows users to manage their saved movies, and is hosted on a live URL or IP address. The code will be versioned using Git and shared with the team. Unit and integration tests should be provided where applicable. Creating User Authentication is not required.

## Functional Requirements

### Movie Search Feature

The app should display search results with basic information such as title, year, and rating

The app should implement pagination to handle large search result sets (e.g., display 10 movies per page)

The app should integrate with the OMDB API, or a similar public movie database API, to search for movies by title:
  - [OMDb Sign up](https://www.omdbapi.com/apikey.aspx) | [OMDb API Documentation](https://www.omdbapi.com/#usage)
  - API Key: **REDACTED**

### Movie Detail View

Clicking on a movie should show additional details (e.g., plot, director, actors).

An option to save the movie to the database as a favorite should be implemented.

### Save Favorite Movies

A user should be able to save a movie to the PostgreSQL/MySQL database by clicking a "Save" button on the movie detail page.

The app does not require user authentication. It may assume that there is just one user accessing the application.

The app should implement a separate page where a user can view all their saved movies, with options to delete them.

Saved movies should include information like the movie title, year, and the user's ID.

### Delete Saved Movies

Users should be able to delete saved movies from their favorites list on the saved movies page.

### Pagination of Movies

The application should paginate movie search results and provide navigation options (e.g., "Next" and "Previous" buttons).

Pagination should also be implemented on the saved movies page if the number of saved movies exceeds a set threshold.

### Hosting

The app must be deployed on a live URL or IP address for access by the team.

The deployment environment should be set up to support continuous delivery, allowing for updates to be pushed to production as new features are implemented.

### Version Control

The entire project should be versioned using Git. The final repository must be shared with the team (e.g., via GitHub, GitLab, or Bitbucket). Include proper commit messages, tags, and branching strategies, if applicable.

### Testing

Unit Tests: Write unit tests for individual functions and components, such as API request handlers, pagination logic, and database interactions, where applicable.

Integration Tests: Ensure that key flows (e.g., saving a movie, viewing saved movies, and deleting a movie) work as expected from end to end.

## Non-Functional Requirements

### Technologies

Backend: Node.js/Express (JavaScript/TypeScript), Python, Java, or Rust
Frontend: HTML, CSS, JavaScript (or a frontend framework if preferred)
Database: PostgreSQL or MySQL
Hosting: Deployed on a live URL or IP address (e.g., Heroku, DigitalOcean, AWS, etc.)
Version Control: Git

### Performance

Ensure that the app loads efficiently and handles multiple API requests without performance degradation.

Implement database indexing where applicable to optimize search and retrieval operations.

### Security

Sanitize user inputs to prevent SQL injection and other security vulnerabilities.

If user authentication is implemented, secure routes that handle sensitive data.

### Scalability

The backend should be designed to handle a reasonable number of concurrent users.

The app should implement pagination in both the search and saved movies pages to manage data load.

### Deployment

The application should be deployed on a platform that supports Node.js/Python/Java/Rust applications (e.g., Heroku, AWS, DigitalOcean).

Ensure that environment variables (e.g., database credentials) are securely managed.

## Deliverables

- Source Code: Git repository containing the full application code.
- Documentation: README file with setup instructions, API usage, and deployment instructions.
- Tests: Unit and/or integration tests included in the repository.
- Live URL: A live URL or IP address where the application is deployed.
- Git Access: Ensure the team has access to the Git repository.
