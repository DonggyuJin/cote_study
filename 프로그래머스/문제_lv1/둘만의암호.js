function solution(s, skip, index) {
  var answer = "";

  const alpha = "abcdefghijklmnopqrstuvwxyz";
  let alp = [...alpha];

  for (let i = 0; i < skip.length; i++) {
    alp = alp.filter((el) => el !== skip[i]);
  }

  for (let i = 0; i < s.length; i++) {
    let idx = alp.findIndex((el) => el === s[i]);
    idx += index;
    if (idx >= alp.length) {
      answer += alp[idx % alp.length];
    } else {
      answer += alp[idx];
    }
  }

  return answer;
}
