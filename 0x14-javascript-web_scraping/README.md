# 0x14. JavaScript - Web scraping
Manipulating JSON Data:
JavaScript provides easy ways to work with JSON data. JSON objects are native JavaScript objects, and you can manipulate them using standard object manipulation techniques. Here's a basic example of how to manipulate JSON data:

// Sample JSON data
const jsonData = '{"name": "John", "age": 30, "city": "New York"}';

// Parsing JSON to JavaScript object
const parsedData = JSON.parse(jsonData);

// Accessing JSON properties
console.log(parsedData.name); // Outputs: John

// Modifying JSON properties
parsedData.age = 31;

// Converting JavaScript object back to JSON
const updatedJsonData = JSON.stringify(parsedData);

