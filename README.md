# GitHub Gists API

This is a simple HTTP API written in Python3 using Flask that interacts with the GitHub API and responds to requests for a specific GitHub user's Gists.

## Setup and Run

1. Install Docker on your system.
2. Clone this repository to your local machine.

```bash
git clone https://github.com/linuxdynasty/ee-test-1.git
cd ee-test-1

# Build the Docker image using the following command:
docker build -t gist-api .
# Run the Docker container:
docker run -p 8080:8080 gist-api
```

The API will be accessible at `<http://localhost:8080/><USER>`, where `<USER>` is the GitHub username you want to retrieve Gists for (e.g., `<http://localhost:8080/octocat>`)

## Usage

To retrieve a list of publicly available Gists for a GitHub user, simply send a GET request to the API endpoint with the GitHub username as the parameter.

Example using cURL: `curl http://localhost:8080/octocat`

Example Response:

```json
[
    {
        "id": "12345",
        "url": "https://gist.github.com/octocat/12345",
        "description": "A sample Gist",
        "created_at": "2023-08-06T12:34:56Z"
    },
    ...
]
```

## Automated Tests

The repository includes automated tests to verify the API's functionality. To run the tests, execute the following command: `python tests.py
` ( **while the application is running.** )

## API Documentation

API Endpoints
    `GET /<USER>`: Retrieves a list of publicly available Gists for the specified GitHub user.

Parameters:
    USER (str): GitHub username of the user.
Response:
    Success (200): JSON response containing the list of Gists.
    Not Found (404): JSON response containing an error message if the user is not found.
