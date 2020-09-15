#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const c = 'C is fun';
  for (let i = 0; i < parseInt(process.argv[2]); i++) {
    console.log(c);
  }
}
