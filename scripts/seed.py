import requests
import logging


class Seed():
    def __init__(self):
        """
        max number of users by page = 100
        """
        self.git_users_list_url = "https://api.github.com/users"

    def get_users(
        self,
        num_users: int,
        since_id: int = 0
    ) -> dict:
        users = []
        # number of users returned correctly
        users_by_page = 45
        ranges = [a for a in range(since_id, num_users, users_by_page)]
        while len(users) < num_users:
            url = "{url}?since={since_id}?per_page={per_page}".format(
                url=self.git_users_list_url,
                since_id=since_id,
                per_page=users_by_page
            )
            _ = requests.get(
                url
            )
            if _.status_code == 200:
                users = users + _.json()
                since_id = since_id + users_by_page
            else:
                logging.error(
                    "Request fails with status code {}".format(
                        _.status_code
                    )
                )
                if _.raise_for_status():
                    logging.error(_.raise_for_status())
                return None
        return users


if __name__ == "__main__":
    import arparse
    import sqlite3
    parser = argparse.ArgumentParser(
        description="""
            This tool populate a DB with a sertain number of
            users from git hub
        """
    )
    parser.add_argument(
        '-t',
        '--total',
        type=int,
        help="""
            A total of users to get from github, this number of
            users will be consulting by an API tested with a correct
            number of results of 45 users by query in an unauthenticated
            version, this free version also allow 60 queries by hour
        """
    )
    
