import os

# API base URLs
API_BASE_URL=os.getenv(
    "API_BASE_URL", 
    "https://jsonplaceholder.typicode.com"
)

AUTH_API_BASE_URL=os.getenv(
    "AUTH_API_BASE_URL",
     "https://httpbin.io"
)

#Request timeout in milliseconds
API_TIMEOUT=15000