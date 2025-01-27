# Imagine a simple web portal at https://shop.ify, where users can input a “long” URL, submit the form, and receive a shortened URL on the next screen, presented in the form https://shop.ify/<shortened-key>.

# If someone were to navigate to https://shop.ify/<shortened-key> in their browser, it would redirect them to the long URL that was input by the original user.

# Eventually, we want this system to scale to be able to store thousands or millions of records, but we can start with the basics and st
# and store a couple mappings instead.

# Implement the following methods that the service will call to accomplish this functionality:
# def generate_short_key() -> str:
#     """Generate a valid short key."""
#     return "short-key"

# def create_entry(short_key: str | None, long_url: str) -> str:
#     """Create a mapping from short key to long URL.

#     Returns:
#     string -- the short key that was mapped to the long_url.
#     """
#     return


# def get_long_url_for(short_key: str) -> str | None:
#     """Get a long URL value for the given short key.

#     Returns:
#     None -- if there is no existing record for the passed in key.
# string -- if there is a matching record for the passed in key.
#     """
#     return

import uuid 
class URLShortener:

    url_mapping = {}

    def generate_short_key(self, url):
        id = str(uuid.uuid4())[:8]
        short_key = f"https://shop.ify/{id}"

        self.url_mapping[short_key] = url

        print(short_key)

    def get_long_url(self, short_key):
        long_url = self.url_mapping.get(short_key)

        return long_url
    

class UrlShortenerCLI:
    def __init__(self):
        self.url_shortener = URLShortener()

    def run(self):
        while True:
            long_url = input("Enter a long URL: ")
            self.url_shortener.generate_short_key(long_url)

            short_key = input("Enter a short key: ")
            print(self.url_shortener.get_long_url(short_key))

if __name__ == "__main__":
    url_shortener = UrlShortenerCLI()
    url_shortener.run()

