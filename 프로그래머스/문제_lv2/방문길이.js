function solution(dirs) {
  var answer = 0;

  let set = new Set();

  let curX = 0;
  let curY = 0;
  let prev = "";

  for (const dir of dirs) {
    prev = "" + curX + curY;
    if (dir === "U" && curY + 1 <= 5) curY += 1;
    else if (dir === "D" && curY - 1 >= -5) curY -= 1;
    else if (dir === "R" && curX + 1 <= 5) curX += 1;
    else if (dir === "L" && curX - 1 >= -5) curX -= 1;
    else continue;

    set.add(curX + (curY + prev));
    set.add(prev + curX + curY);
  }
  answer = set.size / 2;

  return answer;
}
