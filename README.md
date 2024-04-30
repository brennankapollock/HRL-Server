# Build Server Project

## Introduction
This repository contains the code for a build server designed to manage, build, and track the status of various software projects. It uses Flask for the backend, SQLAlchemy for database interactions, and a simple frontend to display build statuses.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/brennankapollock/HRL-Server.git
   ```

2. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up the environment variables:
   ```
   export DATABASE_URL="your_database_url"
   ```

## Usage

- Start the server:
   ```
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