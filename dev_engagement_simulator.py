import time

class DeveloperEngagementAPI:
    """
    A mock API client for a Developer Engagement Platform.
    Demonstrates principles of good Developer Experience (DevX) and Developer Relations (DevRel).
    """
    def __init__(self, api_key: str):
        """
        Initializes the API client.
        DevX Principle: Easy and clear setup for developers is crucial for adoption.
        """
        if not api_key or not api_key.startswith("devrel_"):
            raise ValueError("Invalid API Key. Must start with 'devrel_'.")
        self.api_key = api_key
        self.developers = {
            "dev123": {"name": "Alice Developer", "email": "alice@example.com", "community_score": 85},
            "dev456": {"name": "Bob Coder", "email": "bob@example.com", "community_score": 70},
        }
        print(f"API Client initialized successfully with key: {self.api_key[:8]}...")
        # Developer Marketing: A successful initialization message reassures the developer and promotes confidence.

    def get_developer_profile(self, dev_id: str) -> dict | None:
        """
        Fetches a developer's profile.
        DevX Principle: Clear function names, predictable output, and efficient access to information.
        """
        print(f"Fetching profile for developer ID: {dev_id}...")
        time.sleep(0.1) # Simulate network delay
        profile = self.developers.get(dev_id)
        if profile:
            print(f"  Profile found for {profile['name']}.")
        else:
            print(f"  Error: Developer with ID '{dev_id}' not found.")
            # DevX Principle: Provide helpful and specific error messages.
        return profile

    def publish_announcement(self, title: str, content: str, target_segment: str = "all") -> bool:
        """
        Publishes an announcement to the developer community.
        DevRel Principle: Facilitates one-to-many communication with the community, sharing updates and news.
        """
        print(f"\nPublishing announcement '{title}' to '{target_segment}' segment...")
        if not title or not content:
            print("  Error: Title and content cannot be empty.")
            return False
        # Simulate publishing to a database/message queue
        time.sleep(0.2)
        print(f"  Announcement '{title}' published successfully.")
        # Developer Marketing: This feature allows marketing teams to reach developers with product news.
        return True

    def log_developer_feedback(self, dev_id: str, feedback_message: str) -> bool:
        """
        Logs feedback from a specific developer.
        DevRel Principle: Provides a clear channel for developers to give feedback, fostering trust and improving products.
        """
        print(f"\nLogging feedback from developer ID {dev_id}...")
        if not self.developers.get(dev_id):
            print(f"  Error: Developer with ID '{dev_id}' does not exist. Cannot log feedback.")
            return False
        if not feedback_message:
            print("  Error: Feedback message cannot be empty.")
            return False
        # Simulate logging feedback
        time.sleep(0.1)
        print(f"  Feedback from {self.developers[dev_id]['name']} logged: '{feedback_message[:50]}...' (truncated)")
        # DevX Principle: A clear and reliable way to provide input significantly improves the developer experience.
        return True

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Developer Engagement API Client Simulation ---")
    print("This script demonstrates how good API design (DevX) supports DevRel and Developer Marketing efforts.")

    # Scenario 1: Successful API client initialization
    try:
        api_client = DeveloperEngagementAPI(api_key="devrel_abc123xyz")
    except ValueError as e:
        print(f"Initialization failed: {e}")
        exit(1)

    # Scenario 2: Get developer profiles
    print("\n--- Fetching Developer Profiles ---")
    alice_profile = api_client.get_developer_profile("dev123")
    if alice_profile:
        print(f"  Alice's Community Score: {alice_profile['community_score']}")

    bob_profile = api_client.get_developer_profile("dev456")

    # Scenario 3: Attempt to get a non-existent developer profile (demonstrates error handling)
    non_existent_profile = api_client.get_developer_profile("dev999")

    # Scenario 4: Publish an announcement
    print("\n--- Publishing Announcements ---")
    api_client.publish_announcement(
        title="New API Version Released!",
        content="We're excited to announce v2.0 of our API with improved performance and new features.",
        target_segment="all"
    )

    # Scenario 5: Log developer feedback
    print("\n--- Logging Developer Feedback ---")
    api_client.log_developer_feedback("dev123", "The new API documentation is fantastic! Very clear examples.")
    api_client.log_developer_feedback("dev456", "I'm having trouble with the authentication flow, could use more examples.")

    # Scenario 6: Demonstrate error handling for feedback (non-existent dev)
    api_client.log_developer_feedback("dev999", "This feedback should not be logged.")

    print("\n--- Simulation Complete ---")
