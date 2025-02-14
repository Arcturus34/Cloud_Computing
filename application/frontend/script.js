let display = document.getElementById('display');

function appendNumber(number) {
  display.value += number;
}

function appendOperator(operator) {
  if (display.value !== '' && !isNaN(display.value.slice(-1))) {
    display.value += operator;
  }
}

function clearDisplay() {
  display.value = '';
}

async function calculateResult() {
  let expression = display.value;
  let regex = /^(\d+(\.\d+)?)([+\-*/])(\d+(\.\d+)?)$/;
  let match = expression.match(regex);

  if (!match) {
    display.value = 'Erreur';
    return;
  }

  let num1 = parseFloat(match[1]);
  let operator = match[3];
  let num2 = parseFloat(match[4]);

  let data = { num1, num2, operator };

  try {
    let response = await fetch('http://127.0.0.1:5000/api/calculate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });

    let resultData = await response.json();
    
    if (response.ok) {
      let operationId = resultData.operation_id;
      let resultResponse = await fetch(`http://127.0.0.1:5000/api/result/${operationId}`);
      let resultJson = await resultResponse.json();
      
      if (resultResponse.ok) {
        display.value = resultJson.result;
      } else {
        display.value = 'Erreur';
      }
    } else {
      display.value = resultData.error;
    }
  } catch (error) {
    display.value = 'Erreur serveur';
  }
}

