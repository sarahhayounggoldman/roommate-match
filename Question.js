'use strict';
 
// QUESTION CLASS
class Question {
  
   // creates a Question object
   constructor(questionObject, index){
       this.$dom = helperQuestion(questionObject, index)
   }
 
   // adds the Question object to the given location in the DOM
   addToDom(destination){
       $(this.$dom).appendTo(destination);
   }
}