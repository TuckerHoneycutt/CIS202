#ifndef PIZZA_CALCULATOR_HPP
#define PIZZA_CALCULATOR_HPP

#include <vector>

class PizzaCalculator {
private:
    const int SLICES_PER_PIZZA = 8;
    const int FAMILY_SIZE = 4;
    
    std::vector<int> family_slices;
    int total_slices;
    int pizzas_needed;
    int leftover_slices;

    // Helper function to get valid input
    int get_slices(int person_num);
    // Calculate pizza requirements
    void calculate_totals();

public:
    PizzaCalculator();
    void get_family_orders();
    void display_results() const;
};

#endif
