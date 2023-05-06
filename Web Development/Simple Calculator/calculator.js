// All output values are rounded to 5 decimals if their result
// should contain decimal values

// Converts values toDegrees for Sin, Cos, and Tan Operations
function toDegrees(radians) {
    return radians * (Math.PI / 180);
}

// If the result has more than 7 decimals, the result will then
// be rounded down to 5 decimal points
function roundToFive(output) {
    var resultOutput = document.querySelector("#output-text");
    if (String(output).includes(".")) {
        var digits = String(output).split(".");
        if (String(digits[1].length) >= 7) {
            resultOutput.value = output.toFixed(5);
        } else {
            resultOutput.value = output;
        }
    } else {
        resultOutput.value = output;
    }
}

function revealValue(n) {
    document.querySelector("#output-text").value += n;
}

function clearText () {
    document.querySelector("#output-text").value = "";
}

function sinOperation(userInput) {
    var output = toDegrees(userInput.substr(4, userInput.length));
    roundToFive(Math.sin(output));
}

function cosOperation(userInput) {
    var output = toDegrees(userInput.substr(4, userInput.length));
    roundToFive(Math.cos(output));
}

function tanOperation(userInput) {
    var output = toDegrees(userInput.substr(4, userInput.length));
    roundToFive(Math.tan(output));  
}

function performOperation() {
    var userInput = document.querySelector("#output-text").value;

    if (userInput.includes("Sin")) {
        sinOperation(userInput);
    } else if (userInput.includes("Cos")) {
        cosOperation(userInput);
    } else if (userInput.includes("Tan")) {
        tanOperation(userInput);
    } else {
        var output = eval(userInput);
        roundToFive(output);
    }
}