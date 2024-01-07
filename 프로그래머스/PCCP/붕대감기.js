function solution(bandage, health, attacks) {
  var answer = 0;

  const [time, heal, add] = bandage;

  let attObj = {};
  for (const attack of attacks) {
    const [attTime, damage] = attack;
    attObj[attTime] = damage;
  }

  let currHealth = health;
  let succ = 0;
  const end = attacks[attacks.length - 1][0];
  for (let i = 0; i <= end; i++) {
    if (currHealth <= 0) return -1;
    if (attObj[i]) {
      succ = 0;
      currHealth -= attObj[i];
      continue;
    }
    if (currHealth >= health) {
      currHealth = health;
    } else {
      succ++;
      if (succ === time) {
        currHealth += heal;
        currHealth += add;
        succ = 0;
      } else {
        currHealth += heal;
      }
    }
  }

  answer = currHealth <= 0 ? -1 : currHealth;

  return answer;
}
