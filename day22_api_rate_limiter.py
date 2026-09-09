import time


class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = float(capacity)
        self.refill_rate = refill_rate
        self.last_refill = time.monotonic()

    def refill(self):
        now = time.monotonic()
        elapsed = now - self.last_refill

        self.tokens = min(
            self.capacity,
            self.tokens + elapsed * self.refill_rate
        )

        self.last_refill = now

    def allow_request(self):
        self.refill()

        if self.tokens >= 1:
            self.tokens -= 1
            return True

        return False

    def available_tokens(self):
        self.refill()
        return self.tokens


def main():
    print("=" * 70)
    print("       DAY 22 - API RATE LIMITING TOKEN BUCKET LOGIC")
    print("=" * 70)

    print("\nAuthorized defensive training environment.")
    print("Simulating API request-rate control locally.")

    capacity = 5
    refill_rate = 1

    bucket = TokenBucket(
        capacity=capacity,
        refill_rate=refill_rate
    )

    print("\nToken Bucket Configuration")
    print("-" * 70)
    print(f"Bucket capacity : {capacity} tokens")
    print(f"Refill rate     : {refill_rate} token/second")

    print("\nRequest Simulation")
    print("-" * 70)

    allowed = 0
    throttled = 0

    # Initial burst
    for request_number in range(1, 9):
        if bucket.allow_request():
            allowed += 1
            print(
                f"Request {request_number:02d} : ALLOWED   "
                f"| Tokens remaining: {bucket.available_tokens():.2f}"
            )
        else:
            throttled += 1
            print(
                f"Request {request_number:02d} : THROTTLED "
                f"| Tokens remaining: {bucket.available_tokens():.2f}"
            )

    print("\nWaiting for token refill...")
    time.sleep(2)

    print("\nRequests After Refill")
    print("-" * 70)

    for request_number in range(9, 12):
        if bucket.allow_request():
            allowed += 1
            print(
                f"Request {request_number:02d} : ALLOWED   "
                f"| Tokens remaining: {bucket.available_tokens():.2f}"
            )
        else:
            throttled += 1
            print(
                f"Request {request_number:02d} : THROTTLED "
                f"| Tokens remaining: {bucket.available_tokens():.2f}"
            )

    print("\n" + "=" * 70)
    print("             RATE LIMITING SUMMARY")
    print("=" * 70)

    print(f"Total requests simulated : {allowed + throttled}")
    print(f"Requests allowed         : {allowed}")
    print(f"Requests throttled       : {throttled}")

    print("\nSecurity Effect")
    print("-" * 70)
    print("[1] Requests consume available tokens.")
    print("[2] Requests are throttled when the bucket is empty.")
    print("[3] Tokens gradually refill over time.")
    print("[4] Bursts are permitted only within the configured capacity.")
    print("[5] Rate limiting reduces excessive request activity.")

    print("\n" + "=" * 70)
    print("             SIMULATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()