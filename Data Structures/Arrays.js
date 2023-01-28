var dinnerChioce = [["Salad","Soup","Cheese plate"], ["Chicken","Salmon","Lasagna"]]
let appIndex = 0
let mainDishIndex= 1
// To access data:
let firstApp = dinnerChioce[appIndex][0]
let secondApp = dinnerChioce[appIndex][1]
let thirdMainDish= dinnerChioce[mainDishIndex][2]
console.log(firstApp)
console.log(secondApp)
console.log(thirdMainDish)
dinnerChioce[mainDishIndex][0] = "steak"
console.log(dinnerChioce)