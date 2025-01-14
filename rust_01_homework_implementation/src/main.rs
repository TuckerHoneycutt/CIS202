use std::io::{self, Write};

const SLICES_PER_PIZZA: u32 = 8;
const FAMILY_SIZE: u32 = 4;

#[derive(Debug)]
enum Error {
    InvalidInput,
}

fn main() -> io::Result<()> {
    println!("Different number of slices for each person");

    let family_slices: Vec<u32> = (1..=FAMILY_SIZE)
        .map(|i| get_slices(i))
        .collect::<Result<_, _>>()?;

    let total_slices: u32 = family_slices.iter().sum();
    let pizzas_needed = (total_slices + SLICES_PER_PIZZA - 1) / SLICES_PER_PIZZA;
    let leftover_slices = (pizzas_needed * SLICES_PER_PIZZA) - total_slices;

    println!("\nOrder Summary:");

    for (i, &slices) in family_slices.iter().enumerate() {
        println!("Person {} wants {} slices", i + 1, slices);
    }

    println!("Total slices needed: {total_slices}");
    println!("Number of pizzas needed: {pizzas_needed}");
    println!("Number of leftover slices: {leftover_slices}");

    Ok(())
}

fn get_slices(person: u32) -> io::Result<u32> {
    loop {
        print!("Enter slices for person {person}: ");
        io::stdout().flush()?;

        let mut input = String::new();
        io::stdin().read_line(&mut input)?;

        match input.trim().parse() {
            Ok(slices) => return Ok(slices),
            Err(_) => println!("Please enter a valid number"),
        }
    }
}
