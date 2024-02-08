function solution(book_time) {
  var answer = 0;

  for (let i = 0; i < book_time.length; i++) {
    let [start, end] = book_time[i];
    const [sh, sm] = start.split(":").map(Number);
    const [eh, em] = end.split(":").map(Number);
    book_time[i][0] = sh * 60 + sm;
    book_time[i][1] = eh * 60 + em;
  }

  book_time = book_time.sort(([as, ae], [bs, be]) => as - bs);

  const checked = Array.from(Array(book_time.length), () => 0);

  let time;
  for (let i = 0; i < book_time.length; i++) {
    if (checked[i]) continue;
    let flag = false;
    const [prevS, prevE] = book_time[i];
    time = prevE + 10;
    for (let j = i + 1; j < book_time.length; j++) {
      const [currS, currE] = book_time[j];
      if (time <= currS && !checked[j]) {
        time = currE + 10;
        flag = true;
        checked[i] = 1;
        checked[j] = 1;
      }
    }
    if (flag) answer += 1;
  }

  answer += checked.filter((el) => el === 0).length;

  return answer;
}
