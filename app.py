import requests
from flask import Flask, jsonify

app = Flask(__name__)


def get_gists(username):
    """
    Fetches the public Gists of a GitHub user.

    Parameters:
        username (str): GitHub username of the user.

    Returns:
        list: A list of dictionaries containing Gist details.
              Each dictionary represents a single Gist.
              Returns None if the user is not found or API is down.

    Example:
    [
        {
            "id": "12345",
            "url": "https://gist.github.com/username/12345",
            "description": "A sample Gist",
            "created_at": "2023-08-06T12:34:56Z"
        },
        ...
    ]
    """
    try:
        url = f"https://api.github.com/users/{username}/gists"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching data from GitHub API:", e)
    return None


@app.route('/<username>', methods=['GET'])
def user_gists(username):
    """
    Retrieves a list of publicly available Gists for the specified GitHub user.

    Parameters:
        username (str): GitHub username of the user.

    Returns:
        json: JSON response containing the list of Gists or an error message.

    Example:
    [
        {
            "id": "12345",
            "url": "https://gist.github.com/username/12345",
            "description": "A sample Gist",
            "created_at": "2023-08-06T12:34:56Z"
        },
        ...
    ]
    """
    gists = get_gists(username)
    if gists:
        return jsonify(gists)
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
