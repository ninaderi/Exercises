//Debugging
const flattened = [[0,1], [2,3], [4,5]].reduce(
	(accumulator, array) => {
		console.log("Array", array);
		console.log("Accumulator", accumulator);
		return accumulator.concat(array)
	}, []); // I want the accumulator to start with an empty array

const flattened = [[0,1], [2,3], [4,5]].reduce(
	(accumulator, array) => {
		debugger;
		return accumulator.concat(array)
	}, []);


//Promises
const promise = new Promise((resolve, reject) => {
	if(true) {
		resolve('Stuff Worked');
	} else {
		reject('Error, it broke')
	}
})

// promise.then(result => console.log(result));

//Chaining with promises
promise
	.then(result => result + '!')
	.then(result2 => {
		throw Error
		console.log(result2);
	})
	.catch(() => console.log('errrroooorrr!'))


promise
	.then(result => result + '!')
	.then(result2 => result2 + '?')
	.catch(() => console.log('errrroooorrr!'))
	.then(result3 => {
		console.log(result3 + '!');
	})

	

const promise2 = new Promise((resolve, reject) => {
	setTimeout(resolve, 100, 'Hiiiii')
})

const promise3 = new Promise((resolve, reject) => {
	setTimeout(resolve, 1000, 'Pookie')
})

const promise4 = new Promise((resolve, reject) => {
	setTimeout(resolve, 5000, 'Are you looking for me??')
})

Promise.all([promise, promise2, promise3, promise4])
	.then(values => {
		console.log(values);
	})


const urls = [
	'https://jsonplaceholder.typicode.com/users',
	'https://jsonplaceholder.typicode.com/posts',
	'https://jsonplaceholder.typicode.com/albums',
]

Promise.all(urls.map(url => {
	return fetch(url).then(resp => resp.json())
})).then(results => {
	console.log(results[0])
	console.log(results[1])
	console.log(results[2])
}).catch(() => console.log('errrroooorrr'))

// Async Await
async function fetchUsers() {
	const resp = await fetch('https://jsonplaceholder.typicode.com/users')
	const data = await resp.json();
	console.log(resp);
}


//Object spread operator
const animals = {
	tiger: 20,
	lion: 8,
	bunny: 3,
	kitty: 2
}

function objectSpread(p1, p2, p3) {
	console.log(p1)
	console.log(p2)
	console.log(p3)
}

const { tiger, lion, ...rest } = animals;

objectSpread(tiger, lion, rest);
