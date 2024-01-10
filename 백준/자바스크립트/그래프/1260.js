class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.front = null;
    this.rear = null;
    this.size = 0;
  }

  isEmpty() {
    return this.size === 0;
  }

  push(data) {
    const newNode = new Node(data);
    if (this.isEmpty()) this.front = newNode;
    else this.rear.next = newNode;
    this.rear = newNode;
    this.size++;
  }

  shift() {
    if (this.isEmpty()) return;
    const data = this.front.data;
    this.front = this.front.next;
    this.size--;
    return data;
  }
}

const fs = require("fs");
const path = process.platform === "linux" ? "/dev/stdin" : "../example.txt";
const input = fs
  .readFileSync(path)
  .toString()
  .trim()
  .split("\n")
  .map((x) => x.split(" ").map(Number));

const [N, M, V] = input[0];
// let graph = new Array(N + 1);
// for (let i = 0; i < graph.length; i++) {
//   graph[i] = [];
// }
let graph = Array.from(Array(N + 1), () => []);

for (let i = 0; i < M; i++) {
  const [a, b] = input[i + 1];
  graph[a].push(b);
  graph[b].push(a);
}

console.log(graph);

graph.forEach((element) => {
  element.sort((a, b) => a - b);
});

let visited = new Array(N + 1).fill(0);
let dfs_result = [];

function DFS(v) {
  if (visited[v]) return;
  visited[v] = 1;
  dfs_result.push(v);
  for (let i = 0; i < graph[v].length; i++) {
    let next = graph[v][i];
    if (visited[next] === 0) {
      DFS(next);
    }
  }
}
DFS(V);
console.log(dfs_result.join(" "));

let bfs_result = [];
visited.fill(0);

function BFS(v) {
  let queue = new Queue();
  queue.push(v);

  while (!queue.isEmpty()) {
    let x = queue.shift();
    if (visited[x] === 1) {
      continue;
    }
    visited[x] = 1;
    bfs_result.push(x);
    for (let i = 0; i < graph[x].length; i++) {
      let next = graph[x][i];
      if (visited[next] === 0) {
        queue.push(next);
      }
    }
  }
}
BFS(V);
console.log(bfs_result.join(" "));
