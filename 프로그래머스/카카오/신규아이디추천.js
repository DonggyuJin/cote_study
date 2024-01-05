function solution(new_id) {
  var answer = "";

  new_id = new_id.toLowerCase(); // 1단계
  new_id = new_id
    .split("")
    .filter((id) => id.match(/[a-z]|[0-9]|-|_|\./g))
    .join(""); // 2단계
  new_id = new_id.replaceAll(/\.+/g, "."); // 3단계
  new_id = new_id.replaceAll(/^\.|\.$/g, ""); // 4단계
  if (new_id === "") new_id += "a"; // 5단계
  if (new_id.length >= 16) {
    new_id = new_id.slice(0, 15);
    new_id = new_id.replace(/\.$/g, "");
  } // 6단계
  if (new_id.length <= 2) {
    const str = new_id[new_id.length - 1];
    while (new_id.length !== 3) {
      new_id += str;
    }
  } // 7단계

  answer = new_id;

  return answer;
}
