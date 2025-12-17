from shutil import get_terminal_size

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    count = 0
    term_width = get_terminal_size().columns
    bar_len = max(10, term_width - 40)

    for elem in lst:
        count += 1
        prog = count / total
        filled_len = int(bar_len * prog)

        bar = "█" * filled_len + " " * (bar_len - filled_len)
        percent = int(prog * 100)

        print(f"\r{percent:3d}%|{bar}| {count}/{total}", end="", flush=True)
        yield elem

# from time import sleep
# from tqdm import tqdm

# for elem in ft_tqdm(range(333)):
#     sleep(0.005)
# print()
# for elem in tqdm(range(333)):
#     sleep(0.005)
# print()