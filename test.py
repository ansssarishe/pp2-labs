import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sorting Algorithm Visualization')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Generate a random list
def generate_random_list(size):
    lst = list(range(1, size + 1))
    random.shuffle(lst)
    return lst

# Draw the list
def draw_list(lst, color_positions={}):
    screen.fill(BLACK)
    bar_width = width // len(lst)
    max_val = max(lst)
    for i, val in enumerate(lst):
        color = color_positions.get(i, GREEN)
        scaled_height = (val / max_val) * height
        pygame.draw.rect(screen, color, (i * bar_width, height - scaled_height, bar_width, scaled_height))
        pygame.draw.rect(screen, BLACK, (i * bar_width, height - scaled_height, bar_width, scaled_height), 1)  # Border
    pygame.display.flip()

# Bubble Sort Algorithm
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                draw_list(lst, {j: RED, j+1: GREEN})
                yield True

# Selection Sort Algorithm
def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
            draw_list(lst, {j: RED, min_idx: GREEN})
            yield True
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        draw_list(lst, {i: GREEN, min_idx: RED})
        yield True

# Insertion Sort Algorithm
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            draw_list(lst, {j: RED, j + 1: GREEN})
            yield True
            j -= 1
        lst[j + 1] = key
        draw_list(lst, {j + 1: GREEN})
        yield True

# Merge Sort Algorithm
def merge_sort(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        L = lst[:mid]
        R = lst[mid:]

        yield from merge_sort(L)
        yield from merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1
            else:
                lst[k] = R[j]
                j += 1
            draw_list(lst, {k: GREEN})
            yield True
            k += 1

        while i < len(L):
            lst[k] = L[i]
            i += 1
            draw_list(lst, {k: GREEN})
            yield True
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            draw_list(lst, {k: GREEN})
            yield True
            k += 1

# Quick Sort Algorithm
def quick_sort(lst):
    def partition(low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                draw_list(lst, {i: RED, j: GREEN})
                yield True
        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        draw_list(lst, {i + 1: RED, high: GREEN})
        yield True
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = yield from partition(low, high)
            yield from quick_sort_recursive(low, pi - 1)
            yield from quick_sort_recursive(pi + 1, high)

    yield from quick_sort_recursive(0, len(lst) - 1)

# Heap Sort Algorithm
def heap_sort(lst):
    def heapify(n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and lst[i] < lst[l]:
            largest = l

        if r < n and lst[largest] < lst[r]:
            largest = r

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            draw_list(lst, {i: RED, largest: GREEN})
            yield True
            yield from heapify(n, largest)

    n = len(lst)

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_list(lst, {i: RED, 0: GREEN})
        yield True
        yield from heapify(i, 0)

# Main function
def main():
    lst = generate_random_list(100)
    sorting = False
    sorting_algorithm = None
    algorithm_name = "None"
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not sorting:
                    sorting = True
                if event.key == pygame.K_1:
                    sorting_algorithm = bubble_sort(lst)
                    algorithm_name = "Bubble Sort"
                    sorting = True
                if event.key == pygame.K_2:
                    sorting_algorithm = selection_sort(lst)
                    algorithm_name = "Selection Sort"
                    sorting = True
                if event.key == pygame.K_3:
                    sorting_algorithm = insertion_sort(lst)
                    algorithm_name = "Insertion Sort"
                    sorting = True
                if event.key == pygame.K_4:
                    sorting_algorithm = merge_sort(lst)
                    algorithm_name = "Merge Sort"
                    sorting = True
                if event.key == pygame.K_5:
                    sorting_algorithm = quick_sort(lst)
                    algorithm_name = "Quick Sort"
                    sorting = True
                if event.key == pygame.K_6:
                    sorting_algorithm = heap_sort(lst)
                    algorithm_name = "Heap Sort"
                    sorting = True
                if event.key == pygame.K_r:
                    lst = generate_random_list(100)
                    sorting = False
                    sorting_algorithm = None
                    algorithm_name = "None"

        if sorting and sorting_algorithm:
            try:
                next(sorting_algorithm)
            except StopIteration:
                sorting = False

        draw_list(lst)
        pygame.display.set_caption(f'Sorting Algorithm Visualization - {algorithm_name}')
        clock.tick(60)

if __name__ == "__main__":
    main()