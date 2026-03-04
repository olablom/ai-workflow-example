from datetime import datetime, timezone


def main():
    print("Hello from AI workflow example")
    ts = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    print(f"Timestamp: {ts}")


if __name__ == "__main__":
    main()
