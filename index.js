// function quicksort(array)  {
//     if (array.length < 2) return array
//     const pivot = array[0]
//     const less = array.slice(1).filter(num  => {
//          return num <= pivot
//     })
//     const greater = array.slice(1).filter(num  => {
//         return num > pivot
//     })

//     return [...quicksort(less) , pivot , ...quicksort(greater)]
// }

// const quickArray = [3,7,0,5,32,56,2]
// // console.log(quicksort(quickArray))

// class Ticket {
//     constructor(name,age,gender){
//         this.name = name
//         this.age = age
//         this.gender = gender
//     }

//     greeting() {
//         console.log(this.name,'Welcome to website')
//     }

//     static result() {
//         console.log('Results are not manilpulated by outside')
//     }

// }

// const person = new Ticket('shubham',18,'male')
// // console.log(person.greeting())

function sum(x) {
    let total = 0
    for (let i = 0; i <= x; i++) {
        total += i
    }
    return total
}

console.log(sum(5))