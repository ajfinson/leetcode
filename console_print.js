#!/usr/bin/env node
/**
 * Simple JavaScript file for console printing examples.
 */

// Part 1: Direct code execution (no function)
console.log("=== Part 1: Direct Execution ===");
console.log("Hello from JavaScript!");
const message = "This is a simple print statement";
console.log(message);
console.log(`2 + 2 = ${2 + 2}`);
console.log();

// Part 2: Function definition and call
console.log("=== Part 2: Function Call ===");

/**
 * Function that prints a greeting message.
 * @param {string} name - The name to greet
 */
function greet(name) {
    console.log(`Hello, ${name}!`);
    console.log(`Welcome to JavaScript programming.`);
}

/**
 * Function that calculates and prints the sum of two numbers.
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} The sum of a and b
 */
function calculateSum(a, b) {
    const result = a + b;
    console.log(`The sum of ${a} and ${b} is ${result}`);
    return result;
}

// Calling the functions
greet("World");
calculateSum(10, 20);
