import base64
import hashlib


def generate_short_url_for_user(url: str, user_id: str, encoding: str = "base64") -> str:
    """
    Generate a short URL for the user
    :param url: URL to shorten
    :param user_id: User ID
    :param encoding: Encoding to use
    :return: Shortened URL
    """
    encoding_text = f"{url}:{user_id}"

    if encoding == "base64":
        return base64.urlsafe_b64encode(encoding_text.encode("utf-8")).decode("utf-8")
    elif encoding == "md5":
        return hashlib.md5(encoding_text.encode("utf-8")).hexdigest()
    else:
        raise ValueError("Invalid encoding")


if __name__ == "__main__":
    print(generate_short_url_for_user("https://example.com", "user123"))
    print(generate_short_url_for_user("https://example.com", "user123", "md5"))
    print(generate_short_url_for_user("https://example.com", "user123", "sha256"))
