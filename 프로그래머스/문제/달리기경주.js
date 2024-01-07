function solution(players, callings) {
  var answer = [];

  //     for(const call of callings){
  //         const idx= players.indexOf(call);
  //         let temp = players[idx-1];
  //         players[idx-1] = players[idx];
  //         players[idx] = temp;
  //     }

  //     answer = players;

  //     let pObj = {};
  //     for(let i=0; i<players.length; i++){
  //         pObj[players[i]] = players.length-i;
  //     }

  //     for(const call of callings){
  //         const num = pObj[call] + 1;
  //         pObj[Object.keys(pObj).find(key => pObj[key] === num)] -= 1;
  //         pObj[call] = num;
  //     }

  //     pObj = Object.fromEntries(Object.entries(pObj).sort((a,b) => b[1]-a[1]));
  //     for(const key of Object.keys(pObj)){
  //         answer.push(key);
  //     }

  let pObj = {};
  for (let i = 0; i < players.length; i++) {
    pObj[players[i]] = i;
  }

  for (let i = 0; i < callings.length; i++) {
    const idx = pObj[callings[i]];
    const temp = players[idx - 1];
    players[idx - 1] = callings[i];
    players[idx] = temp;

    pObj[callings[i]] = idx - 1;
    pObj[temp] = idx;
  }

  answer = players;

  return answer;
}
