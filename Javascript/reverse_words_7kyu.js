// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
// Examples

// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"

function reverseWords(str) {
    // split it by space > map it > split (no space) each word in to letters > reverse each letter, join them
    let mapit = str.split(" ").map(each_word => each_word.split("").reverse().join(""));
    // return the str and join them by adding space inbetween the words
    return mapit.join(" ");
  }