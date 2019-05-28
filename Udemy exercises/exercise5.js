// Complete the below questions using this array:
const array2 = [
  {
    username: "john",
    team: "red",
    score: 5,
    items: ["ball", "book", "pen"]
  },
  {
    username: "becky",
    team: "blue",
    score: 10,
    items: ["tape", "backpack", "pen"]
  },
  {
    username: "susy",
    team: "red",
    score: 55,
    items: ["ball", "eraser", "pen"]
  },
  {
    username: "tyson",
    team: "green",
    score: 1,
    items: ["book", "pen"]
  },

];

//Create an array using forEach that has all the usernames with a "!" to each of the usernames
//console.log(array[0]);
let mark = []
array2.forEach(u => {
//  let obj = u;
//  obj.username += '!';
// mark.push(obj.username);
  let x = u.username + "!";
  mark.push(x);
});
console.log("forEach is", mark, 'array2 = ',array2[0]);


// let newArray = []
// array.forEach(user => {
//   let { username } = user;
//   username = username + "!";
//   newArray.push(username);
// })
// console.log(newArray);
// console.log("Array after foreach", array2[0]);

// //Create an array using map that has all the usernames with a "? to each of the usernames
const ar = array2.map(user => {
  //let object = user;
  return user.username + "?";
})
console.log("mapArray is", ar);
// console.log("array now is", array[0]);

//Filter the array to only include users who are on team: red
const arra = array2.filter(u => {
  let object = u;
  return object.team === "red";
})
console.log("filterArray is", arra);

//Find out the total score of all users using reduce
const totalnum = array2.reduce((accum, num) => {
  return accum + num.score;
}, 0); 
console.log("Reduce is", totalnum);


// (1), what is the value of i?
// (2), Make this map function pure:
const arrayNum = [1, 2, 4, 5, 8, 9];
const newArray = arrayNum.map((num, i) => {
	console.log(num, i);
	alert(num);
	return num * 2;
})

// BONUS: create a new list with all user information, but add "!" to the end of each items they own.
// let i = 0
// const arr = array2.map(user => {
//   //let object = user;
//   for (let i=0; i<user.length; i++);
//   return user.items[i] + "!";
// })
// console.log("mapArray is", arr);


const answer = array2.map(user => {
  user.items = user.items.map(item => {
    return item + "!"
  });
  return user;
})
console.log(answer);