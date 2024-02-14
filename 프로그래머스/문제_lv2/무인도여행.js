function solution(maps) {
  var answer = [];

  const m = maps.length;
  const n = maps[0].length;
  const dy = [0, 1, 0, -1];
  const dx = [1, 0, -1, 0];

  const visited = Array.from(Array(m), () => new Array(n).fill(0));

  let temp = 0;
  const dfs = (y, x) => {
    for (let i = 0; i < 4; i++) {
      const ny = y + dy[i];
      const nx = x + dx[i];
      if (ny >= 0 && ny < m && nx >= 0 && nx < n) {
        if (maps[ny][nx] !== "X" && visited[ny][nx] === 0) {
          visited[ny][nx] = 1;
          temp += +maps[ny][nx];
          dfs(ny, nx);
        }
      }
    }
    return temp;
  };

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (maps[i][j] !== "X" && visited[i][j] === 0) {
        visited[i][j] = 1;
        temp = +maps[i][j];
        dfs(i, j);
        answer.push(temp);
        temp = 0;
      }
    }
  }

  answer = answer.sort((a, b) => a - b);

  return answer.length === 0 ? [-1] : answer;
}
