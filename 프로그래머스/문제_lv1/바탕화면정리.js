function solution(wallpaper) {
  var answer = [];

  let minRow = Number.MAX_VALUE;
  let maxRow = Number.MIN_VALUE;
  let minCol = Number.MAX_VALUE;
  let maxCol = Number.MIN_VALUE;

  const row = wallpaper.length;
  const col = wallpaper[0].length;

  for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
      if (wallpaper[i][j] === "#") {
        minRow = Math.min(minRow, i);
        minCol = Math.min(minCol, j);
        maxRow = Math.max(maxRow, i);
        maxCol = Math.max(maxCol, j);
      }
    }
  }

  answer = [minRow, minCol, maxRow + 1, maxCol + 1];

  return answer;
}
