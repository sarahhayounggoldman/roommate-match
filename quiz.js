'use strict';
 
// helper funcs
 
// creates and returns a radio button
function helperRadio(option, index, number) {
   // creating the elements
   var label = $("<label>").text(option);
   var input = $("<input>", {"type" : "radio", "name" : "q"+index, "value" : number});
   // building the tree
   var radio = $("<p>").append(input).append(label);
   // returning the tree
   return radio;
}
 
// creates and returns a section containing a question and answers for the quint questions
function helperQuestionDorms (questionObject, index) {
    //building the elements
    var section = $("<section>", {"class" : "text-answer",
                                 "data-answer" : questionObject.ANS});
    var question = $("<p>").attr("class", "question").text(questionObject.Q);
    // building the tree
    $(section).append(question)
                     .append(helperRadio(questionObject.A, index, "1"))
                     .append(helperRadio(questionObject.B, index, "2"))
                     .append(helperRadio(questionObject.C, index, "3"))
   // returning the tree
   return section;
}

// creates and returns a section containing a question and answers for the questions w 5 options
function helperQuestion1to5 (questionObject, index) {
   // building the elements
   var section = $("<section>", {"class" : "text-answer",
                                 "data-answer" : questionObject.ANS});
   var question = $("<p>").attr("class", "question").text(questionObject.Q);
   // building the tree
   $(section).append(question)
                     .append(helperRadio(questionObject.A, index, "1"))
                     .append(helperRadio(questionObject.B, index, "2"))
                     .append(helperRadio(questionObject.C, index, "3"))
                     .append(helperRadio(questionObject.D, index, "4"))
                     .append(helperRadio(questionObject.E, index, "5"))
   // returning the tree
   return section;
}
 
 
// event handlers
 
$("main").one().on("click", "button", function (event) {helperEvent(event);});
 
// need a handler that does the math for the question, making a "point"

// add elements to page
 
questions.forEach(function(element, index) {
   var q = new Question(element, index);
   q.addToDom("#row");});

