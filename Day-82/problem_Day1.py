# Here I am showing Problem Solve Day 2

# Performance Testing:
# Write a Python script that automates load testing of a web application, simulating user traffic and collecting performance metrics.

from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  # Wait time between tasks in seconds

    @task
    def my_task(self):
        self.client.get("/")  # Replace with the URL you want to test

    # You can add more tasks to simulate different user interactions

if __name__ == '__main__':
    import os
    import time
    from locust import events, runners

    # Define the number of users and hatch rate for the test
    num_users = int(os.environ.get("LOCUST_NUM_USERS", 10))
    hatch_rate = int(os.environ.get("LOCUST_HATCH_RATE", 2))

    # Start the Locust runner with the desired user count and hatch rate
    runner = runners.locust_runner
    runner.start(user_count=num_users, hatch_rate=hatch_rate)

    # Run the load test for a specified duration (in seconds)
    test_duration = int(os.environ.get("LOCUST_TEST_DURATION", 60))
    time.sleep(test_duration)

    # Stop the Locust runner
    runner.quit()
