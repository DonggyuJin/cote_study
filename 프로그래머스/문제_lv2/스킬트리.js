function solution(skill, skill_trees) {
  var answer = 0;

  let newSkill = [];
  for (const tree of skill_trees) {
    newSkill.push(tree.split("").filter((el) => skill.includes(el)));
  }

  const originSkill = skill.split("");
  for (const tree of newSkill) {
    let temp = 0;
    for (let i = 0; i < tree.length; i++) {
      if (originSkill[i] === tree[i]) {
        temp += 1;
      } else {
        break;
      }
    }
    if (temp === tree.length) answer += 1;
  }

  return answer;
}
