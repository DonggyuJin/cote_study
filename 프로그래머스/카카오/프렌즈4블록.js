function solution(m, n, board) {
  var answer = 0;

  board = board.map((e) => e.split(""));

  while (true) {
    let block = [];

    for (let i = 0; i < m - 1; i++) {
      for (let j = 0; j < n - 1; j++) {
        let current = board[i][j];

        if (
          current &&
          current === board[i][j + 1] &&
          current === board[i + 1][j] &&
          current === board[i + 1][j + 1]
        ) {
          block.push([i, j]);
        }
      }
    }

    if (block.length === 0) {
      break;
    }

    block.forEach((e) => {
      let [i, j] = e;

      board[i][j] = 0;
      board[i][j + 1] = 0;
      board[i + 1][j] = 0;
      board[i + 1][j + 1] = 0;
    });

    for (let j = 0; j < n; j++) {
      for (let i = m - 1; i > 0; i--) {
        if (board[i][j] === 0) {
          for (let k = i - 1; k >= 0; k--) {
            if (board[k][j] !== 0) {
              board[i][j] = board[k][j];
              board[k][j] = 0;
              break;
            }
          }
        }
      }
    }
  }

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] === 0) {
        answer++;
      }
    }
  }

  return answer;
}
