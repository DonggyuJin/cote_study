function solution(n, wires) {
  var answer = [];

  const dict = {};
  for (const wire of wires) {
    if (!(wire[0] in dict)) dict[wire[0]] = [wire[1]];
    else dict[wire[0]].push(wire[1]);
    if (!(wire[1] in dict)) dict[wire[1]] = [wire[0]];
    else dict[wire[1]].push(wire[0]);
  }

  for (const wire of wires) {
    const [s, e] = wire;
    const stack = [...dict[s]];
    const visited = {};
    let cnt = 1;

    visited[s] = true;
    visited[e] = true;

    while (stack.length !== 0) {
      const temp = stack.pop();
      if (!visited[temp]) {
        visited[temp] = true;
        stack.push(...dict[temp]);
        cnt += 1;
      }
    }

    answer.push(Math.abs(cnt * 2 - n));
  }

  return Math.min(...answer);
}
