function solution(maps) {
  var answer = -1;

  const n = maps.length;
  const m = maps[0].length;

  const dx = [0, 1, 0, -1];
  const dy = [1, 0, -1, 0];

  const q = [];
  q.push([0, 0, 1]);

  while (q.length) {
    let [x, y, cnt] = q.shift();

    if (x < 0 || x >= n || y < 0 || y >= m) continue;
    if (maps[x][y] === 0) continue;
    if (x === n - 1 && y === m - 1) return cnt;

    maps[x][y] = 0;

    for (let i = 0; i < 4; i++) {
      let nx = x + dx[i];
      let ny = y + dy[i];

      q.push([nx, ny, cnt + 1]);
    }
  }

  return answer;
}
