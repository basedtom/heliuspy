import requests


def _send_request(url, headers=None, params=None, postdict=None, verb=None):
    """Send request to endpoint

    Args:
        params (str, optional): Query string for request. Defaults to None.
        variable_values (dict, optional): variables to populate query with. Defaults to None.
        max_retries (int, optional): Number of retry attempts. Defaults to 3.

    Returns:
        dict[str, any]: API response
    """
    if not verb:
        verb = "POST" if postdict else "GET"

    if not headers:
        headers = {"Content-Type": "application/json"}

    # Make the request
    if verb == "POST":
        response = requests.post(url, json=postdict, headers=headers)
    else:
        response = requests.get(url, params=params, headers=headers)

    return response.json()
