### README.md for the Current Repository

Below is a suggested [README.md](file:///Users/brennanpollock/Code/HRL/README.md#1%2C1-1%2C1) for the current repository, which seems to be a build server setup for managing and building projects:

```markdown
# Build Server Project

## Introduction
This repository contains the code for a build server designed to manage, build, and track the status of various software projects. It uses Flask for the backend, SQLAlchemy for database interactions, and a simple frontend to display build statuses.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-repository-url.git
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the environment variables:
   ```bash
   export DATABASE_URL="your_database_url"
   ```

## Usage

- Start the server:
  ```bash
  python app.py
  ```
- Access the build dashboard at `http://localhost:5000/status` to view the status of all projects.

## Features

- **Automatic Commit Checks**: Periodically checks for new commits in registered repositories.
- **Build Triggering**: Manually trigger builds for any registered project.
- **Artifact Management**: Download the latest successful build artifacts.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
```

This README provides a concise yet comprehensive overview of the project, including how to set it up, use it, and contribute to it. Adjust the repository URL and any specific details as necessary to match your project's configuration.
