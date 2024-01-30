function solution(files) {
  var answer = [];

  const num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];

  let newFiles = [];
  for (let i = 0; i < files.length; i++) {
    const file = files[i].split("");
    let head = "";
    let number = "";
    let tail = "";
    let flag = false;
    let idx = 0;
    for (let j = 0; j < file.length; j++) {
      if (!num.includes(file[j])) {
        if (flag) break;
        head += file[j];
      } else {
        idx = j;
        number += file[j];
        flag = true;
      }
    }
    tail = file.slice(idx + 1).join("");
    newFiles.push([head, number, tail]);
  }

  newFiles = newFiles
    .sort(([a, x, y], [b, c, v]) => {
      return x - c;
    })
    .sort(([a, x, y], [b, c, v]) => {
      return a.toUpperCase().localeCompare(b.toUpperCase());
    });

  for (const file of newFiles) {
    const [head, num, tail] = file;
    answer.push(head + num + tail);
  }

  return answer;
}
