function solution(board, moves) {
  var answer = 0;

  let basket = [];

  for (const move of moves) {
    for (let i = 0; i < board.length; i++) {
      if (board[i][move - 1] !== 0) {
        basket.push(board[i][move - 1]);

        if (basket[basket.length - 2] === basket[basket.length - 1]) {
          basket.pop();
          basket.pop();
          answer += 2;
        }

        board[i][move - 1] = 0;
        break;
      }
    }
  }

  return answer;
}
