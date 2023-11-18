# GitHub Repository Finder

This Python script (`app.py`), when run as a cron job inside a Docker container, searches for GitHub repositories with "good first issues" and stores the results in a CSV file.

## Prerequisites

- Docker installed on your machine ([Install Docker](https://docs.docker.com/get-docker/))
- A GitHub token with the necessary permissions to access the GitHub API ([Generate GitHub Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token))

## Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/github-repo-finder.git
   cd github-repo-finder
   ```

2. **Create a .env File:**
Create a .env file in the project directory and add your GitHub token:
```GITHUB_TOKEN=your_actual_github_token```

3. **Build and Run the Docker Image with Docker Compose:**
Build the Docker image and run the container using Docker Compose:
```bash
docker-compose up -d
```
<t>
Replace your_actual_github_token with your GitHub token.

4. **Check the Output:**
After the container has run, you should find a repositories.csv file in your current working directory on the host.

## Cron Job Configuration
By default, the cron job is set to run the script every day at 8 AM. You can adjust the cron schedule in the Dockerfile if needed.

## Customization
- Modify the search query in app.py if you want to search for different criteria.
- Adjust the Dockerfile and Python script according to your specific requirements.

## Important Notes
- Treat your GitHub token like a password. Keep it confidential and avoid sharing it publicly.
- Be aware of GitHub API rate limits and adjust your script accordingly if needed.
- The entire current working directory is mounted as a volume, allowing the script's output and the CSV file to be stored in the same directory as your project.
