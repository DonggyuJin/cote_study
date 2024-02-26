function solution(board) {
  var answer = 0;

  let row = board.length;
  let column = board[0].length;

  if (row === 1 || column === 1) return 1;

  for (let i = 1; i < row; i++) {
    for (let j = 1; j < column; j++) {
      if (board[i][j] === 1) {
        let cross = board[i - 1][j - 1];
        let up = board[i - 1][j];
        let left = board[i][j - 1];
        if (cross >= 1 && up >= 1 && left >= 1) {
          board[i][j] = Math.min(cross, up, left) + 1;
        }
        answer = Math.max(answer, board[i][j]);
      }
    }
  }

  return answer ** 2;
}
