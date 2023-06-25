function clearbutton() 
{
    let input =document.getElementById("result");
    input.value="";
  }
function display(value) 
{
    let output=document.getElementById("result");
    output.value +=value;
  }
function calculate() 
{
let expression = document.getElementById("result").value;
let result = math.evaluate(expression);
switch (typeof result) 
{
    case "undefined":
        document.getElementById("result").value = "";
        break;
    default:
        document.getElementById("result").value = result;
        break;
}
}
function Scientificfunction(func) 
{
let expression = document.getElementById("result").value;
let angle = math.evaluate(expression);
let result;
switch (func)
{
    case "sin":
        result = Math.sin(angle);
        break;
    case "cos":
        result = Math.cos(angle);
        break;
    case "tan":
        result = Math.tan(angle);
        break;
    case "√":
        result = Math.sqrt(angle);
        break;
    case "pow":
        let power = prompt("enter the power:");
        result = Math.pow(angle,power);
      break;
    default:
        console.log("Undefined");
        return;
}
    console.log(result);
    document.getElementById("result").value = result;
}
  
    
    
  
  