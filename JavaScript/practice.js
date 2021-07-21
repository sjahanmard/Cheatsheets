/* arrow functions */
const sal = function (num) {
  num * num;
};
const sal = (num) => num * num;
console.log(sal);
/*template literal: use back tick to put dynamic variables in there*/
const string = `this is a word ${faradars}`;
/*destructuring*/
const stundet = {
    firstname = 'ali', 
    lastname='ahmadi',
};
student.firstname

const {firstname , lastname} = student;
// then just call it like : firstname
/*ternary operator*/
let age = 18
if (age>=18) {
    alert ('welcome to my website')
}else{
    alert('no information found')
};
age >= 18 ? alert('welcome to my webside') : alert('no information found')
/*export & import*/
export const a = [ 1 , 2 , 3 ,4]
import {a} from "./javascript.js"
export default class boob{

}
import boob from "./javascript.js"

/*map*/
const myArray = [1,2,3,4]
const newArray = myArray.map((value,index,array)=> value*2);
// Person is a function that we imported here and persons is a list
const personList = persons.map (person => <Person key={person.id} person={person} />)
// at the end of the above line weare setting a property with the name person
// which is exactly our own person
/*filter*/
const myArray = [1,2,3,4]
const newArray = myArray.filter((value,index,array) => value%2 == 0);

/*reduce*/

const myArray = [1,2,3,4]
const newArray = myArray.reduce((acc,currValue,currIndex, array) => value%2 == 0);