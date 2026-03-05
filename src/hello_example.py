import argparse
from datetime import datetime, timezone


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", action="store_true", help="Append a run line to artifacts/run_log.txt")
    args = parser.parse_args()

    ts = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    print("Hello from AI workflow example")
    print(f"Timestamp: {ts}")

    if args.log:
        log_path = "artifacts/run_log.txt"
        with open(log_path, "a") as f:
            f.write("Run logged\n")


if __name__ == "__main__":
    main()
