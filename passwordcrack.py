import itertools
import string
import time


def crack_password(
    target: str,
    max_length: int,
    quiet: bool = False,
) -> tuple[str | None, int, float]:
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
    attempts = 0
    start = time.time()

    for length in range(1, max_length + 1):
        for candidate_tuple in itertools.product(charset, repeat=length):
            attempts += 1
            candidate = "".join(candidate_tuple)
            if not quiet:
                print(candidate)
            if candidate == target:
                elapsed = time.time() - start
                return candidate, attempts, elapsed

    elapsed = time.time() - start
    return None, attempts, elapsed


def main() -> None:
    target = input("Enter the password that will attempted to be cracked: ")
    max_length_raw = input("length: ")
    quiet_raw = input("Quiet mode? (shows you progress if set to false): ").strip().lower()
    quiet = quiet_raw == "true"

    try:
        max_length = int(max_length_raw)
    except ValueError:
        print("Max length must be a number.")
        return

    if max_length <= 0:
        print("Max length must be greater than 0.")
        return

    found, attempts, elapsed = crack_password(target, max_length, quiet=quiet)
    if found is not None:
        print(f"Found: {found}")
        print(f"Attempts: {attempts}")
        print(f"Time: {elapsed:.2f}s")
    else:
        print("Password could not be found, maybe try another length?")
        print(f"Number of Attempts: {attempts}")
        print(f"Elapsed Time: {elapsed:.2f}s")


if __name__ == "__main__":
    main()
