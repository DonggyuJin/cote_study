function solution(keymap, targets) {
  var answer = [];

  let hashMap = {};

  for (const key of keymap) {
    for (let i = 0; i < key.length; i++) {
      if (key[i] in hashMap) {
        hashMap[key[i]] = Math.min(hashMap[key[i]], i + 1);
      } else {
        hashMap[key[i]] = i + 1;
      }
    }
  }

  for (const target of targets) {
    temp = 0;
    for (let i = 0; i < target.length; i++) {
      temp += hashMap[target[i]];
    }

    if (isNaN(temp)) {
      answer.push(-1);
    } else {
      answer.push(temp);
    }
  }

  return answer;
}
