function solution(n, arr1, arr2) {
  var answer = [];

  let map1 = [];
  let map2 = [];
  for (let i = 0; i < n; i++) {
    map1.push(arr1[i].toString(2).padStart(n, "0"));
    map2.push(arr2[i].toString(2).padStart(n, "0"));
  }

  for (let i = 0; i < n; i++) {
    temp = "";
    for (let j = 0; j < n; j++) {
      if (map1[i][j] === "0" && map2[i][j] === "0") {
        temp += " ";
      } else {
        temp += "#";
      }
    }
    answer.push(temp);
  }

  console.log(map1, map2);

  return answer;
}
