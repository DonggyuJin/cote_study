function solution(str1, str2) {
  //     var answer = 0;

  //     let map1 = {};
  //     let map2 = {};
  //     for(let i=0; i<str1.length; i++){
  //         if(str1.slice(i, i+2).match(/^[a-z][a-z]$/i)){
  //             if(map1[str1.slice(i, i+2).toLowerCase()]) map1[str1.slice(i, i+2).toLowerCase()] += 1;
  //             else map1[str1.slice(i, i+2).toLowerCase()] = 1;
  //         }

  //     }
  //     for(let i=0; i<str2.length; i++){
  //         if(str2.slice(i, i+2).match(/^[a-z][a-z]$/i)){
  //                 if(map2[str2.slice(i, i+2).toLowerCase()]) map2[str2.slice(i, i+2).toLowerCase()] += 1;
  //                 else map2[str2.slice(i, i+2).toLowerCase()] = 1;
  //             }
  //     }

  //     const mapArr1 = Object.keys(map1);
  //     const mapArr2 = Object.keys(map2);
  //     let a = 0;
  //     let z = {};
  //     for(let i=0; i<mapArr1.length; i++){
  //         for(let j=0; j<mapArr2.length; j++){
  //             if(mapArr1[i] === mapArr2[j]) {
  //                 a += Math.min(map1[mapArr1[i]], map2[mapArr2[j]]);
  //                 z[mapArr1[i]]= Math.max(map1[mapArr1[i]], map2[mapArr2[j]]);
  //             } else {
  //                 if(!z[mapArr1[i]]){
  //                     z[mapArr1[i]] = map1[mapArr1[i]];
  //                 }
  //                 if(!z[mapArr2[i]]){
  //                     z[mapArr2[i]] = map2[mapArr2[i]];
  //                 }
  //             }
  //         }
  //     }

  //     let c = 0;
  //     for(const el in z){
  //         c += z[el];
  //     }

  //     answer = parseInt((a / c) * 65536);
  //     if(isNaN(answer)) return 65536;

  //     return answer;
  function explode(text) {
    const result = [];
    for (let i = 0; i < text.length - 1; i++) {
      const node = text.substr(i, 2);
      if (node.match(/[A-Za-z]{2}/)) {
        result.push(node.toLowerCase());
      }
    }
    return result;
  }

  const arr1 = explode(str1);
  const arr2 = explode(str2);
  const set = new Set([...arr1, ...arr2]);
  let union = 0;
  let intersection = 0;

  set.forEach((item) => {
    const has1 = arr1.filter((x) => x === item).length;
    const has2 = arr2.filter((x) => x === item).length;
    union += Math.max(has1, has2);
    intersection += Math.min(has1, has2);
  });
  return union === 0 ? 65536 : Math.floor((intersection / union) * 65536);
}
