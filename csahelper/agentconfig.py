from google.genai import types

# Configure Model Retry on errors
retry_config = types.HttpRetryOptions(
    attempts=8,  # Maximum retry attempts
    exp_base=3,  # Delay multiplier
    initial_delay=1,
    http_status_codes=[429, 500, 503, 504],  # Retry on these HTTP errors
)
