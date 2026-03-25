from functools import lru_cache


@lru_cache
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def main() -> None:
    for i in range(0, 40):
        print(f"fib({i}) = {fib(i)}")


if __name__ == "__main__":
    main()
