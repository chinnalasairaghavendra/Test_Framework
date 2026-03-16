import os


class Config:

    BASE_URL = os.getenv(
        "BASE_URL",
        "https://react-frontend-api-testing.vercel.app"
    )

    BROWSER = os.getenv("BROWSER", "chrome")

    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

    GRID_URL = os.getenv("GRID_URL", None)