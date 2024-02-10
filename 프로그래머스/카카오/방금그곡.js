function solution(m, musicinfos) {
  var answer = "";

  let mel = m.split("");
  for (let i = 0; i < mel.length + 1; i++) {
    if (mel[i] === "#") {
      mel[i - 1] += "#";
      mel[i] = " ";
    }
  }
  mel = mel.filter((el) => el !== " ");
  mel = [...mel];
  const temp = {};
  for (let x = 0; x < musicinfos.length; x++) {
    let [start, end, name, music] = musicinfos[x].split(",");
    const [sh, sm] = start.split(":").map(Number);
    const [eh, em] = end.split(":").map(Number);
    const time = 60 * eh + em - (60 * sh + sm);
    const cnt = time - music.length;
    let musics;
    if (cnt > 0) musics = music.repeat(cnt + 1);
    else {
      let temp = music.split("");
      for (let i = 0; i < temp.length; i++) {
        if (temp[i] === "#") {
          temp[i - 1] += "#";
          temp[i] = " ";
        }
      }
      temp = temp.filter((el) => el !== " ");
      musics = temp.slice(0, time).join("").repeat(2);
    }

    let tempMel = musics.split("");
    for (let i = 0; i < tempMel.length + 1; i++) {
      if (tempMel[i] === "#") {
        tempMel[i - 1] += "#";
        tempMel[i] = " ";
      }
    }
    tempMel = tempMel.filter((el) => el !== " ");
    for (let i = 0; i < tempMel.length; i++) {
      if (
        JSON.stringify(tempMel.slice(i, i + mel.length)) === JSON.stringify(mel)
      ) {
        temp[name] = time;
      }
    }
  }

  if (Object.entries(temp).length === 0) return "(None)";
  else {
    const result = Object.entries(temp).sort(([an, at], [bn, bt]) => bt - at);
    answer = result[0][0];
  }

  return answer;
}
