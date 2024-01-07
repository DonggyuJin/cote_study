function solution(park, routes) {
  var answer = [];

  const move = { E: 1, S: 1, N: -1, W: -1 }; // j,i,i,j
  const newP = park.map((p) => p.split(""));

  let pos;
  for (let i = 0; i < newP.length; i++) {
    for (let j = 0; j < newP[i].length; j++) {
      if (newP[i][j] === "S") pos = [i, j];
    }
  }

  let flag;
  let one = 1;
  for (const route of routes) {
    flag = true;
    let [mv, d] = route.split(" ");
    let [x, y] = pos;
    const tempX = x;
    const tempY = y;

    for (let i = 1; i <= +d; i++) {
      if (mv === "S" || mv === "N") {
        if (
          x + move[mv] * one < 0 ||
          x + move[mv] * one >= newP.length ||
          newP[x + move[mv] * one][y] === "X"
        ) {
          flag = false;
          continue;
        }
        x += move[mv] * one;
      } else {
        if (
          y + move[mv] * one < 0 ||
          y + move[mv] * one >= newP[0].length ||
          newP[x][y + move[mv] * one] === "X"
        ) {
          flag = false;
          continue;
        }
        y += move[mv] * one;
      }
    }
    if (flag === false) {
      x = tempX;
      y = tempY;
    }
    pos = [x, y];
  }

  answer = pos;

  return answer;
}

// 참고
// function solution(park, routes) {
//     const dirs = { E: [0, 1], W: [0, -1], S: [1, 0], N: [-1, 0] };
//     let [x, y] = [0, 0];
//     for (let i = 0; i < park.length; i++) {
//       if (park[i].includes('S')) {
//         [x, y] = [i, park[i].indexOf('S')];
//         break;
//       }
//     }

//     routes.forEach((route) => {
//       const [r, n] = route.split(' ');
//       let [nx, ny] = [x, y];
//       let cnt = 0;
//       while (cnt < n) {
//         [nx, ny] = [nx + dirs[r][0], ny + dirs[r][1]];
//         if (!park[nx] || !park[nx][ny] || park[nx][ny] === 'X') break;
//         cnt++;
//       }
//       if (cnt == n) [x, y] = [nx, ny];
//     });
//     return [x, y];
//   }
