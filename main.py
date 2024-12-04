//scrap data from Tiktok and instagram using python playwright script

from playwright.sync_api import sync_playwright
import time
import json

# Function to scrape TikTok profile data
def scrape_tiktok_profile(username):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for headless mode
        page = browser.new_page()
        
        # Navigate to the TikTok user profile
        page.goto(f"https://www.tiktok.com/@{username}")
        time.sleep(2)  # Wait for the page to load
        
        # Example: Scrape the number of followers, following, and likes
        followers = page.query_selector("strong[data-e2e='followers-count']").inner_text()
        following = page.query_selector("strong[data-e2e='following-count']").inner_text()
        likes = page.query_selector("strong[data-e2e='likes-count']").inner_text()
        
        data = {
            'username': username,
            'followers': followers,
            'following': following,
            'likes': likes
        }
        
        print(f"TikTok Profile Data: {json.dumps(data, indent=2)}")
        
        browser.close()

# Function to scrape Instagram profile data
def scrape_instagram_profile(username, cookies):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Change to True for headless mode
        page = browser.new_page()
        
        # Set cookies (use cookies from your browser or use a method to log in)
        page.context.add_cookies(cookies)
        
        # Navigate to the Instagram user profile
        page.goto(f"https://www.instagram.com/{username}/")
        time.sleep(2)  # Wait for the page to load
        
        # Scrape the number of followers, following, and posts (visible in the header)
        followers = page.query_selector('span[class="k9GMp "]').inner_text()
        following = page.query_selector('a[href="/{username}/following/"]').inner_text()
        posts = page.query_selector('span[class="g47SY "]').inner_text()
        
        data = {
            'username': username,
            'followers': followers,
            'following': following,
            'posts': posts
        }
        
        print(f"Instagram Profile Data: {json.dumps(data, indent=2)}")
        
        browser.close()

# Example usage for TikTok
tiktok_username = "your_tiktok_username"
scrape_tiktok_profile(tiktok_username)

# Example usage for Instagram
# For Instagram, you must have the cookies stored from a valid login session
instagram_username = "your_instagram_username"
instagram_cookies = [
    {
        "name": "sessionid",
        "value": "your_sessionid_cookie_value",
        "domain": ".instagram.com",
        "path": "/",
        "httpOnly": True,
        "secure": True,
        "sameSite": "Strict"
    }
]
scrape_instagram_profile(instagram_username, instagram_cookies)
