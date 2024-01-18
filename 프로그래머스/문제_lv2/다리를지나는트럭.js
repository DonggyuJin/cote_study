function solution(bridge_length, weight, truck_weights) {
  var answer = 0;

  let bridge = [];
  let sum = 0;
  for (let i = 0; i < bridge_length; i++) {
    bridge.push(0);
  }

  while (true) {
    let pl = bridge.shift();
    sum -= pl;

    if (sum + truck_weights[0] > weight) {
      bridge.push(0);
    } else {
      sum += truck_weights[0];
      bridge.push(truck_weights[0]);
      truck_weights.shift();
    }

    answer += 1;

    if (truck_weights.length === 0) {
      for (let i = 0; i < bridge_length; i++) {
        answer += 1;
      }
      return answer;
    }
  }

  return answer;
}
