"""
==============================================================================
Project:     Linear Programming Graphical Solver
File:        main.py
Author:      Yevhen Biezhyn
Description: Unified CLI orchestrator for 2D Linear Programming problems.
             Computes constraint boundaries, feasible regions, and visualizes
             optimization models using NumPy and Matplotlib.
==============================================================================
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
from typing import Optional


def plot_problem_1(save_path: Optional[str] = None):
    """Problem 1: Produktionsplanung (Hemden x1, Pyjamas x2)"""
    x1 = np.linspace(0, 300, 500)
    y1 = (280 - x1) / 0.75  # x1 + 0.75*x2 <= 280
    y2 = (450 - 1.5 * x1) / 2.0  # 1.5*x1 + 2*x2 <= 450

    plt.figure(figsize=(8, 6))
    plt.plot(x1, y1, 'b-', label=r'$x_1 + 0.75x_2 \leq 280$')
    plt.plot(x1, y2, 'g-', label=r'$1.5x_1 + 2x_2 \leq 450$')

    feasible = np.minimum(y1, y2)
    feasible = np.clip(feasible, 0, np.inf)
    plt.fill_between(x1, feasible, color='gray', alpha=0.35, label='Zulaessiger Bereich (Feasible Region)')

    plt.xlim(0, 300)
    plt.ylim(0, 240)
    plt.xlabel(r'$x_1$ (Anzahl Hemden / Shirts)')
    plt.ylabel(r'$x_2$ (Anzahl Pyjamas)')
    plt.title('Problem 1: Produktions- und Ressourcenallokation')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    _finish_plot(save_path, "problem_1.png")


def plot_problem_2(save_path: Optional[str] = None):
    """Problem 2: 2x1 + x2 <= 40, x1 + 3x2 <= 30"""
    x1 = np.linspace(0, 30, 500)
    y1 = 40 - 2 * x1
    y2 = (30 - x1) / 3.0

    plt.figure(figsize=(8, 6))
    plt.plot(x1, y1, 'b-', label=r'$2x_1 + x_2 \leq 40$')
    plt.plot(x1, y2, 'g-', label=r'$x_1 + 3x_2 \leq 30$')

    feasible = np.minimum(y1, y2)
    feasible = np.clip(feasible, 0, np.inf)
    plt.fill_between(x1, feasible, color='gray', alpha=0.35, label='Zulaessiger Bereich')

    plt.xlim(0, 30)
    plt.ylim(0, 25)
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.title('Problem 2: Lineare Restriktionen mit zwei Schranken')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    _finish_plot(save_path, "problem_2.png")


def plot_problem_3(save_path: Optional[str] = None):
    """Problem 3: 4x + 3y <= 36, 2x + 4y <= 40, x >= 3"""
    x = np.linspace(0, 12, 500)
    y1 = (36 - 4 * x) / 3.0
    y2 = (40 - 2 * x) / 4.0
    x_min = 3.0

    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, 'b-', label=r'$4x + 3y \leq 36$')
    plt.plot(x, y2, 'g-', label=r'$2x + 4y \leq 40$')
    plt.axvline(x=x_min, color='red', linestyle='--', label=r'$x \geq 3$')

    y_upper = np.minimum(y1, y2)
    y_upper = np.clip(y_upper, 0, np.inf)
    plt.fill_between(x, y_upper, where=(x >= x_min), color='gray', alpha=0.35, label='Zulaessiger Bereich')

    plt.xlim(0, 12)
    plt.ylim(0, 14)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Problem 3: Beschraenkter Bereich mit Mindestschranke x >= 3')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    _finish_plot(save_path, "problem_3.png")


def plot_problem_4(save_path: Optional[str] = None):
    """Problem 4: x + y <= 12, x + 2y <= 20, x >= 2"""
    x = np.linspace(0, 16, 500)
    y1 = 12 - x
    y2 = (20 - x) / 2.0
    x_min = 2.0

    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, 'b-', label=r'$x + y \leq 12$')
    plt.plot(x, y2, 'g-', label=r'$x + 2y \leq 20$')
    plt.axvline(x=x_min, color='red', linestyle='--', label=r'$x \geq 2$')

    y_upper = np.minimum(y1, y2)
    y_upper = np.clip(y_upper, 0, np.inf)
    plt.fill_between(x, y_upper, where=(x >= x_min), color='gray', alpha=0.35, label='Zulaessiger Bereich')

    plt.xlim(0, 16)
    plt.ylim(0, 14)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Problem 4: Simplex-Restriktionspolygon')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    _finish_plot(save_path, "problem_4.png")


def plot_problem_5(save_path: Optional[str] = None):
    """Problem 5: Minimierungsproblem x1 + 2x2 >= 80, 3x1 + x2 >= 75"""
    x1 = np.linspace(0, 100, 500)
    x2_1 = (80 - x1) / 2.0
    x2_2 = 75 - 3 * x1

    plt.figure(figsize=(8, 6))
    plt.plot(x1, x2_1, 'b-', label=r'$x_1 + 2x_2 \geq 80$')
    plt.plot(x1, x2_2, 'g-', label=r'$3x_1 + x_2 \geq 75$')

    y_lower = np.maximum(x2_1, x2_2)
    y_lower = np.clip(y_lower, 0, np.inf)
    plt.fill_between(x1, y_lower, 60, color='gray', alpha=0.35, label='Zulaessiger Bereich (Nach oben unbeschraenkt)')

    plt.xlim(0, 90)
    plt.ylim(0, 60)
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.title('Problem 5: Minimierungsraum mit unteren Ungleichungen')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    _finish_plot(save_path, "problem_5.png")


def _finish_plot(save_path: Optional[str], default_filename: str):
    if save_path:
        filename = save_path if save_path.endswith(".png") else default_filename
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"[+] Diagramm erfolgreich gespeichert unter: {filename}")
        plt.close()
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(description="2D Linear Programming Graphical Solver")
    parser.add_argument("--problem", type=int, choices=[1, 2, 3, 4, 5], default=1,
                        help="Nummer des Optimierungsproblems (1 bis 5)")
    parser.add_argument("--all", action="store_true", help="Visualisiert alle 5 Probleme nacheinander")
    parser.add_argument("--save", action="store_true",
                        help="Speichert Diagramme als Bilddateien anstatt sie anzuzeigen")
    args = parser.parse_args()

    problem_map = {
        1: plot_problem_1,
        2: plot_problem_2,
        3: plot_problem_3,
        4: plot_problem_4,
        5: plot_problem_5,
    }

    if args.all:
        for num, fn in problem_map.items():
            print(f"[*] Visualisiere Problem {num}...")
            fn(save_path=f"problem_{num}.png" if args.save else None)
    else:
        print(f"[*] Visualisiere Problem {args.problem}...")
        problem_map[args.problem](save_path=f"problem_{args.problem}.png" if args.save else None)


if __name__ == "__main__":
    main()
