#include "pizza_calculator.hpp"
#include <iostream>
#include <limits>

PizzaCalculator::PizzaCalculator() 
    : total_slices(0), pizzas_needed(0), leftover_slices(0) {
    family_slices.reserve(FAMILY_SIZE);
}

int PizzaCalculator::get_slices(int person_num) {
    int slices;
    while (true) {
        std::cout << "Enter slices for person " << person_num << ": ";
        if (std::cin >> slices) {
            return slices;
        }
        std::cout << "Please enter a valid number\n";
        std::cin.clear();
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
}

void PizzaCalculator::get_family_orders() {
    std::cout << "Different number of slices for each person\n";
    
    for (int i = 1; i <= FAMILY_SIZE; ++i) {
        family_slices.push_back(get_slices(i));
    }
    
    calculate_totals();
}

void PizzaCalculator::calculate_totals() {
    total_slices = 0;
    for (int slices : family_slices) {
        total_slices += slices;
    }
    
    pizzas_needed = (total_slices + SLICES_PER_PIZZA - 1) / SLICES_PER_PIZZA;
    leftover_slices = (pizzas_needed * SLICES_PER_PIZZA) - total_slices;
}

void PizzaCalculator::display_results() const {
    std::cout << "\nOrder Summary:\n";
    for (int i = 0; i < FAMILY_SIZE; ++i) {
        std::cout << "Person " << (i + 1) << " wants " 
                 << family_slices[i] << " slices\n";
    }
    
    std::cout << "Total slices needed: " << total_slices << '\n'
              << "Number of pizzas needed: " << pizzas_needed << '\n'
              << "Number of leftover slices: " << leftover_slices << '\n';
}
