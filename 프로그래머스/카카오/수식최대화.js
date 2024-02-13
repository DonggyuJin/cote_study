const calculate = (caseType, strArray) => {
  switch (caseType) {
    case "+":
      return strArray.reduce((acc, val) => acc + Number(val), 0);
    case "-":
      return (
        strArray.reduce((acc, val) => acc - Number(val), 0) + strArray[0] * 2
      );
    case "*":
      return strArray.reduce((acc, val) => acc * Number(val), 1);
    default:
      return [];
  }
};

function solution(expression) {
  const cases = ["+*-", "+-*", "-*+", "-+*", "*-+", "*+-"];
  let maxValue = -Infinity;
  cases.forEach((caseTypes) => {
    const [thirdPriority, secondPriority, firstPriority] = caseTypes.split("");

    const splitCase = expression
      .split(thirdPriority)
      .map((str) =>
        str.split(secondPriority).map((str) => str.split(firstPriority))
      );
    const result = calculate(
      thirdPriority,
      splitCase.map((str) =>
        calculate(
          secondPriority,
          str.map((str) => calculate(firstPriority, str))
        )
      )
    );
    maxValue = Math.max(maxValue, Math.abs(result));
  });

  return maxValue;
}
