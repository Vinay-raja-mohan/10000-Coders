const calculator = {
    displayValue: '0',
    firstOperand: null,
    waitingForSecondOperand: false,
    operator: null,
};

function toggleTheme() {
    document.body.classList.toggle('light-mode');
    const toggler = document.querySelector('.theme-toggler');
    if (document.body.classList.contains('light-mode')) {
        toggler.textContent = '🌙';
    } else {
        toggler.textContent = '☀️';
    }
}

function inputDigit(digit) {
    const { displayValue, waitingForSecondOperand } = calculator;

    if (waitingForSecondOperand === true) {
        calculator.displayValue = digit;
        calculator.waitingForSecondOperand = false;
    } else {
        calculator.displayValue = displayValue === '0' ? digit : displayValue + digit;
    }
}

function inputDecimal(dot) {
    if (calculator.waitingForSecondOperand === true) return;

    if (!calculator.displayValue.includes(dot)) {
        calculator.displayValue += dot;
    }
}

function handleOperator(nextOperator) {
    const { firstOperand, displayValue, operator } = calculator;
    const inputValue = parseFloat(displayValue);

    if (operator && calculator.waitingForSecondOperand) {
        calculator.operator = nextOperator;
        return;
    }

    if (firstOperand == null) {
        calculator.firstOperand = inputValue;
    } else if (operator) {
        const currentValue = firstOperand || 0;
        const result = performCalculation[operator](currentValue, inputValue);

        calculator.displayValue = String(result);
        calculator.firstOperand = result;

        // Save to History
        if (operator !== '=') {
            // Logic for intermediate steps if needed, but for simple calc usually only on =
        }
    }

    calculator.waitingForSecondOperand = true;
    calculator.operator = nextOperator;
}

// History Feature
let history = [];

function toggleHistory() {
    document.querySelector('.calculator-inner').classList.toggle('flipped');
}

function clearHistory() {
    history = [];
    renderHistory();
}

function addToHistory(expression, result) {
    history.unshift({ expression, result });
    if (history.length > 20) history.pop(); // Keep last 20
    renderHistory();
}

function renderHistory() {
    const list = document.querySelector('.history-list');
    list.innerHTML = '';

    history.forEach(item => {
        const div = document.createElement('div');
        div.className = 'history-item';
        div.innerHTML = `
            <span class="expression">${item.expression}</span>
            <span class="result">= ${item.result}</span>
        `;
        list.appendChild(div);
    });
}

const performCalculation = {
    '/': (firstOperand, secondOperand) => {
        const result = firstOperand / secondOperand;
        addToHistory(`${firstOperand} ÷ ${secondOperand}`, result);
        return result;
    },
    '*': (firstOperand, secondOperand) => {
        const result = firstOperand * secondOperand;
        addToHistory(`${firstOperand} × ${secondOperand}`, result);
        return result;
    },
    '+': (firstOperand, secondOperand) => {
        const result = firstOperand + secondOperand;
        addToHistory(`${firstOperand} + ${secondOperand}`, result);
        return result;
    },
    '-': (firstOperand, secondOperand) => {
        const result = firstOperand - secondOperand;
        addToHistory(`${firstOperand} - ${secondOperand}`, result);
        return result;
    },
    '=': (firstOperand, secondOperand) => secondOperand
};

function resetCalculator() {
    calculator.displayValue = '0';
    calculator.firstOperand = null;
    calculator.waitingForSecondOperand = false;
    calculator.operator = null;
}

function updateDisplay() {
    const display = document.querySelector('.calculator-screen');
    display.value = calculator.displayValue;
}

updateDisplay();

function handleBackspace() {
    if (calculator.waitingForSecondOperand) {
        return;
    }

    // If it's single digit, change to '0'
    if (calculator.displayValue.length === 1) {
        calculator.displayValue = '0';
    } else {
        // Remove last character
        calculator.displayValue = calculator.displayValue.slice(0, -1);
    }
}

function inputPercent() {
    const value = parseFloat(calculator.displayValue);
    calculator.displayValue = String(value / 100);
}

const keys = document.querySelector('.calculator-keys');
keys.addEventListener('click', (event) => {
    const { target } = event;
    if (!target.matches('button')) {
        return;
    }

    if (target.classList.contains('operator')) {
        handleOperator(target.value);
        updateDisplay();
        return;
    }

    if (target.classList.contains('decimal')) {
        inputDecimal(target.value);
        updateDisplay();
        return;
    }

    if (target.classList.contains('all-clear')) {
        resetCalculator();
        updateDisplay();
        return;
    }

    if (target.classList.contains('delete-btn')) {
        handleBackspace();
        updateDisplay();
        return;
    }

    if (target.classList.contains('percentage')) {
        inputPercent();
        updateDisplay();
        return;
    }

    inputDigit(target.value);
    updateDisplay();
});

document.addEventListener('keydown', (event) => {
    const { key } = event;

    if (/[0-9]/.test(key)) {
        inputDigit(key);
        updateDisplay();
    } else if (key === '.') {
        inputDecimal(key);
        updateDisplay();
    } else if (key === '+' || key === '-' || key === '*' || key === '/') {
        handleOperator(key);
        updateDisplay();
    } else if (key === 'Enter' || key === '=') {
        event.preventDefault(); // Prevent default action for Enter key
        handleOperator('=');
        updateDisplay();
    } else if (key === 'Backspace') {
        handleBackspace();
        updateDisplay();
    } else if (key === 'Escape') {
        resetCalculator();
        updateDisplay();
    } else if (key === '%') {
        inputPercent();
        updateDisplay();
    }
});
